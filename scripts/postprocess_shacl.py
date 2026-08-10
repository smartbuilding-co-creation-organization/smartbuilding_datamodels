#!/usr/bin/env python3
"""Downgrade specific SHACL constraints from blocking (sh:Violation, the SHACL
default) to advisory (sh:Warning), for constraints whose vocabulary is still
provisional rather than agreed.

sh:Warning results still appear in the validation report (so tooling can
surface them), but do not affect pyshacl's `conforms` — a warning-only
mismatch no longer fails an otherwise-valid import. See WARNING_SEVERITY_PATHS
below for what is currently downgraded and why.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import SH

SBCO = Namespace("https://www.sbco.or.jp/ont/")

# sbco:unit's UnitEnum vocabulary is still under discussion with the SBCO/GUTP
# working group (README "sbco:unit 語彙と正規化", #35/#36) -- until it settles,
# an out-of-vocabulary unit should be visible to tooling but must not block an
# otherwise-valid import.
WARNING_SEVERITY_PATHS: list[URIRef] = [SBCO.unit]


def downgrade_to_warning(graph: Graph, paths: list[URIRef]) -> int:
    changed = 0
    for path in paths:
        for shape in graph.subjects(SH.path, path):
            if (shape, SH.severity, None) in graph:
                continue
            graph.add((shape, SH.severity, SH.Warning))
            changed += 1
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("shacl_ttl", type=Path, help="Path to the generated SHACL Turtle file (edited in place).")
    args = parser.parse_args()
    graph = Graph()
    graph.parse(args.shacl_ttl, format="turtle")
    changed = downgrade_to_warning(graph, WARNING_SEVERITY_PATHS)
    graph.serialize(destination=str(args.shacl_ttl), format="turtle")
    print(f"postprocess_shacl: downgraded {changed} property shape(s) to sh:Warning severity in {args.shacl_ttl}")


if __name__ == "__main__":
    main()
