# スマートビル・オントロジー入門ガイド

> 初めてスマートビルや建物データ標準を学ぶ方のための入門ドキュメントです。  
> 事前知識は不要です。まずはこのドキュメントを通読してください。

---

## 1. スマートビルとは

スマートビルとは、温度・湿度・照度・消費電力など**多数のセンサーからのデータをリアルタイムに収集・活用し、快適性・省エネ・安全性を向上させる建物**のことです。

典型的なスマートビルでは以下のようなことが実現されます：

- 各部屋の温度・CO2濃度・在室状況を自動モニタリング
- 在室者がいない会議室の空調・照明を自動オフ
- 設備の異常をデータから事前に検知（予防保全）
- エネルギー使用量の見える化と最適制御

これらを実現するためには、**多数の機器・センサーからのデータを統一的に扱うための仕組み**が必要です。それが本プロジェクトが扱う「ポイントリスト」「データモデル」「オントロジー」です。

---

## 2. 「ポイント」とは

スマートビルの世界では、設備やセンサーが発するひとつひとつのデータを**「ポイント（Point）」**と呼びます。

| 区分 | 英語名 | 説明 | 例 |
|------|--------|------|----|
| 計測 | Measurement | センサーが測定した値（読み取り専用） | 室温: 24.5℃ |
| 計量 | Metering | 累積値の計測 | 電力量: 1,234 kWh |
| 状態 | Status | 機器の稼働状態（読み取り専用） | ポンプ: 運転中 |
| 設定 | Setpoint | 目標値の設定 | 設定温度: 26℃ |
| 制御 | Command | 機器への指令（書き込み可能） | エアコン: オン |
| 警報 | Alarm | 異常・アラームの通知 | 高温警報: 発生 |

一般的なビルには数百〜数千のポイントが存在します。これらすべてを管理するために作成するのが「ポイントリスト」です。

---

## 3. ポイントリストとは

**ポイントリストとは、建物内にあるすべてのポイントを一覧化した「カタログ」**です。CSV形式で作成され、各ポイントについて以下の情報を記録します。

```
どの建物・部屋に ──→ site / building / floor / installation_area
どの機器が      ──→ device_id / device_name / device_type
どんな値を      ──→ point_type / unit / max_pres_value / min_pres_value
どう提供するか  ──→ point_specification / writable / interval
どのゲートウェイ経由で ──→ gateway_id / local_id
```

詳細なフィールド定義は [pointlist.md](pointlist.md) を、記入例は [pointlist_sample.md](pointlist_sample.md) を参照してください。

### ゲートウェイとは

ビル内に設置されたセンサーや設備機器（BACnet対応空調機など）は、直接インターネットにつながっていません。**ゲートウェイ（Gateway）**は、これらの機器とビルOSクラウドをつなぐ中継装置です。

```
[温度センサー] ─── BACnet ───→ [ゲートウェイ GW001] ─── インターネット ───→ [ビルOS クラウド]
```

### BACnetとは

**BACnet（Building Automation and Control Networks）**は、空調・照明・防災設備などの建物設備を制御・監視するために広く使われている通信プロトコル（ASHRAE規格）です。ビル内の多くの機器がBACnetで通信しているため、ポイントリストにはBACnet固有のフィールド（`device_id_bacnet`、`object_type_bacnet`など）が含まれています。

---

## 4. データモデル・オントロジーとは

CSV形式のポイントリストは人間には読みやすいですが、コンピュータには「温度センサー」と「温度計」が同じものなのか、「3F」と「3階」が同じ場所なのかを判断できません。

**データモデル**とは、機器・空間・ポイント間の**関係と意味を機械が理解できる形式で定義したもの**です。

**オントロジー（Ontology）**とは、「建物とはどんな概念か」「設備と空間はどう関係するか」を**辞書＋文法のように形式的に定義した知識体系**です。

| 比喩 | 実際の役割 |
|------|-----------|
| 語彙（辞書） | `Building`（建物）`Equipment`（設備）`Point`（ポイント）の定義 |
| 文法（関係） | 「建物はフロアを持つ」「設備はポイントを持つ」というルール |
| 推論 | CO2センサーはセンサーの一種 → センサーは計測ポイントを持つはず、と推論できる |

本プロジェクトでは、国際標準の **[Brick Schema](https://brickschema.org/)** と **[RealEstateCore (REC)](https://www.realestatecore.io/)** を基礎として、スマートビルディング共創機構（SBCO）独自の拡張クラス（`EquipmentExt`、`PointExt`）を定義しています。

---

## 5. ツール全体像：3つのリポジトリの連携

本プロジェクトは以下の3つのリポジトリで構成されています。

```
smartbuilding_documents/        ← このリポジトリ（仕様文書・入門ガイド）
smartbuilding_datamodel_builder/ ← CSVエディタ＆バリデータ（Webアプリ）
smartbuilding_datamodels/       ← オントロジー定義 + RDF/JSON Schema 生成
```

### データフロー

```
① ポイントリスト作成
   pointlist.md のフォーマットに従ってCSVを手作成、またはBMSから出力
         ↓
② builder Webアプリでインポート・検証・編集
   ブラウザ上でツリー表示を確認し、バリデーションエラーを修正
         ↓
③ RDF / JSON-LD / YAML などにエクスポート
         ↓
④ ビルOSプラットフォームへ投入
   datamodels のオントロジーに基づいて意味付けされたデータとして管理
         ↓
⑤ デジタルツイン構築・アプリ活用
   モニタリング・遠隔制御・AI分析・エネルギー最適化
```

### smartbuilding_datamodel_builder（CSVエディタ）

ポイントリストCSVをブラウザ上で読み込み、編集・バリデーション・エクスポートができるWebアプリです。

🔧 **[デモを試す（GitHub Pages）](https://smartbuilding-co-creation-organization.github.io/smartbuilding_datamodel_builder/)** ・
[ソースコード](https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodel_builder)

- `pnpm install && pnpm dev` でローカル起動（ポート 5173）
- サンプルCSVを読み込むと `Site → Building → Floor → Room → Device → Point` の階層ツリーが表示される
- 必須フィールド欠落・参照エラーなどを自動検出
- CSV / JSON / RDF(Turtle) / YAML / JSON-LD でエクスポート可能

### smartbuilding_datamodels（オントロジー定義）

[LinkML](https://linkml.io/) という仕様記述言語で書かれたオントロジーから、OWL・SHACL・JSON Schema を自動生成するリポジトリです。

- `schema/building_model_shacl.yaml` がメインの定義ファイル
- `output/` 以下に生成済みの RDF/Turtle・SHACL・JSON Schema が含まれる
- GitHub Actions により push のたびに自動生成・ドキュメント更新

---

*次のステップ：*
- *[ウォークスルー](walkthrough.md) — 温度センサー1点をStep-by-Stepで登録する実例*
- *[学習ロードマップ](learning_roadmap.md) — 自分の目的に合った学習順序を確認する*
- *[用語集](glossary.md) — 用語をいつでも引ける独立リファレンス*
