#!/usr/bin/env python3
"""Check that committed RDF Turtle outputs match a freshly regenerated copy.

A plain ``git diff --exit-code`` does not work for ``output/*.ttl``: the
Turtle serializer's blank-node ordering is not stable across runs (verified
empirically — regenerating ``output/building_model.shacl.ttl`` twice in a
row from an unchanged schema produces two byte-different files), so a
naive text diff is flaky and would fail CI even when nothing semantically
changed. This script instead parses both the on-disk (freshly regenerated)
and the git-committed (``HEAD``) version of each file and compares them
with RDF graph isomorphism, which is invariant to blank-node
relabeling/reordering and only fails on a real content difference.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from rdflib import Graph
from rdflib.compare import to_isomorphic


def committed_graph(path: Path) -> Graph:
    result = subprocess.run(
        ["git", "show", f"HEAD:{path.as_posix()}"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    graph = Graph()
    graph.parse(data=result.stdout, format="turtle")
    return graph


def on_disk_graph(path: Path) -> Graph:
    graph = Graph()
    graph.parse(path, format="turtle")
    return graph


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Turtle files to check for drift against HEAD.")
    args = parser.parse_args()

    drifted: list[Path] = []
    for path in args.paths:
        committed = to_isomorphic(committed_graph(path))
        current = to_isomorphic(on_disk_graph(path))
        if committed == current:
            print(f"OK: {path} matches the committed version (regeneration is a no-op).")
        else:
            drifted.append(path)
            print(f"DRIFT: {path} differs from the committed version — regenerate and commit it.")

    if drifted:
        sys.exit(f"check_ttl_drift: {len(drifted)} file(s) out of date: {', '.join(str(p) for p in drifted)}")


if __name__ == "__main__":
    main()
