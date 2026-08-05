#!/usr/bin/env python3
"""Registers the synced smartbuilding_documents narrative docs (docs/guide/*.md,
produced by smartbuilding_documents's tools/export_docs_for_datamodels.js) into
this repo's mkdocs.yml nav, under the "ガイド" section's marker-delimited block.

Run after the transform step has written docs/guide/*.md.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

BEGIN = "# BEGIN documents-guide-generated"
END = "# END documents-guide-generated"
GUIDE_BLOCK_RE = re.compile(re.escape(BEGIN) + r"[\s\S]*?" + re.escape(END))

# Display titles for known filenames; falls back to the filename stem for
# anything not listed here (e.g. a new doc added on the documents side).
TITLES = {
    "getting_started.md": "スマートビルとは",
    "walkthrough.md": "ウォークスルー",
    "learning_roadmap.md": "学習ロードマップ",
    "glossary.md": "用語集",
    "smart_building_data_flow.md": "データフロー",
    "pointlist.md": "ポイントリスト定義",
    "pointlist_sample.md": "ポイントリスト サンプル",
    "smart_building_ontology_survey.md": "オントロジー調査",
}

# Reading order matching smartbuilding_documents's own information architecture
# (入門 → 仕様 → 調査). Anything not listed here (e.g. a new doc added later)
# sorts alphabetically after these.
READING_ORDER = list(TITLES.keys())


def list_guide_docs(guide_dir: Path) -> list[str]:
    files = [p.name for p in guide_dir.glob("*.md")]
    if not files:
        raise SystemExit(f"No .md files found in {guide_dir}")

    def sort_key(name: str) -> tuple[int, str]:
        if name in READING_ORDER:
            return (READING_ORDER.index(name), name)
        return (len(READING_ORDER), name)

    return sorted(files, key=sort_key)


def update_mkdocs_yml(mkdocs_path: Path, files: list[str]) -> None:
    lines = [f"    - {TITLES.get(name, Path(name).stem)}: guide/{name}" for name in files]
    content = mkdocs_path.read_text(encoding="utf-8")
    if not GUIDE_BLOCK_RE.search(content):
        raise SystemExit(
            f"{mkdocs_path}: markers {BEGIN!r} / {END!r} not found — add the scaffold first"
        )
    block = f"{BEGIN}\n" + "\n".join(lines) + f"\n{END}"
    updated = GUIDE_BLOCK_RE.sub(lambda _m: block, content, count=1)
    mkdocs_path.write_text(updated, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--guide-dir", default=Path("docs/guide"), type=Path,
        help="Directory containing the synced narrative docs (default: docs/guide).",
    )
    parser.add_argument(
        "--mkdocs", default=Path("mkdocs.yml"), type=Path,
        help="Path to mkdocs.yml (default: mkdocs.yml).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    files = list_guide_docs(args.guide_dir)
    update_mkdocs_yml(args.mkdocs, files)
    print(f"Registered {len(files)} guide docs in {args.mkdocs}")


if __name__ == "__main__":
    main()
