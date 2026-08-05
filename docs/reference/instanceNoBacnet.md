---
search:
  boost: 5.0
---

# Slot: instanceNoBacnet 


_BACnet object instance number_






URI: [sbco:instanceNoBacnet](https://www.sbco.or.jp/ont/instanceNoBacnet)
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
| description_ja | BACnetオブジェクトインスタンス番号 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:instanceNoBacnet |
| native | sbco:instanceNoBacnet |




## LinkML Source

<details markdown="1">
```yaml
name: instanceNoBacnet
annotations:
  description_ja:
    tag: description_ja
    value: BACnetオブジェクトインスタンス番号
description: BACnet object instance number
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- PointExt
range: string

```
</details>