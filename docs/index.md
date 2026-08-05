# Smart Building Ontology (LinkML)

スマートビルディング共創機構（SBCO）が策定する、建物・設備・ポイントのための
LinkMLベースのデータモデルです。スキーマから OWL・SHACL・JSON Schema を自動生成し、
ナラティブな解説とあわせて公開しています。

[ガイドを読む](guide/getting_started.md){ .md-button .md-button--primary }
[スキーマリファレンスを見る](reference/index.md){ .md-button }

## このサイトについて

| セクション | 内容 |
| --- | --- |
| **[ガイド](guide/getting_started.md)** | スマートビルとは何か、データがどう流れるか、標準ポイントリストの仕様など、初学者向けのナラティブな解説 |
| **[スキーマリファレンス](reference/index.md)** | LinkMLスキーマから自動生成された、全クラス・スロット・列挙型・型の技術リファレンス |

## 生成される成果物

- OWL (Turtle): [`output/building_model.owl.ttl`](https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels/blob/main/output/building_model.owl.ttl)
- SHACL (Turtle): [`output/building_model.shacl.ttl`](https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels/blob/main/output/building_model.shacl.ttl)
- JSON Schema: [`output/building_model.schema.json`](https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels/blob/main/output/building_model.schema.json)

いずれもスキーマの更新に合わせて自動生成・公開されます。

## リンク

- [GitHubリポジトリ](https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels)
