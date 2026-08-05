# 用語集

本プロジェクトで使用する主要な用語を五十音順・カテゴリ別にまとめます。  
概念の全体像を把握するには [getting_started.md](getting_started.md) を参照してください。

---

## スマートビル・設備

| 用語 | 英語 | 説明 |
|------|------|------|
| ゲートウェイ | Gateway | 現地の設備機器とクラウドをつなぐ中継装置。`gateway_id` で識別する |
| ポイント | Point | センサーや制御機器が持つデータの1単位。計測・制御・警報などの種類がある |
| ポイントリスト | Point List | 建物内の全ポイントを記録したCSVカタログ |
| ビルOS | Building OS | 建物の設備データを統合管理するプラットフォーム |
| デジタルツイン | Digital Twin | 物理的な建物のデータ上の仮想モデル |
| BMS | BMS (Building Management System) | 建物設備（空調・照明・防災等）を統合監視・制御するシステム |
| BACS | BACS (Building Automation and Control System) | 建物の自動化・制御システム。BMSとほぼ同義で使われることも多い |
| VAV | VAV (Variable Air Volume) | 可変風量ユニット。室温に応じて吹き出す風量を調節するHVAC設備 |
| AHU | AHU (Air Handling Unit) | エアハンドリングユニット。空気の温度・湿度・清浄を調整する空調機器 |

---

## ポイント区分（point_specification）

| 英語名 | 日本語 | 説明 |
|--------|--------|------|
| Measurement | 計測 | センサーが測定した値（読み取り専用） |
| Metering | 計量 | 電力・ガス・水などの累積量 |
| Status | 状態 | 機器の稼働状態（運転中/停止など） |
| Setpoint | 設定 | 目標値（設定温度など） |
| Command | 制御 | 機器への指令（書き込み可能） |
| Alarm | 警報 | 異常・アラームの通知 |

---

## 通信プロトコル

| 用語 | 英語 | 説明 |
|------|------|------|
| BACnet | BACnet (Building Automation and Control Networks) | 建物設備の制御・監視に広く使われる通信プロトコル（ASHRAE規格）。空調・照明・防災設備の多くが対応 |
| MQTT | MQTT (Message Queuing Telemetry Transport) | IoT機器に広く使われる軽量なPub/Subメッセージングプロトコル |

---

## データモデル・オントロジー

| 用語 | 英語 | 説明 |
|------|------|------|
| オントロジー | Ontology | 概念・関係・制約を機械が理解できる形式で定義した知識体系。「辞書＋文法」の役割 |
| RDF | RDF (Resource Description Framework) | 情報をトリプル（主語・述語・目的語）で表すW3C標準のデータモデル |
| Turtle | Turtle | RDFの人間可読なシリアライズ形式（拡張子 `.ttl`） |
| JSON-LD | JSON-LD | RDFをJSON形式で表現するシリアライズ形式 |
| OWL | OWL (Web Ontology Language) | RDFを拡張したオントロジー記述言語（W3C標準）。クラス・プロパティ・制約を定義 |
| SHACL | SHACL (Shapes Constraint Language) | RDFデータのバリデーションルールを定義するW3C標準 |
| LinkML | LinkML | データモデルをYAMLで記述し、OWL・SHACL・JSON Schemaを自動生成するツール |
| DTDL | DTDL (Digital Twins Definition Language) | Microsoft Azure Digital Twins で使われるデータ記述言語 |

---

## 建物オントロジー標準

| 用語 | 正式名称 | 説明 |
|------|---------|------|
| Brick | Brick Schema | 建物設備・ポイントのオントロジー標準。センサー・制御点・設備クラスを豊富に定義（米国発） |
| RealEstateCore | RealEstateCore (REC) | 不動産・建物管理のオントロジー標準。空間・設備・運用情報をカバー（スウェーデン発） |
| BOT | BOT (Building Topology Ontology) | 建物の空間的階層（サイト・建物・フロア・部屋）を表すW3C LBDオントロジー |
| QUDT | QUDT (Quantities, Units, Dimensions and Types) | 計測単位の標準語彙。℃・%・ppm などを機械可読な形式で定義 |
| bSDD | buildingSMART Data Dictionary | 建築・設備のデジタル辞書。IFCと連携した用語定義サービス |
| BDNS | Building Device Naming Specification | 建物内の設備・センサー・制御点に一貫した命名規則を与える仕様 |
| IFC | IFC (Industry Foundation Classes) | BIM（建物情報モデリング）のデータ標準。建物設計情報を含む |
| NGSI-LD | NGSI-LD | スマートシティ向けのLinked Dataコンテキスト管理API標準（ETSI） |

---

## 組織・プログラム

| 用語 | 説明 |
|------|------|
| SBCO | スマートビルディング共創機構。本プロジェクトの標準を策定する組織 |
| IEA Annex 81 | 国際エネルギー機関（IEA）の「Data-Driven Smart Buildings」プログラム。2025年最終報告書を発行 |
| FAIR原則 | Findable（発見可能）・Accessible（アクセス可能）・Interoperable（相互運用可能）・Reusable（再利用可能）。データ管理の国際指針 |
