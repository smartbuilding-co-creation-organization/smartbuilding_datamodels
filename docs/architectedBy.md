---
search:
  boost: 5.0
---

# Slot: architectedBy 


_Agent or resource that architected this structure_



<div data-search-exclude markdown="1">



URI: [rec:architectedBy](https://w3id.org/rec/architectedBy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [Level](Level.md) | A building storey |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain Of | [Architecture](Architecture.md) |
| Slot URI | [rec:architectedBy](https://w3id.org/rec/architectedBy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:architectedBy |
| native | sbco:architectedBy |




## LinkML Source

<details>
```yaml
name: architectedBy
description: Agent or resource that architected this structure
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:architectedBy
domain_of:
- Architecture
range: Agent
multivalued: true

```
</details></div>