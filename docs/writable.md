---
search:
  boost: 5.0
---

# Slot: writable 


_Whether the point value can be written (commanded)_



<div data-search-exclude markdown="1">



URI: [sbco:writable](https://www.sbco.or.jp/ont/writable)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [PointExt](PointExt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_ja | ポイントの値を書き込み（制御）できるかどうか |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:writable |
| native | sbco:writable |




## LinkML Source

<details>
```yaml
name: writable
annotations:
  description_ja:
    tag: description_ja
    value: ポイントの値を書き込み（制御）できるかどうか
description: Whether the point value can be written (commanded)
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- PointExt
range: boolean

```
</details></div>