---
search:
  boost: 5.0
---

# Slot: objectTypeBacnet 


_BACnet object type (e.g., Analog-Input, Binary-Output)_






URI: [sbco:objectTypeBacnet](https://www.sbco.or.jp/ont/objectTypeBacnet)
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
| description_ja | BACnetオブジェクトタイプ（例：Analog-Input、Binary-Output） |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:objectTypeBacnet |
| native | sbco:objectTypeBacnet |




## LinkML Source

<details markdown="1">
```yaml
name: objectTypeBacnet
annotations:
  description_ja:
    tag: description_ja
    value: BACnetオブジェクトタイプ（例：Analog-Input、Binary-Output）
description: BACnet object type (e.g., Analog-Input, Binary-Output)
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- PointExt
range: string

```
</details>