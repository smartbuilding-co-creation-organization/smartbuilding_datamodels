---
search:
  boost: 5.0
---

# Slot: pointType 


_Point type - a profile or template name used to refer to the telemetry format obtainable from the device or point. Specific definitions are provided separately in schema files._






URI: [sbco:pointType](https://www.sbco.or.jp/ont/pointType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PointExt](PointExt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_ja | ポイントタイプ - 機器やポイントから取得できるテレメトリのフォーマットを参照するためのプロファイル名、またはテンプレート名。具体的な定義については、スキーマファイル等で当該タイプについては別途定義される。 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:pointType |
| native | sbco:pointType |




## LinkML Source

<details markdown="1">
```yaml
name: pointType
annotations:
  description_ja:
    tag: description_ja
    value: ポイントタイプ - 機器やポイントから取得できるテレメトリのフォーマットを参照するためのプロファイル名、またはテンプレート名。具体的な定義については、スキーマファイル等で当該タイプについては別途定義される。
description: Point type - a profile or template name used to refer to the telemetry
  format obtainable from the device or point. Specific definitions are provided separately
  in schema files.
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- PointExt
range: string
required: true

```
</details>