#!/usr/bin/env python3
from __future__ import annotations

import argparse
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml
from pyshacl import validate
from linkml_runtime.utils.schemaview import SchemaView
from rdflib import Graph, Literal, Namespace, RDF, URIRef

LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class ConversionConfig:
    root_class: str
    class_chain: list[str]
    inject_is_part_of: bool
    instance_prefix: str
    instance_base: str


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping at root of {path}, got {type(data)}")
    return data


def normalize_prefix_map(schema_view: SchemaView) -> dict[str, str]:
    prefix_map: dict[str, str] = {}
    for prefix, uri in schema_view.schema.prefixes.items():
        prefix_map[prefix] = str(uri.prefix_reference)
    return prefix_map


def curie_to_uri(prefix_map: dict[str, str], value: str) -> URIRef:
    if ":" not in value:
        raise ValueError(f"Expected CURIE (prefix:value), got '{value}'")
    prefix, local = value.split(":", 1)
    if prefix not in prefix_map:
        raise KeyError(f"Unknown prefix '{prefix}' for '{value}'")
    return URIRef(prefix_map[prefix] + local)


def expand_uri(prefix_map: dict[str, str], value: str) -> URIRef:
    if value.startswith("http://") or value.startswith("https://"):
        return URIRef(value)
    if ":" in value:
        return curie_to_uri(prefix_map, value)
    raise ValueError(f"Expected CURIE or absolute URI, got '{value}'")


def slot_predicate(schema_view: SchemaView, prefix_map: dict[str, str], slot_name: str) -> URIRef:
    slot = schema_view.get_slot(slot_name)
    if slot is None:
        raise KeyError(f"Slot '{slot_name}' missing from schema")
    if slot.slot_uri:
        return expand_uri(prefix_map, str(slot.slot_uri))
    default_prefix = schema_view.schema.default_prefix
    if not default_prefix:
        raise KeyError(f"Slot '{slot_name}' missing slot_uri and schema default_prefix is not set")
    if default_prefix not in prefix_map:
        raise KeyError(
            f"Slot '{slot_name}' missing slot_uri and default prefix '{default_prefix}' is not in prefixes"
        )
    return URIRef(prefix_map[default_prefix] + slot_name)


def slot_range(schema_view: SchemaView, slot_name: str) -> str | None:
    slot = schema_view.get_slot(slot_name)
    if slot is None:
        return None
    return slot.range


def slot_range_is_class(schema_view: SchemaView, slot_name: str) -> bool:
    range_name = slot_range(schema_view, slot_name)
    if not range_name:
        return False
    return schema_view.get_class(range_name) is not None


def slot_range_is_enum(schema_view: SchemaView, slot_name: str) -> bool:
    range_name = slot_range(schema_view, slot_name)
    if not range_name:
        return False
    return schema_view.get_enum(range_name) is not None


def is_curie_or_uri(value: str) -> bool:
    return value.startswith("http://") or value.startswith("https://") or ":" in value


def class_uri(schema_view: SchemaView, prefix_map: dict[str, str], class_name: str) -> URIRef:
    class_def = schema_view.get_class(class_name)
    if class_def is None or class_def.class_uri is None:
        raise KeyError(f"Class '{class_name}' missing class_uri in schema")
    return expand_uri(prefix_map, str(class_def.class_uri))


def normalize_instance_id(prefix_map: dict[str, str], value: str, config: ConversionConfig) -> str:
    if value.startswith("http://") or value.startswith("https://") or ":" in value:
        return value
    if config.instance_prefix not in prefix_map:
        raise KeyError(f"Instance prefix '{config.instance_prefix}' is not defined in prefixes")
    return f"{config.instance_prefix}:{value}"


def add_literal(graph: Graph, subject: URIRef, predicate: URIRef, value: Any) -> None:
    graph.add((subject, predicate, Literal(value)))


def enum_literal(value: str) -> str:
    if "#" in value:
        return value.rsplit("#", 1)[-1]
    if "/" in value:
        return value.rsplit("/", 1)[-1]
    if ":" in value:
        return value.rsplit(":", 1)[-1]
    return value


def resolve_class_name(
    node: dict[str, Any],
    depth: int,
    config: ConversionConfig,
    class_override: str | None = None,
) -> str:
    for key in ("type", "@type", "class"):
        explicit = node.get(key)
        if explicit:
            return explicit
    if class_override:
        return class_override
    if depth == 0:
        return config.root_class
    if depth < len(config.class_chain):
        return config.class_chain[depth]
    return config.class_chain[-1]


def iter_child_nodes(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, list):
        for item in value:
            if isinstance(item, dict):
                yield item
            else:
                raise ValueError(f"Expected list of dicts, got {type(item)}")
    elif isinstance(value, dict):
        yield value
    else:
        raise ValueError(f"Expected dict or list for inlined slot, got {type(value)}")


def convert_node(
    graph: Graph,
    schema_view: SchemaView,
    prefix_map: dict[str, str],
    node: dict[str, Any],
    depth: int,
    config: ConversionConfig,
    parent: URIRef | None = None,
    parent_predicate: URIRef | None = None,
    class_override: str | None = None,
) -> URIRef:
    node_id = node.get("id")
    if not node_id:
        raise ValueError("Each node must include an 'id' field")
    normalized_id = normalize_instance_id(prefix_map, node_id, config)
    subject = curie_to_uri(prefix_map, normalized_id)

    class_name = resolve_class_name(node, depth, config, class_override=class_override)
    graph.add((subject, RDF.type, class_uri(schema_view, prefix_map, class_name)))

    if schema_view.get_slot("id") is not None:
        add_literal(graph, subject, slot_predicate(schema_view, prefix_map, "id"), node_id)

    if parent is not None and parent_predicate is not None:
        graph.add((parent, parent_predicate, subject))
        if config.inject_is_part_of and schema_view.get_slot("isPartOf"):
            graph.add((subject, slot_predicate(schema_view, prefix_map, "isPartOf"), parent))

    for key, value in node.items():
        if key in {"id", "type", "@type", "class"}:
            continue
        if key == "hasPart":
            predicate = slot_predicate(schema_view, prefix_map, key)
            for child in iter_child_nodes(value):
                convert_node(
                    graph,
                    schema_view,
                    prefix_map,
                    child,
                    depth + 1,
                    config,
                    parent=subject,
                    parent_predicate=predicate,
                )
            continue
        if key == "isLocationOf":
            predicate = slot_predicate(schema_view, prefix_map, key)
            items = value if isinstance(value, list) else [value]
            for item in items:
                graph.add((subject, predicate, expand_uri(prefix_map, str(item))))
            continue

        predicate = slot_predicate(schema_view, prefix_map, key)
        if isinstance(value, dict):
            if slot_range_is_class(schema_view, key):
                class_name = slot_range(schema_view, key)
                convert_node(
                    graph,
                    schema_view,
                    prefix_map,
                    value,
                    depth + 1,
                    config,
                    parent=subject,
                    parent_predicate=predicate,
                    class_override=class_name,
                )
                continue
            raise ValueError(f"Slot '{key}' expects literal(s), got mapping")
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    if slot_range_is_class(schema_view, key):
                        class_name = slot_range(schema_view, key)
                        convert_node(
                            graph,
                            schema_view,
                            prefix_map,
                            item,
                            depth + 1,
                            config,
                            parent=subject,
                            parent_predicate=predicate,
                            class_override=class_name,
                        )
                        continue
                    raise ValueError(f"Slot '{key}' expects literal(s), got mapping")
                if slot_range_is_class(schema_view, key):
                    graph.add((subject, predicate, expand_uri(prefix_map, str(item))))
                elif slot_range_is_enum(schema_view, key) and isinstance(item, str):
                    add_literal(graph, subject, predicate, enum_literal(item))
                else:
                    add_literal(graph, subject, predicate, item)
        else:
            if slot_range_is_class(schema_view, key) and isinstance(value, str):
                graph.add((subject, predicate, expand_uri(prefix_map, value)))
            elif slot_range_is_enum(schema_view, key) and isinstance(value, str):
                add_literal(graph, subject, predicate, enum_literal(value))
            else:
                add_literal(graph, subject, predicate, value)

    return subject


def build_graph(
    schema_path: Path,
    data_path: Path,
    config: ConversionConfig,
) -> Graph:
    schema_view = SchemaView(str(schema_path))
    prefix_map = normalize_prefix_map(schema_view)
    prefix_map.setdefault(config.instance_prefix, config.instance_base)

    graph = Graph()
    for prefix, uri in prefix_map.items():
        graph.bind(prefix, Namespace(uri))

    data = load_yaml(data_path)
    convert_node(graph, schema_view, prefix_map, data, depth=0, config=config)
    return graph


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert LinkML YAML instance data into RDF/Turtle using the schema.",
    )
    parser.add_argument("schema", type=Path, help="Path to LinkML schema YAML.")
    parser.add_argument("input", type=Path, help="Path to instance YAML file.")
    parser.add_argument("output", type=Path, help="Path to output TTL file.")
    parser.add_argument(
        "--root-class",
        default="Site",
        help="Root class to use when instances omit explicit class/type.",
    )
    parser.add_argument(
        "--class-chain",
        default="Site,Building,Level,Room",
        help="Comma-separated class chain for nested hasPart entries.",
    )
    parser.add_argument(
        "--inject-is-part-of",
        action="store_true",
        help="Add inverse isPartOf triples for hasPart relationships.",
    )
    parser.add_argument(
        "--instance-prefix",
        default="ex",
        help="Prefix to use when instance ids omit an explicit prefix.",
    )
    parser.add_argument(
        "--instance-base",
        default="https://example.com/",
        help="Base URI for the instance prefix.",
    )
    parser.add_argument(
        "--shacl",
        type=Path,
        help="Optional SHACL shapes graph for validation.",
    )
    parser.add_argument(
        "--ontology",
        type=Path,
        help="Optional OWL ontology to load as inference graph.",
    )
    parser.add_argument(
        "--validation-report",
        type=Path,
        help="Write SHACL validation report TTL to this path.",
    )
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = parse_args()
    config = ConversionConfig(
        root_class=args.root_class,
        class_chain=[item.strip() for item in args.class_chain.split(",") if item.strip()],
        inject_is_part_of=args.inject_is_part_of,
        instance_prefix=args.instance_prefix,
        instance_base=args.instance_base,
    )
    if not config.class_chain:
        raise ValueError("class-chain must include at least one class name")

    graph = build_graph(args.schema, args.input, config)
    if args.shacl:
        shacl_graph = Graph().parse(args.shacl, format="turtle")
        ont_graph = None
        if args.ontology:
            ont_graph = Graph().parse(args.ontology, format="turtle")
        conforms, report_graph, report_text = validate(
            data_graph=graph,
            shacl_graph=shacl_graph,
            ont_graph=ont_graph,
            inference="rdfs",
            debug=False,
        )
        if args.validation_report:
            args.validation_report.parent.mkdir(parents=True, exist_ok=True)
            report_graph.serialize(destination=str(args.validation_report), format="turtle")
        if not conforms:
            raise ValueError(f"SHACL validation failed:\n{report_text}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    graph.serialize(destination=str(args.output), format="turtle")
    LOGGER.info("Wrote RDF Turtle to %s", args.output)


if __name__ == "__main__":
    main()
