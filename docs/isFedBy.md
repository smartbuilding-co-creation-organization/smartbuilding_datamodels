---
search:
  boost: 5.0
---

# Slot: isFedBy 


_Resource that feeds this architecture_



<div data-search-exclude markdown="1">



URI: [rec:isFedBy](https://w3id.org/rec/isFedBy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [Level](Level.md) | A building storey |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Resource](Resource.md) |
| Domain Of | [Architecture](Architecture.md), [Equipment](Equipment.md) |
| Slot URI | [rec:isFedBy](https://w3id.org/rec/isFedBy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| substance | SubstanceEnum |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:isFedBy |
| native | sbco:isFedBy |




## LinkML Source

<details>
```yaml
name: isFedBy
annotations:
  substance:
    tag: substance
    value: SubstanceEnum
description: Resource that feeds this architecture
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:isFedBy
domain_of:
- Architecture
- Equipment
range: Resource
multivalued: true

```
</details></div>