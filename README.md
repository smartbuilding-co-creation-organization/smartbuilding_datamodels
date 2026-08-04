# Smart Building Ontology (LinkML)

LinkMLでスマートビル向けモデル（オントロジー）を管理し、以下を自動生成・公開するプロジェクトです。
このプロジェクトは、スマートビルディング共創機構の標準策定WGで仕様検討しているデータモデルです。

- OWL (Turtle): `output/building_model.owl.ttl` (from `schema/building_model_owl.yaml`)
- SHACL (Turtle): `output/building_model.shacl.ttl` (from `schema/building_model_shacl.yaml`)
- JSON Schema: `output/building_model.schema.json` (from `schema/building_model_shacl.yaml`)
- Docs (MkDocs + GitHub Pages)

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export PYTHONHASHSEED=0

# Generate artifacts
linkml generate owl --metadata-profile rdfs schema/building_model_owl.yaml -f ttl > output/building_model.owl.ttl
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
  --schema schema/building_model_shacl.yaml \
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
- 主な階層・関連スロット: `hasPart`, `isPartOf`, `hasPoint`, `isPointOf`, `locatedIn`
- カーディナリティ: `multivalued`（複数可）、`required`（必須）、`inlined_as_list`（子要素をリストとしてインライン展開）で表現。
- `hasPart` / `isPartOf` は Site・Building・Level・Room・Zone・OutdoorSpace・Space 間の階層関係を表現します。
- `id` は文字列、`maintenanceInterval` は独自の `DurationString` 型で定義します。`DurationString` は `xsd:duration` にマップされます。

**English recap**
- Schema sources: use `schema/building_model_shacl.yaml` for SHACL/JSON Schema/Docs and `schema/building_model_owl.yaml` for OWL.
- Core hierarchy: `Site` → `Building` → `Level` → `Space` with embedded `Equipment` and `Point`.
- Key relationship slots: `hasPart`, `isPartOf`, `hasPoint`, `isPointOf`, and `locatedIn`.
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

ex:site_001 a sbco:Site ;
  sbco:name "Marunouchi HQ" ;
  sbco:hasPart ex:building_A .

ex:building_A a sbco:Building ;
  sbco:name "Tower A" ;
  sbco:isPartOf ex:site_001 ;
  sbco:hasPart ex:level_A-3F .

ex:level_A-3F a sbco:Level ;
  sbco:name "3F" ;
  sbco:levelNumber 3 ;
  sbco:isPartOf ex:building_A ;
  sbco:hasPart ex:space_A-3F-Office .

ex:space_A-3F-Office a sbco:Space ;
  sbco:name "Office Area" ;
  sbco:isPartOf ex:level_A-3F ;
  sbco:hasPart ex:equip_AHU-01 .

ex:equip_AHU-01 a sbco:EquipmentExt ;
  sbco:id "equip/AHU-01" ;
  sbco:name "AHU-01" ;
  sbco:identifiers [ sbco:key "serial" ; sbco:value "AHU-01-XYZ" ] ;
  sbco:deviceType "AHU" ;
  sbco:panel "Panel-1" ;
  sbco:installationArea "Office Area" ;
  sbco:targetArea "Office Area" ;
  sbco:locatedIn ex:space_A-3F-Office ;
  sbco:hasPoint ex:point_AHU-01-SAT, ex:point_AHU-01-SF-CMD .

ex:point_AHU-01-SAT a sbco:PointExt ;
  sbco:id "point/AHU-01-SAT" ;
  sbco:name "Supply Air Temperature" ;
  sbco:identifiers [ sbco:key "BACnet" ; sbco:value "1234" ] ;
  sbco:pointType "TemperatureSensor" ;
  sbco:pointSpecification <https://www.sbco.or.jp/ont/PointSpecificationEnum#Measurement> ;
  sbco:unit <https://www.sbco.or.jp/ont/UnitEnum#celsius> ;
  sbco:isPointOf ex:equip_AHU-01 ;
  sbco:hasQuantity <https://www.sbco.or.jp/ont/QuantityEnum#Temperature> .

ex:point_AHU-01-SF-CMD a sbco:PointExt ;
  sbco:id "point/AHU-01-SF-CMD" ;
  sbco:name "Supply Fan Command" ;
  sbco:identifiers [ sbco:key "BACnet" ; sbco:value "5678" ] ;
  sbco:pointType "Command" ;
  sbco:pointSpecification <https://www.sbco.or.jp/ont/PointSpecificationEnum#Command> ;
  sbco:unit <https://www.sbco.or.jp/ont/UnitEnum#percent> ;
  sbco:isPointOf ex:equip_AHU-01 ;
  sbco:hasQuantity <https://www.sbco.or.jp/ont/QuantityEnum#Active_Power> .
```

## 参考

- LinkML: https://linkml.io
- MkDocs: https://www.mkdocs.org/
- mkdocs-material: https://squidfunk.github.io/mkdocs-material/

## ライセンス

- オントロジー、スキーマ、生成物、サンプル、ドキュメント:
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- スクリプト、ビルド設定、CI設定:
  [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

適用範囲と第三者プロジェクトに関する表示は、[LICENSE](LICENSE) と
[NOTICE.md](NOTICE.md) を参照してください。
