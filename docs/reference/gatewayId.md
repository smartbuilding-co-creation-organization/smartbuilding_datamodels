---
search:
  boost: 5.0
---

# Slot: gatewayId 


_Identifier of the gateway device managing this point_






URI: [sbco:gatewayId](https://www.sbco.or.jp/ont/gatewayId)
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










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_ja | このポイントを管理するゲートウェイデバイスの識別子 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:gatewayId |
| native | sbco:gatewayId |




## LinkML Source

<details markdown="1">
```yaml
name: gatewayId
annotations:
  description_ja:
    tag: description_ja
    value: このポイントを管理するゲートウェイデバイスの識別子
description: Identifier of the gateway device managing this point
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- PointExt
range: string

```
</details>