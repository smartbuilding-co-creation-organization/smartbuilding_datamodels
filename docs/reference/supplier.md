---
search:
  boost: 5.0
---

# Slot: supplier 


_Supplier or vendor of the device associated with this point_






URI: [sbco:supplier](https://www.sbco.or.jp/ont/supplier)
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
| description_ja | このポイントに関連するデバイスのサプライヤーまたはベンダー |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:supplier |
| native | sbco:supplier |




## LinkML Source

<details markdown="1">
```yaml
name: supplier
annotations:
  description_ja:
    tag: description_ja
    value: このポイントに関連するデバイスのサプライヤーまたはベンダー
description: Supplier or vendor of the device associated with this point
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- PointExt
range: string

```
</details>