# ウォークスルー：温度センサー1点の旅

> **対象読者**: [getting_started.md](getting_started.md) でポイントリストとデータモデルの概念を理解した方  
> スマートビルにおけるデータの流れを、具体的な1つのセンサーを例に Step-by-Step で追います。

---

## シナリオ

東京の「TokyoSite1」ビル3F会議室101に設置された温度センサー（DEV001）の計測ポイント（PT001）を登録する。

---

## Step 1：物理的な設置

```
[温度センサー（BACnet接続）] ──→ [ゲートウェイ GW001]
                                          ↓ インターネット
                                    [ビルOS クラウド]
```

- センサーはゲートウェイ GW001 に BACnet で接続
- BACnet デバイス識別子: `BAC001`
- BACnet オブジェクト種別: `Analog-Input`（アナログ入力＝連続値の計測）
- BACnet インスタンス番号: `OBJ001`

---

## Step 2：ポイントリストへの記入

[pointlist.md](pointlist.md) のフィールド定義に従い、CSV の1行として記入します。

| フィールド | 値 | 意味 |
|-----------|-----|------|
| gateway_id | GW001 | データ収集ゲートウェイ名 |
| device_id | DEV001 | ビルOS上の機器ID（ビルOSが識別する） |
| device_name | 温度センサー01 | 機器の名称 |
| device_type | Sensor | 機器種別テンプレート |
| site | TokyoSite1 | サイト名 |
| building | MainBldg | 建物名 |
| floor | 3F | フロア |
| installation_area | 会議室101 | 設置エリア |
| point_id | PT001 | ポイントのビルOS内ユニークID |
| point_name | 室温センサー | ポイント名称 |
| point_type | 温度 | ポイント種別 |
| point_specification | Measurement | ポイント区分（計測） |
| writable | false | 読み取り専用（センサーなので書き込み不可） |
| interval | 60 | 60秒おきにビルOSへ送信 |
| unit | ℃ | 単位 |
| local_id | LOCAL001 | GW が現地機器を識別するための設備側識別子 |
| device_id_bacnet | BAC001 | BACnet デバイスID |
| object_type_bacnet | Analog-Input | BACnet オブジェクト種別 |
| instance_no_bacnet | OBJ001 | BACnet インスタンス番号 |

この1行が、ゲートウェイ・ビルOS・データモデル生成ツールのすべてが必要とする情報を含んでいます。

---

## Step 3：builder Webアプリでの処理

[smartbuilding_datamodel_builder](https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodel_builder) を `pnpm dev` で起動し、CSVをインポートします（[GitHub Pagesのデモ](https://smartbuilding-co-creation-organization.github.io/smartbuilding_datamodel_builder/)でも同じ操作を試せます）。

1. CSVをWebアプリにドラッグ＆ドロップ
2. 左パネルのツリーに `TokyoSite1 > MainBldg > 3F > 会議室101 > DEV001 > PT001` が表示される
3. `PT001` を選択すると右パネルに全フィールドが表示され、その場で編集も可能
4. バリデーションエラー（必須フィールド欠落など）がなければ「Export」から出力

---

## Step 4：RDF Turtle での表現

Turtle形式（RDFの人間可読なシリアライズ）では以下のように表現されます。

```turtle
@prefix sbco: <https://www.sbco.or.jp/ont/> .
@prefix ex:   <https://example.com/tokyosite1/> .

# 3Fの会議室101（空間レイヤ）
ex:room_3f_conf101 a sbco:Room ;
    sbco:id   "room_3f_conf101" ;
    sbco:name "会議室101" .

# 温度センサー DEV001（設備レイヤ）
ex:device_dev001 a sbco:EquipmentExt ;
    sbco:id         "DEV001" ;
    sbco:name       "温度センサー01" ;
    sbco:deviceType "Sensor" ;
    sbco:locatedIn  ex:room_3f_conf101 .

# 室温計測ポイント PT001（データポイントレイヤ）
ex:point_pt001 a sbco:PointExt ;
    sbco:id               "PT001" ;
    sbco:name             "室温センサー" ;
    sbco:pointSpecification <https://www.sbco.or.jp/ont/PointSpecificationEnum#Measurement> ;
    sbco:unit             <https://www.sbco.or.jp/ont/UnitEnum#celsius> ;
    sbco:isPointOf        ex:device_dev001 .
```

**CSV → Turtle の対応関係**

| CSV フィールド | Turtle での表現 |
|---|---|
| `device_id: DEV001` | `sbco:id "DEV001"` |
| `device_type: Sensor` | `sbco:deviceType "Sensor"` |
| `installation_area: 会議室101` | `sbco:locatedIn ex:room_3f_conf101` |
| `point_specification: Measurement` | `sbco:pointSpecification ...#Measurement` |
| `unit: ℃` | `sbco:unit ...#celsius` |

`sbco:EquipmentExt`・`sbco:PointExt` は [smartbuilding_datamodels](https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels) の `output/building_model.owl.ttl` で定義されたクラスです。

---

## Step 5：ビルOSでの活用

投入されたRDFデータをもとに、ビルOSは以下のようなことが可能になります。

- 「3F会議室101の温度ポイントをすべて取得」というクエリに対して `PT001` を返す
- 「温度が28℃を超えたら空調を制御する」というルールを汎用的に記述できる
- 異なるベンダーの建物でも同じクエリで同じ意味のデータを取れる（相互運用性）

---

*続けて読む：[ポイントリスト サンプル](pointlist_sample.md) で会議室全体（5点）の構成例を確認する*
