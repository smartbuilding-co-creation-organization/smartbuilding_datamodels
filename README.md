# Smart Building Ontology (LinkML)

LinkMLでスマートビル向けモデル（オントロジー）を管理し、以下を自動生成・公開するテンプレートです。
このプロジェクトは、スマートビルディング共創機構の標準策定WGで仕様検討しているデータモデルです。

- OWL (Turtle): `output/building_model.owl.ttl` (from `schema/building_model_owl.yaml`)
- SHACL (Turtle): `output/building_model.shacl.ttl` (from `schema/building_model_shacl.yaml`)
- JSON Schema: `output/building_model.schema.json` (from `schema/building_model_shacl.yaml`)
- Docs (MkDocs + GitHub Pages)

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Generate artifacts
linkml generate owl --metadata-profile rdfs schema/building_model_owl.yaml -f ttl >  output/building_model.owl.ttl
linkml generate shacl --non-closed --suffix Shape schema/building_model_shacl.yaml > output/building_model.shacl.ttl
linkml generate json-schema schema/building_model_shacl.yaml > output/building_model.schema.json

# Generate docs and preview
gen-doc --directory docs schema/building_model_shacl.yaml
mkdocs serve
```

## RDF Validation (OWL Inference + SHACL)

`scripts/validate_rdf.py` runs the YAML→RDF conversion and validates the resulting RDF with
the generated OWL/SHACL artifacts. Validation cases live under `sample/validation/` and
can assert both SHACL conformance and expected inferred class types.

```bash
python scripts/validate_rdf.py \
  --schema schema/building_model.yaml \
  --ontology output/building_model.owl.ttl \
  --shacl output/building_model.shacl.ttl \
  --cases sample/validation/cases.yaml
```

## CI/CD

- GitHub Actions (`.github/workflows/ci.yml`) により、`main` への push で
  - 生成（OWL/SHACL/JSON Schema/Docs）
  - MkDocs build
  - GitHub Pages へデプロイ（`gh-pages`）
  を自動実行します。

## スキーマ概要と編集ポイント

- スキーマ分割: `schema/building_model_shacl.yaml`（SHACL/JSON Schema/Docs）と `schema/building_model_owl.yaml`（OWL）
- トップレベルの階層: `Site` → `Building` → `Level` → `Space`
- 設備とポイント: `Equipment` が設備本体、`Point` が計測・制御・状態などのポイント。
- 主なスロット: `buildings`, `levels`, `spaces`, `equipment_list`, `points`
- カードィナリティ: `multivalued`（複数可）、`required`（必須）、`inlined_as_list`（子要素をリストとしてインライン展開）で表現。
- `hasPart` / `isPartOf` は `Space` を range として扱います（Space→Space の階層関係を表現）。
- `id` と `maintenanceInterval` は独自の型（`IdString` / `DurationString`）で定義します。`DurationString` は `xsd:duration` にマップされます。

**English recap**
- Schema sources: use `schema/building_model_shacl.yaml` for SHACL/JSON Schema/Docs and `schema/building_model_owl.yaml` for OWL.
- Core hierarchy: `Site` → `Building` → `Level` → `Space` with embedded `Equipment` and `Point`.
- Key slots: `buildings`, `levels`, `spaces`, `equipment_list`, `points`.
- Cardinality controls: `multivalued`, `required`, and `inlined_as_list` indicate multiplicity, requiredness, and inline list expansion.

## サンプルデータモデル（RDF/Turtle）

LinkML スキーマから生成された OWL / SHACL に合わせ、実際のクラス URI とスロット URI（`sbco:hasPart`, `sbco:isPartOf`, `sbco:locatedIn`,
`sbco:hasPoint`, `sbco:isPointOf`, `sbco:hasQuantity`, `sbco:unit` など）を使って階層構造を示した例です。Site → Building → Level →
Space → Equipment → Point の接続関係を、`output/building_model.owl.ttl` / `output/building_model.shacl.ttl` の語彙に準拠して RDF/Turtle で表しています。

**English explanation**
This Turtle example follows the OWL/SHACL vocabulary generated from the LinkML schema. It uses the official `sbco` terms such as
`sbco:hasPart`, `sbco:isPartOf`, `sbco:locatedIn`, and `sbco:hasPoint` to show the Site → Building → Level → Space → Equipment →
Point hierarchy. Points reference quantities and units via the enumerations defined in the generated artifacts.

```turtle
@prefix sbco: <https://www.sbco.or.jp/ont/> .
@prefix ex:   <https://example.com/> .

ex:site/001 a sbco:Site ;
  sbco:name "Marunouchi HQ" ;
  sbco:hasPart ex:building/A .

ex:building/A a sbco:Building ;
  sbco:name "Tower A" ;
  sbco:isPartOf ex:site/001 ;
  sbco:hasPart ex:level/A-3F .

ex:level/A-3F a sbco:Level ;
  sbco:name "3F" ;
  sbco:levelNumber 3 ;
  sbco:isPartOf ex:building/A ;
  sbco:hasPart ex:space/A-3F-Office .

ex:space/A-3F-Office a sbco:Space ;
  sbco:name "Office Area" ;
  sbco:isPartOf ex:level/A-3F ;
  sbco:hasPart ex:equip/AHU-01 .

ex:equip/AHU-01 a sbco:EquipmentExt ;
  sbco:id "equip/AHU-01" ;
  sbco:name "AHU-01" ;
  sbco:identifiers [ sbco:key "serial" ; sbco:value "AHU-01-XYZ" ] ;
  sbco:deviceType "AHU" ;
  sbco:panel "Panel-1" ;
  sbco:installationArea "Office Area" ;
  sbco:targetArea "Office Area" ;
  sbco:locatedIn ex:space/A-3F-Office ;
  sbco:hasPoint ex:point/AHU-01-SAT, ex:point/AHU-01-SF-CMD .

ex:point/AHU-01-SAT a sbco:PointExt ;
  sbco:id "point/AHU-01-SAT" ;
  sbco:name "Supply Air Temperature" ;
  sbco:identifiers [ sbco:key "BACnet" ; sbco:value "1234" ] ;
  sbco:pointType "TemperatureSensor" ;
  sbco:pointSpecification <https://www.sbco.or.jp/ont/PointSpecificationEnum#Measurement> ;
  sbco:unit <https://www.sbco.or.jp/ont/UnitEnum#celsius> ;
  sbco:isPointOf ex:equip/AHU-01 ;
  sbco:hasQuantity <https://www.sbco.or.jp/ont/QuantityEnum#Temperature> .

ex:point/AHU-01-SF-CMD a sbco:PointExt ;
  sbco:id "point/AHU-01-SF-CMD" ;
  sbco:name "Supply Fan Command" ;
  sbco:identifiers [ sbco:key "BACnet" ; sbco:value "5678" ] ;
  sbco:pointType "Command" ;
  sbco:pointSpecification <https://www.sbco.or.jp/ont/PointSpecificationEnum#Command> ;
  sbco:unit <https://www.sbco.or.jp/ont/UnitEnum#percent> ;
  sbco:isPointOf ex:equip/AHU-01 ;
  sbco:hasQuantity <https://www.sbco.or.jp/ont/QuantityEnum#Active_Power> .
```

## 参考

- LinkML: https://linkml.io
- MkDocs: https://www.mkdocs.org/
- mkdocs-material: https://squidfunk.github.io/mkdocs-material/
