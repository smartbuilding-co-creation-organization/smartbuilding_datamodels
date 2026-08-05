# 学習ロードマップ

初学者からエキスパートまで、読者の目的に応じた推奨学習順序を示します。

---

## 読者タイプ別ガイド

### A. スマートビルを初めて学ぶ方

前提知識なし。まず全体像を把握したい方向け。

1. **[getting_started.md](getting_started.md)** — スマートビルとポイント・オントロジーの基礎概念
2. **[walkthrough.md](walkthrough.md)** — 温度センサー1点の登録をStep-by-Stepで体験
3. **[smart_building_data_flow.md](smart_building_data_flow.md)** — データ生成フローの全体把握
4. **[glossary.md](glossary.md)** — 疑問に思った用語をいつでも参照

---

### B. ポイントリスト作成担当者（設備・BMS担当者）

建物の設備情報をポイントリストに起こす作業を担当する方向け。

1. **[getting_started.md](getting_started.md)** — 特にセクション2〜3（ポイント・ポイントリストの概念）を重点的に
2. **[pointlist_sample.md](pointlist_sample.md)** — 記入例と各フィールドの読み方
3. **[pointlist.md](pointlist.md)** — 全フィールド仕様の精読（値定義・データ制約）
4. **[smartbuilding_datamodel_builder](https://smartbuilding-co-creation-organization.github.io/smartbuilding_datamodel_builder/)** — WebアプリでサンプルCSVを試す（[GitHub](https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodel_builder)）

---

### C. データモデル・オントロジー開発者

PoC実装や標準拡張など、コード・スキーマレベルで関わる方向け。

1. **[getting_started.md](getting_started.md)** — セクション4〜5（データモデル・ツール概要）
2. **[walkthrough.md](walkthrough.md)** — CSV → RDF の変換例を確認
3. **[smart_building_ontology_survey.md](smart_building_ontology_survey.md)** — オントロジー体系を精読
4. **smartbuilding_datamodels** — `schema/building_model_shacl.yaml` と `output/` を確認（[GitHub](https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels)）

---

### D. 研究者・標準化担当者

国際標準との関係や理論的背景を深く理解したい方向け。

1. **[smart_building_ontology_survey.md](smart_building_ontology_survey.md)** — 全体精読（技術・標準規格）
2. **2026-05 業界・市場動向レポート** — 業界・市場動向（特にSection 12：標準化、Section 15：グローバルvs日本）
3. **smartbuilding_datamodels** — OWL / SHACL 出力を精読（`output/building_model.owl.ttl`）
4. 参考論文：Pauwels & Fierro (2022)、IEA Annex 81 最終報告書 (2025)（文献リストは各調査文書末尾）

---

## ドキュメント依存関係

```
getting_started（概念入門）
    │
    ├──→ walkthrough（実例）──→ pointlist_sample（サンプル詳解）
    │           │
    │           └──→ pointlist（フィールド仕様）
    │                       │
    │                       └──→ smartbuilding_datamodel_builder（CSV編集ツール）
    │
    ├──→ smart_building_data_flow（フロー把握）
    │
    └──→ smart_building_ontology_survey（オントロジー技術）
    │               │
    │               └──→ smartbuilding_datamodels（オントロジー実装）
    │
    └──→ reports/（業界・市場動向レポート）
```

---

## 学習チェックリスト

以下がすべてできれば、本プロジェクトへの参加・貢献が可能なレベルです。

### 基礎レベル

- [ ] 「ポイント」とは何かを人に説明できる
- [ ] gateway → 設備 → ポイント のデータフローを図に描ける
- [ ] ポイントリストのサンプル行を読んで各フィールドの意味がわかる

### 中級レベル

- [ ] builder WebアプリでサンプルCSVを読み込み、ツリーを確認できる
- [ ] バリデーションエラーを見つけて修正できる
- [ ] RDF Turtle 形式で `Site > Building > Equipment > Point` の階層を記述できる

### 上級レベル

- [ ] オントロジーとスキーマの違いを説明できる
- [ ] `smartbuilding_datamodels` の LinkML YAML を読んでクラス定義を理解できる
- [ ] 新しいデバイス種別のテンプレートを提案・定義できる
