# ポイントリスト サンプルデータ

> フィールドの仕様定義は [pointlist.md](pointlist.md) を参照してください。  
> サンプルを使ったStep-by-Stepの解説は [walkthrough.md](walkthrough.md) も参照してください。

---

## シナリオ

「TokyoSite1」ビル（MainBldg）3F 会議室101 に設置された5つのポイントのサンプルです。  
2台のゲートウェイ（GW001・GW002）経由でデータを収集する構成になっています。

---

## サンプルデータ

| gateway_id | device_id | device_name | device_type | site | building | floor | installation_area | target_area | panel | point_type | point_specification | point_id | point_name | writable | interval | unit | max_pres_value | min_pres_value | labels | scale | tags | supplier | owner | local_id | device_id_bacnet | object_id_bacnet | object_type_bacnet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GW001 | DEV001 | 温度センサー01 | Sensor | TokyoSite1 | MainBldg | 3F | 会議室101 | 会議室101 | | 温度 | Measurement | PT001 | 室温センサー | false | 60 | ℃ | 50 | -10 | | 1.0 | 温度&&会議室 | メーカーA | 管理会社 | LOCAL001 | BAC001 | OBJ001 | Analog-Input |
| GW001 | DEV002 | 湿度センサー01 | Sensor | TokyoSite1 | MainBldg | 3F | 会議室101 | 会議室101 | | 湿度 | Measurement | PT002 | 室内湿度センサー | false | 60 | % | 100 | 0 | | 1.0 | 湿度&&会議室 | メーカーB | 管理会社 | LOCAL002 | BAC002 | OBJ002 | Analog-Input |
| GW001 | DEV003 | 二酸化炭素センサー | Sensor | TokyoSite1 | MainBldg | 3F | 会議室101 | 会議室101 | | CO2濃度 | Measurement | PT003 | 室内CO2センサー | false | 120 | ppm | 2000 | 400 | | 1.0 | CO2&&会議室 | メーカーC | 管理会社 | LOCAL003 | BAC003 | OBJ003 | Analog-Input |
| GW002 | DEV004 | 照度センサー01 | Sensor | TokyoSite1 | MainBldg | 3F | 会議室101 | 会議室101 | | 照度 | Measurement | PT004 | 室内照度センサー | false | 30 | lx | 10000 | 0 | | 1.0 | 照度&&会議室 | メーカーD | 管理会社 | LOCAL004 | BAC004 | OBJ004 | Analog-Input |
| GW002 | DEV005 | 空調制御01 | VAV | TokyoSite1 | MainBldg | 3F | 会議室101 | 会議室101 | PAN01 | 空調制御 | Command | PT005 | 空調制御ポイント | true | 0 | 無 | | | 開&&閉 | | 空調&&会議室 | メーカーE | 管理会社 | LOCAL005 | BAC005 | OBJ005 | Binary-Output |

---

## 各行の解説

### ゲートウェイと接続構成

PT001〜PT003（温度・湿度・CO2センサー）はすべて **GW001** 経由、PT004〜PT005（照度・空調制御）は **GW002** 経由で収集されます。同じ会議室でも機器によって接続先ゲートウェイが異なるケースが実際に起こります。

```
GW001 ──→ DEV001（温度）
      ──→ DEV002（湿度）
      ──→ DEV003（CO2）

GW002 ──→ DEV004（照度）
      ──→ DEV005（空調制御）
```

### 計測ポイントと制御ポイントの違い

**計測ポイント（PT001〜PT004）**

- `writable: false` — 読み取り専用。センサーはデータを送るだけ
- `point_specification: Measurement` — 環境値を計測
- `interval: 30〜120` — 定期的にポーリング（例：CO2は120秒おきに収集）

**制御ポイント（PT005）**

- `writable: true` — 書き込み可能。ビルOSから指令を送れる
- `point_specification: Command` — 機器への指令
- `interval: 0` — 定期ポーリングなし（書き込み時のみ通信するイベント駆動型）
- `labels: 開&&閉` — Binary-Output のため、値 0 と 1 に対応するラベルが必要

### BACnetフィールドの読み方

| フィールド | DEV001の例 | 意味 |
|---|---|---|
| `device_id_bacnet` | BAC001 | BACnetネットワーク上のデバイスID |
| `object_type_bacnet` | Analog-Input | ポイントの信号種別（連続値入力） |
| `instance_no_bacnet` | OBJ001 | デバイス内のオブジェクト識別番号 |
| `local_id` | LOCAL001 | ゲートウェイが機器を収集するための設備側識別子 |

`Analog-Input` は連続したアナログ信号（温度・湿度・CO2・照度）、`Binary-Output` は ON/OFF 等の2値信号（空調制御のオン/オフ指令）を示します。

### `&&` 区切りの理由

`labels` や `tags` フィールドで複数の値を列挙する際は `&&` で区切ります（例：`温度&&会議室`、`開&&閉`）。CSV ではカンマが列の区切り文字として使われるため、フィールド内の区切りに別の記号を使う必要があるためです。

### このサンプルのデータモデル上の表現

このサンプルデータが builder でエクスポートされると、以下の階層としてモデル化されます：

```
sbco:Site (TokyoSite1)
  └── sbco:Building (MainBldg)
        └── sbco:Level (3F)
              └── sbco:Room (会議室101)
                    ├── sbco:EquipmentExt (DEV001: 温度センサー01)
                    │     └── sbco:PointExt (PT001: 室温センサー)
                    ├── sbco:EquipmentExt (DEV002: 湿度センサー01)
                    │     └── sbco:PointExt (PT002: 室内湿度センサー)
                    ├── sbco:EquipmentExt (DEV003: 二酸化炭素センサー)
                    │     └── sbco:PointExt (PT003: 室内CO2センサー)
                    ├── sbco:EquipmentExt (DEV004: 照度センサー01)
                    │     └── sbco:PointExt (PT004: 室内照度センサー)
                    └── sbco:EquipmentExt (DEV005: 空調制御01)
                          └── sbco:PointExt (PT005: 空調制御ポイント)
```
