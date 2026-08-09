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

It also removes any global ``rdfs:range`` that survives on the slots listed
in ``_MULTI_RANGE_SLOTS`` (``hasPoint``, ``isPointOf``) as a defensive
backstop. Those two slots are constrained per-class via a
``slot_usage.any_of`` override at every usage site — the schema
deliberately declares no base ``range:`` for them (see the comments next to
``hasPoint``/``isPointOf`` in ``schema/building_model_owl.yaml``), because a
declared base range gets ANDed into the generated ``owl:allValuesFrom`` as
an ``owl:intersectionOf`` alongside the ``any_of`` union, collapsing it back
down to the (narrower) base range. That collapse is actively unsound once
the property also gains an ``owl:equivalentProperty`` to an external
(rec:/brick:) predicate: RDFS range entailment (``rdfs2``) doesn't
validate, it only asserts — so a value of the *wrong* type (e.g. an
``EquipmentExt`` used as a ``hasPoint`` target) silently gets an extra,
incorrect ``sbco:Point`` type instead of being caught, defeating the SHACL
``sh:class``/``sh:or`` checks that exist specifically to catch that
mistake. If a future schema change reintroduces a base range for one of
these slots (or adds a new ``any_of`` override elsewhere), this backstop
removes the resulting global range rather than letting the bug resurface
silently.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from rdflib import Graph, Namespace, OWL, RDF, RDFS, URIRef

SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
SBCO = Namespace("https://www.sbco.or.jp/ont/")

_PROPERTY_TYPES = (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)

# Slots with a slot_usage.any_of range override in schema/building_model_owl.yaml.
_MULTI_RANGE_SLOTS = ("hasPoint", "isPointOf")


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


def drop_multi_range_global_ranges(graph: Graph) -> int:
    removed = 0
    for slot_name in _MULTI_RANGE_SLOTS:
        subject = SBCO[slot_name]
        for triple in list(graph.triples((subject, RDFS.range, None))):
            graph.remove(triple)
            removed += 1
    return removed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("owl_ttl", type=Path, help="Path to the generated OWL Turtle file (edited in place).")
    args = parser.parse_args()

    graph = Graph()
    graph.parse(args.owl_ttl, format="turtle")
    added = add_equivalence_axioms(graph)
    removed = drop_multi_range_global_ranges(graph)
    graph.serialize(destination=str(args.owl_ttl), format="turtle")
    print(
        f"postprocess_owl: added {added} owl:equivalentClass/equivalentProperty axioms, "
        f"removed {removed} redundant global rdfs:range triples in {args.owl_ttl}"
    )


if __name__ == "__main__":
    main()
