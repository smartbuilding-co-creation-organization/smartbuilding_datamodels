#!/usr/bin/env python3
from __future__ import annotations

import argparse
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from linkml_runtime.utils.schemaview import SchemaView
from owlrl import DeductiveClosure, OWLRL_Semantics
from pyshacl import validate
from rdflib import Graph, Namespace, OWL, RDF, RDFS, URIRef

from convert_yaml_to_ttl import ConversionConfig, build_graph, expand_uri, normalize_prefix_map

LOGGER = logging.getLogger(__name__)
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")


@dataclass(frozen=True)
class InferenceExpectation:
    subject: str
    types: list[str]


@dataclass(frozen=True)
class CaseExpectation:
    shacl_conforms: bool
    inferred_types: list[InferenceExpectation]


@dataclass(frozen=True)
class ValidationCase:
    name: str
    input_path: Path
    output_ttl: Path | None
    root_class: str
    class_chain: list[str]
    inject_is_part_of: bool
    expected: CaseExpectation


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping at root of {path}, got {type(data)}")
    return data


def parse_cases(path: Path) -> list[ValidationCase]:
    raw = load_yaml(path)
    cases_raw = raw.get("cases")
    if not isinstance(cases_raw, list):
        raise ValueError("cases must be a list")
    cases: list[ValidationCase] = []
    for item in cases_raw:
        if not isinstance(item, dict):
            raise ValueError("each case must be a mapping")
        expected_raw = item.get("expected", {})
        inferred_raw = expected_raw.get("inferred_types", [])
        inferred: list[InferenceExpectation] = []
        for entry in inferred_raw:
            if not isinstance(entry, dict):
                raise ValueError("inferred_types entries must be mappings")
            types = entry.get("types", [])
            if not isinstance(types, list):
                raise ValueError("types must be a list")
            inferred.append(
                InferenceExpectation(subject=str(entry["subject"]), types=[str(t) for t in types])
            )
        expected = CaseExpectation(
            shacl_conforms=bool(expected_raw.get("shacl_conforms", True)),
            inferred_types=inferred,
        )
        class_chain = item.get("class_chain", ["Site", "Building", "Level", "Room"])
        cases.append(
            ValidationCase(
                name=str(item["name"]),
                input_path=Path(item["input"]),
                output_ttl=Path(item["output_ttl"]) if item.get("output_ttl") else None,
                root_class=str(item.get("root_class", "Site")),
                class_chain=[str(c) for c in class_chain],
                inject_is_part_of=bool(item.get("inject_is_part_of", False)),
                expected=expected,
            )
        )
    return cases


def run_inference_checks(
    graph: Graph,
    ontology: Graph,
    schema_view: SchemaView,
    expectations: list[InferenceExpectation],
) -> list[str]:
    errors: list[str] = []
    prefix_map = normalize_prefix_map(schema_view)
    combined = Graph()
    for triple in graph:
        combined.add(triple)
    for triple in ontology:
        combined.add(triple)
    DeductiveClosure(OWLRL_Semantics).expand(combined)

    equivalence_map = build_equivalence_map(ontology)
    superclass_map = build_superclass_map(ontology)

    for expectation in expectations:
        subject_uri = expand_uri(prefix_map, expectation.subject)
        subject_types = set(combined.objects(subject_uri, RDF.type))
        available_types = expand_supertypes(subject_types, superclass_map, equivalence_map)
        for type_curie in expectation.types:
            type_uri = expand_uri(prefix_map, type_curie)
            if type_uri not in available_types:
                errors.append(
                    f"Expected inferred type missing for {expectation.subject}: {type_curie}"
                )
    return errors


def build_equivalence_map(ontology: Graph) -> dict[URIRef, set[URIRef]]:
    eq_map: dict[URIRef, set[URIRef]] = {}
    for predicate in (SKOS.exactMatch, OWL.equivalentClass):
        for subject, _, obj in ontology.triples((None, predicate, None)):
            if not isinstance(subject, URIRef) or not isinstance(obj, URIRef):
                continue
            eq_map.setdefault(subject, set()).add(obj)
            eq_map.setdefault(obj, set()).add(subject)
    return eq_map


def expand_equivalence(types: set[URIRef], eq_map: dict[URIRef, set[URIRef]]) -> set[URIRef]:
    expanded = set(types)
    stack = list(types)
    while stack:
        current = stack.pop()
        for eq in eq_map.get(current, set()):
            if eq not in expanded:
                expanded.add(eq)
                stack.append(eq)
    return expanded


def build_superclass_map(ontology: Graph) -> dict[URIRef, set[URIRef]]:
    super_map: dict[URIRef, set[URIRef]] = {}
    for subject, _, obj in ontology.triples((None, RDFS.subClassOf, None)):
        if not isinstance(subject, URIRef) or not isinstance(obj, URIRef):
            continue
        super_map.setdefault(subject, set()).add(obj)
    return super_map


def expand_supertypes(
    types: set[URIRef],
    superclass_map: dict[URIRef, set[URIRef]],
    eq_map: dict[URIRef, set[URIRef]],
) -> set[URIRef]:
    expanded = expand_equivalence(types, eq_map)
    stack = list(expanded)
    while stack:
        current = stack.pop()
        for parent in superclass_map.get(current, set()):
            for parent_eq in expand_equivalence({parent}, eq_map):
                if parent_eq not in expanded:
                    expanded.add(parent_eq)
                    stack.append(parent_eq)
    return expanded


def run_case(
    case: ValidationCase,
    schema_path: Path,
    shacl_path: Path,
    ontology_path: Path,
    use_output_ttl: bool,
) -> list[str]:
    errors: list[str] = []
    if use_output_ttl:
        if not case.output_ttl:
            return [f"Case {case.name} is missing output_ttl for --use-output-ttl"]
        if not case.output_ttl.exists():
            return [f"Case {case.name} output_ttl not found: {case.output_ttl}"]
        graph = Graph().parse(str(case.output_ttl), format="turtle")
    else:
        config = ConversionConfig(
            root_class=case.root_class,
            class_chain=case.class_chain,
            inject_is_part_of=case.inject_is_part_of,
        )
        graph = build_graph(schema_path, case.input_path, config)
        if case.output_ttl:
            case.output_ttl.parent.mkdir(parents=True, exist_ok=True)
            graph.serialize(destination=str(case.output_ttl), format="turtle")

    shacl_graph = Graph().parse(shacl_path, format="turtle")
    ont_graph = Graph().parse(ontology_path, format="turtle")
    conforms, report_graph, report_text = validate(
        data_graph=graph,
        shacl_graph=shacl_graph,
        ont_graph=ont_graph,
        inference="owlrl",
        debug=False,
    )

    if conforms != case.expected.shacl_conforms:
        errors.append(
            f"SHACL conformance mismatch for {case.name}: expected {case.expected.shacl_conforms}, got {conforms}"
        )
    if not conforms:
        report_path = None
        if case.output_ttl:
            report_path = case.output_ttl.with_suffix(".report.ttl")
            report_graph.serialize(destination=str(report_path), format="turtle")
        if case.expected.shacl_conforms:
            errors.append(
                f"SHACL validation failed for {case.name}: {report_text.strip()}"
                + (f" (report: {report_path})" if report_path else "")
            )

    schema_view = SchemaView(str(schema_path))
    if case.expected.inferred_types:
        errors.extend(run_inference_checks(graph, ont_graph, schema_view, case.expected.inferred_types))
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate converted RDF against OWL inference and SHACL expectations.",
    )
    parser.add_argument(
        "--schema",
        default="schema/building_model.yaml",
        type=Path,
        help="LinkML schema YAML path.",
    )
    parser.add_argument(
        "--shacl",
        default="output/building_model.shacl.ttl",
        type=Path,
        help="SHACL shapes Turtle path.",
    )
    parser.add_argument(
        "--ontology",
        default="output/building_model.owl.ttl",
        type=Path,
        help="OWL ontology Turtle path.",
    )
    parser.add_argument(
        "--cases",
        default="sample/validation/cases.yaml",
        type=Path,
        help="YAML file describing validation cases.",
    )
    parser.add_argument(
        "--use-output-ttl",
        action="store_true",
        help="Validate using pre-generated output_ttl files instead of converting YAML.",
    )
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = parse_args()
    cases = parse_cases(args.cases)
    if not cases:
        raise ValueError("No cases found")

    all_errors: list[str] = []
    for case in cases:
        LOGGER.info("Running case %s", case.name)
        errors = run_case(case, args.schema, args.shacl, args.ontology, args.use_output_ttl)
        all_errors.extend(errors)

    if all_errors:
        message = "\n".join(all_errors)
        raise SystemExit(f"Validation failed:\n{message}")
    LOGGER.info("All validation cases passed")


if __name__ == "__main__":
    main()
