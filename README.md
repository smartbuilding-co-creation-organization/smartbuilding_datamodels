# Smart Building Ontology (LinkML)

LinkMLでスマートビル向けモデル（オントロジー）を管理し、以下を自動生成・公開するプロジェクトです。
このプロジェクトは、スマートビルディング共創機構の標準策定WGで仕様検討しているデータモデルです。

📖 **公開ドキュメント:** [Smart Building Ontology](https://smartbuilding-co-creation-organization.github.io/smartbuilding_datamodels/)

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
gen-doc --directory docs/reference --template-directory templates/docgen schema/building_model_shacl.yaml
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
  - GitHub Pages へデプロイ
  を自動実行します。

## スキーマ概要と編集ポイント

- スキーマ分割: `schema/building_model_shacl.yaml`（SHACL/JSON Schema/Docs）と `schema/building_model_owl.yaml`（OWL）
- トップレベルの階層: `Site` → `Building` → `Level` → `Space`
- 設備とポイント: `Equipment` が設備本体、`Point` が計測・制御・状態などのポイント。
- 主な階層・関連スロット: `hasPart`, `isPartOf`, `hasPoint`, `isPointOf`, `locatedIn`
- カーディナリティ: `multivalued`（複数可）、`required`（必須）、`inlined_as_list`（子要素をリストとしてインライン展開）で表現。
- `hasPart` / `isPartOf` は Site・Building・Level・Room・Zone・OutdoorSpace・Space 間の階層関係を表現します。
- `id` は文字列、`maintenanceInterval` は独自の `DurationString` 型で定義します。`DurationString` は `xsd:duration` にマップされます。
- **語彙方針**: 建物階層（Site/Building/Level/Room 等）と汎用スロット（`hasPart`, `isPartOf`, `locatedIn`, `name`, `hasPoint` など）は
  RealEstateCore（`rec:`）/ Brick（`brick:`）を正規語彙として使用します。`sbco:` は `EquipmentExt` / `PointExt` と、
  それらに固有のフィールド（`gatewayId`, `pointType`, `writable` など）にのみ使う拡張名前空間です。
  各クラス・スロットの `sbco:` 別名と正規語彙の対応は `owl:equivalentClass` / `owl:equivalentProperty` として
  `output/building_model.owl.ttl` に生成されます（`scripts/postprocess_owl.py` 参照）。

**English recap**
- Schema sources: use `schema/building_model_shacl.yaml` for SHACL/JSON Schema/Docs and `schema/building_model_owl.yaml` for OWL.
- Core hierarchy: `Site` → `Building` → `Level` → `Space` with embedded `Equipment` and `Point`.
- Key relationship slots: `hasPart`, `isPartOf`, `hasPoint`, `isPointOf`, and `locatedIn`.
- Cardinality controls: `multivalued`, `required`, and `inlined_as_list` indicate multiplicity, requiredness, and inline list expansion.
- **Vocabulary policy**: the building hierarchy (Site/Building/Level/Room, …) and generic slots (`hasPart`, `isPartOf`,
  `locatedIn`, `name`, `hasPoint`, …) use RealEstateCore (`rec:`) / Brick (`brick:`) as the canonical vocabulary. `sbco:` is
  reserved for `EquipmentExt` / `PointExt` and their SBCO-specific fields (`gatewayId`, `pointType`, `writable`, …). Each
  `sbco:` alias is linked to its canonical term via `owl:equivalentClass`/`owl:equivalentProperty` in the generated
  `output/building_model.owl.ttl` (see `scripts/postprocess_owl.py`).

## サンプルデータモデル（RDF/Turtle）

LinkML スキーマから生成された OWL / SHACL の正規語彙に合わせ、建物階層は RealEstateCore/Brick（`rec:hasPart`, `rec:isPartOf`,
`rec:locatedIn`, `rec:hasPoint`, `brick:isPointOf`, `brick:hasQuantity` など）、SBCO 固有拡張（`EquipmentExt`/`PointExt` と
そのフィールド）は `sbco:` を使って階層構造を示した例です。Site → Building → Level → Space → Equipment → Point の接続関係を、
`output/building_model.owl.ttl` / `output/building_model.shacl.ttl` の語彙に準拠して RDF/Turtle で表しています。

**English explanation**
This Turtle example follows the OWL/SHACL vocabulary generated from the LinkML schema. The building hierarchy uses the
canonical RealEstateCore/Brick terms (`rec:hasPart`, `rec:isPartOf`, `rec:locatedIn`, `rec:hasPoint`, `brick:isPointOf`,
`brick:hasQuantity`, …), while `sbco:` is used only for the SBCO-specific `EquipmentExt`/`PointExt` extensions and their
fields, to show the Site → Building → Level → Space → Equipment → Point hierarchy. Points reference quantities and units
via the enumerations defined in the generated artifacts.

```turtle
@prefix rec:  <https://w3id.org/rec/> .
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix sbco: <https://www.sbco.or.jp/ont/> .
@prefix ex:   <https://example.com/> .

ex:site_001 a rec:Site ;
  rec:name "Marunouchi HQ" ;
  rec:hasPart ex:building_A .

ex:building_A a rec:Building ;
  rec:name "Tower A" ;
  rec:isPartOf ex:site_001 ;
  rec:hasPart ex:level_A-3F .

ex:level_A-3F a rec:Level ;
  rec:name "3F" ;
  rec:levelNumber 3 ;
  rec:isPartOf ex:building_A ;
  rec:hasPart ex:space_A-3F-Office .

ex:space_A-3F-Office a rec:Space ;
  rec:name "Office Area" ;
  rec:isPartOf ex:level_A-3F ;
  rec:hasPart ex:equip_AHU-01 .

ex:equip_AHU-01 a sbco:EquipmentExt ;
  sbco:id "equip/AHU-01" ;
  rec:name "AHU-01" ;
  rec:identifiers [ sbco:key "serial" ; sbco:value "AHU-01-XYZ" ] ;
  sbco:deviceType "AHU" ;
  sbco:panel "Panel-1" ;
  sbco:installationArea "Office Area" ;
  sbco:targetArea "Office Area" ;
  rec:locatedIn ex:space_A-3F-Office ;
  rec:hasPoint ex:point_AHU-01-SAT, ex:point_AHU-01-SF-CMD .

ex:point_AHU-01-SAT a sbco:PointExt ;
  sbco:id "point/AHU-01-SAT" ;
  rec:name "Supply Air Temperature" ;
  rec:identifiers [ sbco:key "BACnet" ; sbco:value "1234" ] ;
  sbco:pointType "TemperatureSensor" ;
  sbco:pointSpecification "Measurement" ;
  sbco:unit "celsius" ;
  brick:isPointOf ex:equip_AHU-01 ;
  brick:hasQuantity "Temperature" .

ex:point_AHU-01-SF-CMD a sbco:PointExt ;
  sbco:id "point/AHU-01-SF-CMD" ;
  rec:name "Supply Fan Command" ;
  rec:identifiers [ sbco:key "BACnet" ; sbco:value "5678" ] ;
  sbco:pointType "Command" ;
  sbco:pointSpecification "Command" ;
  sbco:unit "percent" ;
  brick:isPointOf ex:equip_AHU-01 ;
  brick:hasQuantity "Active_Power" .
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
