---
search:
  boost: 5.0
---

# Slot: interval 


_Polling or reporting interval in seconds_



<div data-search-exclude markdown="1">



URI: [sbco:interval](https://www.sbco.or.jp/ont/interval)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [PointExt](PointExt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_ja | ポーリングまたはレポートの間隔（秒） |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:interval |
| native | sbco:interval |




## LinkML Source

<details>
```yaml
name: interval
annotations:
  description_ja:
    tag: description_ja
    value: ポーリングまたはレポートの間隔（秒）
description: Polling or reporting interval in seconds
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- PointExt
range: integer

```
</details></div>