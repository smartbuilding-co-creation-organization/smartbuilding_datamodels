#!/usr/bin/env python3
"""Transform LinkML gen-doc Markdown (docs/) into pages that render correctly in the
smartbuilding_documents SPA (marked.js / CommonMark), and stage them for that repo's
docs/datamodels/ directory.

gen-doc wraps most page bodies in a `<div data-search-exclude markdown="1">` block that
relies on Python-Markdown's markdown="1" attribute (used by MkDocs) to keep processing
markdown inside raw HTML. marked.js follows CommonMark, where content inside a raw HTML
block is opaque, so that wrapper (plus the mkdocs-material search front matter, the
<details> collapsibles, and MkDocs-site-relative mermaid `click` hrefs) must be removed
before the files can be embedded in the SPA.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

FRONT_MATTER_RE = re.compile(r"\A---\nsearch:\n  boost: [\d.]+\n---\n*")
DIV_OPEN_RE = re.compile(r'<div data-search-exclude markdown="1">\n*')
DIV_CLOSE_RE = re.compile(r"\n*</div>\s*\Z")
DETAILS_OPEN_RE = re.compile(r"<details>\n?")
DETAILS_CLOSE_RE = re.compile(r"\n?</details>")
MERMAID_CLICK_RE = re.compile(r"^[ \t]*click \S+ href \"[^\"]*\"[ \t]*\n?", re.MULTILINE)

INDEX_FILENAME = "index.md"
GENERATED_BEGIN = "<!-- BEGIN:generated-schema-tables -->"
GENERATED_END = "<!-- END:generated-schema-tables -->"
GENERATED_BLOCK_RE = re.compile(
    re.escape(GENERATED_BEGIN) + r".*?" + re.escape(GENERATED_END), re.DOTALL
)

INDEX_SCAFFOLD = """# データモデル仕様

このページは、[smartbuilding_datamodels](\
https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels) \
リポジトリで管理されている LinkML スキーマから自動生成された、クラス・スロット・\
列挙型・型のリファレンスです。スキーマの更新に合わせて自動的に同期されます。

初めてこのページを訪れる方は、先に以下のナラティブなドキュメントで全体像を掴んでから\
読むことをおすすめします。

- [スマートビルとは](../getting_started.md) — スマートビル・ポイント・オントロジーの基礎概念
- [データフロー](../smart_building_data_flow.md) — ポイントリストからRDF/DTDLへ変換される流れ
- [用語集](../glossary.md) — BACnet・RDF/OWL・Brick・REC などの用語解説

以下は、スキーマに含まれる全クラス・スロット・列挙型・型の一覧です。名称をクリックすると、\
継承関係・プロパティ・mermaidクラス図・LinkMLソース定義などを含む詳細ページを確認できます。

{begin}
{generated}
{end}

## 関連ドキュメント

- OWL / SHACL / JSON Schema などの生成済み成果物は \
[smartbuilding_datamodels](https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels) \
で公開されています。
- スキーマの背景にある標準規格の調査は [オントロジー調査](../smart_building_ontology_survey.md) \
も参照してください。
""".format(begin=GENERATED_BEGIN, generated="{generated}", end=GENERATED_END)


def transform(text: str) -> str:
    text = FRONT_MATTER_RE.sub("", text, count=1)
    text = DIV_OPEN_RE.sub("", text, count=1)
    text = DIV_CLOSE_RE.sub("\n", text, count=1)
    text = DETAILS_OPEN_RE.sub("", text)
    text = DETAILS_CLOSE_RE.sub("", text)
    text = MERMAID_CLICK_RE.sub("", text)
    return text.strip() + "\n"


def extract_schema_tables(index_text: str) -> str:
    marker = "## Classes"
    if marker not in index_text:
        raise SystemExit(
            f"export_docs_for_documents: expected marker {marker!r} not found in "
            "docs/index.md — gen-doc's output format may have changed."
        )
    return index_text[index_text.index(marker):].strip()


def merge_index_page(generated_tables: str, existing_path: Path) -> str:
    if existing_path.exists():
        existing = existing_path.read_text(encoding="utf-8")
        if GENERATED_BLOCK_RE.search(existing):
            block = f"{GENERATED_BEGIN}\n{generated_tables}\n{GENERATED_END}"
            return GENERATED_BLOCK_RE.sub(lambda _m: block, existing, count=1)
    return INDEX_SCAFFOLD.format(generated=generated_tables)


def run(src: Path, out: Path) -> tuple[int, int]:
    out.mkdir(parents=True, exist_ok=True)
    source_files = sorted(src.glob("*.md"))
    if not source_files:
        raise SystemExit(f"No Markdown files found under {src}")

    written = 0
    for path in source_files:
        text = path.read_text(encoding="utf-8")
        if path.name == INDEX_FILENAME:
            transformed = transform(text)
            tables = extract_schema_tables(transformed)
            merged = merge_index_page(tables, out / INDEX_FILENAME)
            (out / INDEX_FILENAME).write_text(merged, encoding="utf-8")
        else:
            (out / path.name).write_text(transform(text), encoding="utf-8")
        written += 1
    return written, len(source_files)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transform LinkML gen-doc output for embedding in the "
        "smartbuilding_documents SPA.",
    )
    parser.add_argument(
        "--src",
        default=Path("docs"),
        type=Path,
        help="Directory containing the gen-doc Markdown output (default: docs).",
    )
    parser.add_argument(
        "--out",
        required=True,
        type=Path,
        help="Target docs/datamodels directory in the smartbuilding_documents checkout.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    written, total = run(args.src, args.out)
    print(f"Wrote {written}/{total} transformed docs to {args.out}")


if __name__ == "__main__":
    main()
