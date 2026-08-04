---
search:
  boost: 5.0
---

# Slot: deviceIdBacnet 


_BACnet device identifier_



<div data-search-exclude markdown="1">



URI: [sbco:deviceIdBacnet](https://www.sbco.or.jp/ont/deviceIdBacnet)
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
| description_ja | BACnetデバイス識別子 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:deviceIdBacnet |
| native | sbco:deviceIdBacnet |




## LinkML Source

<details>
```yaml
name: deviceIdBacnet
annotations:
  description_ja:
    tag: description_ja
    value: BACnetデバイス識別子
description: BACnet device identifier
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- PointExt
range: string

```
</details></div>