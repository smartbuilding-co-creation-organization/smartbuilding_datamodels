# スマートビル 標準ポイントリスト / Standard Point List for Smart Buildings

## このドキュメントについて

本ドキュメントはポイントリストのフィールド仕様を定義する技術文書です。  
**スマートビルや本プロジェクトが初めての方は、先に [getting_started.md](getting_started.md)（入門ガイド）をお読みください。**

ポイントリストは、ビルOSやゲートウェイと連携するスマートビルを構築する際の「設備・ポイント情報の一覧表」であり、[データフロー](smart_building_data_flow.md)の起点となります。ここで定義された情報がデータモデル生成ツール（[smartbuilding_datamodel_builder](https://smartbuilding-co-creation-organization.github.io/smartbuilding_datamodel_builder/)）に渡され、RDFやDTDLへのシリアライズが行われます。

## 1. 概要 / Overview
本ドキュメントは、ビルOSやそこに接続する連携ゲートウェイを有するスマートビルを構築するための標準的なポイントリストです。CSVでフォーマットされることを想定しています。
This document is a standard point list for constructing smart buildings with a building OS and connected gateway. It is intended to be formatted in CSV.

## 2. ポイントリスト定義 / Point List Definition

### 汎用ポイントマスタ / General Point Master

| 項目名 / Item Name       | 日本語名 / Japanese Name | 内容 / Description                                                                 | 必須 / Required | 利用者 / User | 備考 / Remarks                         |
|--------------------------|--------------------------|------------------------------------------------------------------------------------|-----------------|---------------|----------------------------------------|
| gateway_id               | ゲートウェイ名称         | 機器が接続されるゲートウェイの識別名。ポイントが紐付くGWデバイス名を指定する。       | 〇              | ビルOS/ GW     | GW構築者から提供される   | 
| point_id                 | ポイント識別子           | ポイントを特定するためのビル内で一意な文字列とする。                               | 〇              | ビルOS        |                                        |
| point_name               | ポイント名称             | ヒューマンリーダブルなポイント名称                                                 | 〇              | ビルOS        |                                        |
| point_type               | ポイント種別             | 機器から取得できるデータの種別、プロパティ識別子（温度、湿度、電流など）           | 〇              | ビルOS/GW     |                                        |
| point_specification      | ポイント区分             | 取得データの区分（警報/制御/設定/計測/計量/状態）                             | 〇              | ビルOS/GW     |                                        |
| writable                 | ポイント読み書きタイプ   | 制御の可否（false：読み取り可能, true：書き込み可能）                              | 〇              | ビルOS        |                                        |
| interval                 | ポーリング間隔           | データ発出間隔 (秒)                                                                |                 | ビルOS        |                                        |
| unit                     | 単位                     | ポイントの単位                                                                     |                 | ビルOS        |                                        |
| max_pres_value           | 最大値                   | アナログポイントの最大値                                                           |                 | ビルOS        |                                        |
| min_pres_value           | 最小値                   | アナログポイントの最小値                                                           |                 | ビルOS        |                                        |
| labels                   | ラベル                   | 状態値やマルチステートの場合のラベル。&&で複数のラベルを記載する                    |                 | ビルOS        |                                        |
| scale                    | 倍率                     | 取得したPresent Valueなどに対する倍率/重み                                         |                 | ビルOS        |                                        |
| device_id                | デバイス識別子           | 機器を一意に識別するID                                                             | 〇              | ビルOS/GW     | 図面記載のIDを想定             |
| device_name              | デバイス名称             | ヒューマンリーダブルな機器名称                                                     | 〇              | ビルOS/GW     | 図面記載の名称を想定             |
| device_type              | デバイス種別             | 機器の種類。デバイス種別によりどのようなポイントを持つか決まる。（例：VAV、EHP、Sensor） | 〇              | ビルOS/GW     | Equipment拡張クラス（独自定義）       |
| site                     | 土地名称                 | 機器が設置されるデータモデル上の土地                                               | 〇              | ビルOS        |                                        |
| building                 | 建物名称                 | 機器が設置されるデータモデル上の建物                                               | 〇              | ビルOS        |                                        |
| floor                    | 階名称                   | 機器が設置されるデータモデル上の階                                                 | 〇              | ビルOS        |                                        |
| installation_area        | 設置エリア               | 機器が設置されるデータモデル上の部屋（エリア）                                     | 〇              | ビルOS        |                                        |
| target_area              | 制御対象エリア           | 機器の制御対象エリア                                                              |               | ビルOS        |                                        |
| panel                    | 制御盤情報               | デバイスが接続されている制御盤（RSなど）の名前またはID。                           |                 | ビルOS        |                                        |
| tags                     | タグ情報                 | 検索用タグ。&&で複数のタグを記載可能                                              |                 | ビルOS        |                                        |
| supplier                 | 提供者                   | デバイスやポイントを設置しているメーカー、またはベンダー                            |                 | ビルOS        |                                        |
| owner                    | 所有者                   | デバイスの所有者                                                                   |                 | ビルOS        |                                        |
| description | 説明 | ポイントに関する説明 | | ビルOS | |
| local_id                 | 設備側ポイント識別子     | 設備側のポイント読み取り・コントロール対象ポイントを特定するための識別子情報        | 〇              | GW            | BACnetでいうとObjectID, MQTTであればTOPIC |
| device_id_bacnet         | 機器ID                   | BACnet接続情報。デバイス識別子                                                    |                 | GW            |                                        |
| instance_no_bacnet         | オブジェクト種別         | BACnet接続情報。BACnetオブジェクト内でのポイント識別に利用する番号                         |                 | GW            |                                        |
| object_type_bacnet       | インスタンス番号         | BACnetのオブジェクトタイプ。Analog-Input、Binary-Input等                           |                 | GW            |                                        |

## 3. 値定義 / Value Definitions

### デバイス識別子 (device_id) / Device Identifier (device_id)
同じ識別子を持つポイントは1つのデバイスとして認識される。モデルとしても１つに統合され、ポイントはデバイス内のプロパティとして表現される。  
Points with the same identifier are recognized as one device. They are integrated into one model, and points are represented as properties within the device.

### デバイス種別 (device_type) / Device Type (device_type)
デバイスに設定されたプロパティや、値定義などを参照するためのプロファイル名、またはテンプレート名。
具体的な定義については、スキーマファイル等で当該タイプについては別途定義される。
Web of ThingsではThing Modelとして表現されるもの。[UDMI](https://faucetsdn.github.io/udmi/)にも同様のスキーマが定義されている。
The device type is a profile or template name used to refer to the properties and value definitions set for the device. Specific definitions are provided separately in schema files. In the Web of Things, it is represented as a Thing Model.

### 空間情報 (site / building / floor / installation_area / target_area)
BIMの階層構造から抽出することが望ましいが、プロジェクトの進行上、BIMの整備が難しい場合、
仕様決定がなされた段階で設置位置については、確定しているはずなので、ポイントリストに直接記述をする。  
Spatial information should ideally be extracted from the BIM hierarchical structure. However, if BIM development is difficult due to project progress, the installation location should be determined at the specification stage and directly described in the point list.

### ポイント種別 (point_type)
機器やポイントから取得できるテレメトリのフォーマットを参照するためのプロファイル名、またはテンプレート名。
具体的な定義については、スキーマファイル等で当該タイプについては別途定義される。
以下、JSON-Schemaでの記述例。  
The point type is a profile or template name used to refer to the telemetry format obtainable from the device or point. Specific definitions are provided separately in schema files. Below is an example in JSON Schema.

```JSON Schema Example
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "IoT Device Telemetry",
    "description": "Schema for telemetry data from Building devices",
    "type": "object",
    "properties": {
        "point_id": {
            "type": "string",
            "description": "Unique identifier for the telemetry point"
        },
        "value": {
            "type": "number/string",
            "description": "Representative value of the telemetry data"
        },
        "data": {
            "type": "object",
            "description": "Additional data associated with the telemetry point",
            "properties": {},
            "additionalProperties": true
        },
        "datetime": {
            "type": "string",
            "format": "date-time",
            "description": "Date and time when the telemetry data was recorded in ISO 8601 format"
        },
        "building": {
            "type": "string",
            "description": "Name of the building the telemetry point belongs to"
        },
        "name": {
            "type": "string",
            "description": "Optional name of the telemetry point"
        },
        "device_id": {
            "type": "string",
            "description": "Optional device identifier"
        }
    },
    "required": ["point_id", "value","datetime"],
    "additionalProperties": false
}
```

### ポイント区分（point_specification）/ Point Specification
設備のポイントリストで示される、ポイントの区分を明示。英語での指定を推奨。  
Specify the category as shown in the equipment point list. English is recommended.
- Alarm: 警報
- Command: 制御
- Setpoint : 設定
- Measurement: 計測
- Metering: 計量
- Status: 状態

### ポーリング間隔・ポーリング間隔性能(interval, interval_capability)
ゲートウェイからビルOSに発出するデータの間隔をintervalとする。秒で指定をする。
ゲートウェイまたはゲートウェイ配下のデバイスにおける、データ発出間隔の最小値をinterval_capabilityとした。  
The interval is the data transmission interval from the gateway to the building OS. The interval_capability is the minimum data transmission interval for the gateway or devices under the gateway.

### 測定単位（unit）/ Measurement Units
ヒューマンリーダブルな単位を指定。以下は例。ヒューマンリーダブルなものが分かりやすいが、その後の活用を考慮すると、[QUDT](https://qudt.org/)の利用も有効。  
Specify human-readable units. Examples:
- ℃: 温度 / Temperature
- %: 湿度 / Humidity
- ppm: CO2濃度 / CO2 Concentration
- kWh: 電力量 / Energy Consumption
- lx: 照度 / Illuminance

### 最大値、最小値 (max_pres_value, min_pres_value)
対象ポイントが数値である場合の最小値と最大値。BACnetの[オブジェクトリスト授受用CSVフォーマット](https://www.azbil.com/jp/product/building/system/image/ak007_v1.02.pdf)の語彙を参考にしている。  
The minimum and maximum values for numerical points. Refer to the vocabulary of BACnet's [CSV format for object list exchange](https://www.azbil.com/jp/product/building/system/image/ak007_v1.02.pdf).

### ラベル (labels)
BACnetにおいて、ポイントの種別がマルチステートの場合は、0, 1, 2などに対応したラベルがないと、アプリケーションが値を解釈することができない。
CSVのフォーマットだと、カンマで区切ることができないので、&&で区切ることとした。  
In BACnet, if the point type is multi-state, labels corresponding to 0, 1, 2, etc., are necessary for applications to interpret the values. In CSV format, commas cannot be used as separators, so && is used instead.

### スケール (scale)
機器から送信されるデータは、スケールを考慮せずに送られてくる場合がある。
中央監視システムなどでは、それらをシステム側が変換して利用することが一般的である。
ゲートウェイで、スケールを乗じてクラウド側に送ることも可能であるが、そのまま送られることも多いので、ポイントリストに記載することとしている。  
Data sent from devices may not consider scale. Central monitoring systems typically convert and use such data. While gateways can apply scale before sending data to the cloud, it is often sent as-is, so it is included in the point list.

### タグ (tags)
データモデルをもとにしたセマンティックな検索によっても、リソースの同定は可能であるが、ビルOSによっては、タグ検索が可能なものもあると考えられる。
タグの語彙に特に指定はないが[Heystack](https://project-haystack.org/doc/appendix/tags)などで定義されたタグが参考になる。ラベルと同様に&&で区切ることとしている。  
Semantic searches based on the data model can identify resources, but some building OS may support tag searches. There are no specific vocabulary requirements for tags, but tags defined by [Heystack](https://project-haystack.org/doc/appendix/tags) can be useful. Tags are separated by &&, similar to labels.

### 設備側ポイント識別子 (local_id)
ローカルネットワークに設定されたゲートウェイが、現地のデバイスからデータを収集するために必要な情報。
例えば、BACnetであれば、オブジェクトリスト授受用CSVフォーマットで指定されるObject IDなどを設定する。IoT機器であれば、MQTTのTOPICなど。
実際の設定に当たっては、IPアドレスなどの情報が必要になるが、それらは別途やり取りをすることを前提とする。  
Information required for a gateway set up on a local network to collect data from on-site devices. For example, in BACnet, the Object ID specified in the CSV format for object list exchange is set. For IoT devices, the MQTT TOPIC is set. Actual settings require information such as IP addresses, which are exchanged separately.

## 4. データ制約 / Data Constraints
- 必須項目（○）は必ず値が設定されていること。  
        Required items (○) must have values set.

## 5. サンプルポイントデータ / Sample Point Data

3F 会議室101（5ポイント）の記入例は **[pointlist_sample.md](pointlist_sample.md)** を参照してください。  
各フィールドの読み方・BACnet値の解釈・ゲートウェイ構成の解説も同ファイルに収録しています。