#!/usr/bin/env python3
"""Post-process the LinkML-generated OWL ontology.

The LinkML OWL generator mints every class/slot's own node IRI from the
schema's default prefix (``sbco:``) and only records cross-vocabulary
mappings declared via ``exact_mappings:`` as ``skos:exactMatch`` — which is
SKOS concept-mapping metadata, not an OWL equivalence axiom. Nothing in the
generated file lets a standard OWL/SPARQL reasoner treat ``sbco:Building``
and ``rec:Building`` (or ``sbco:hasPart`` and ``rec:hasPart``) as the same
class/property.

This script adds the missing axioms: for every ``skos:exactMatch`` triple
whose subject is an ``owl:Class``, it asserts ``owl:equivalentClass``; for
every ``skos:exactMatch`` triple whose subject is an ``owl:ObjectProperty``
or ``owl:DatatypeProperty``, it asserts ``owl:equivalentProperty``. The
``skos:exactMatch`` triples themselves are left in place (harmless
traceability metadata).

Note on ``hasPoint``/``isPointOf``: these two slots are constrained
per-class via a ``slot_usage.any_of`` override at every usage site (see
``schema/building_model_owl.yaml``). Earlier revisions of this script tried
to fix a validation-bypass bug here by dropping their global ``rdfs:range``
entirely — but LinkML's OWL generator needs *some* class-valued range to
know a slot is an ``owl:ObjectProperty`` rather than an
``owl:DatatypeProperty``, so that produced invalid OWL (these two ended up
typed as ``owl:DatatypeProperty`` while still being used with class-valued
restrictions elsewhere). The actual fix now lives in the schema itself:
both slots declare `range: Resource` — broad enough that it doesn't
collapse the ``any_of`` union via ``owl:intersectionOf`` the way a narrow
range (``Point``/``Equipment``) did, but not itself a class any SHACL shape
here checks for, so RDFS range entailment can no longer launder
wrongly-typed values (e.g. an ``EquipmentExt`` used as a ``hasPoint``
target) past the SHACL checks that exist to catch that mistake. See the
comments next to ``hasPoint``/``isPointOf`` in
``schema/building_model_owl.yaml`` for the full explanation.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from rdflib import Graph, Namespace, OWL, RDF, URIRef

SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

_PROPERTY_TYPES = (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)


def add_equivalence_axioms(graph: Graph) -> int:
    added = 0
    for subject, _, obj in list(graph.triples((None, SKOS.exactMatch, None))):
        if not isinstance(subject, URIRef) or not isinstance(obj, URIRef):
            continue
        if (subject, RDF.type, OWL.Class) in graph:
            triple = (subject, OWL.equivalentClass, obj)
        elif any((subject, RDF.type, ptype) in graph for ptype in _PROPERTY_TYPES):
            triple = (subject, OWL.equivalentProperty, obj)
        else:
            continue
        if triple not in graph:
            graph.add(triple)
            added += 1
    return added


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("owl_ttl", type=Path, help="Path to the generated OWL Turtle file (edited in place).")
    args = parser.parse_args()

    graph = Graph()
    graph.parse(args.owl_ttl, format="turtle")
    added = add_equivalence_axioms(graph)
    graph.serialize(destination=str(args.owl_ttl), format="turtle")
    print(f"postprocess_owl: added {added} owl:equivalentClass/equivalentProperty axioms to {args.owl_ttl}")


if __name__ == "__main__":
    main()
