---
search:
  boost: 5.0
---

# Slot: levelNumber 


_Floor or level number within a building_



<div data-search-exclude markdown="1">



URI: [rec:levelNumber](https://w3id.org/rec/levelNumber)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Level](Level.md) | A building storey |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Level](Level.md) |
| Slot URI | [rec:levelNumber](https://w3id.org/rec/levelNumber) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_ja | 建物内のフロアまたはレベル番号 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:levelNumber |
| native | sbco:levelNumber |




## LinkML Source

<details>
```yaml
name: levelNumber
annotations:
  description_ja:
    tag: description_ja
    value: 建物内のフロアまたはレベル番号
description: Floor or level number within a building
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:levelNumber
domain_of:
- Level
range: integer

```
</details></div>