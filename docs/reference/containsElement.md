---
search:
  boost: 5.0
---

# Slot: containsElement 


_Building element contained within this architecture_






URI: [rec:containsElement](https://w3id.org/rec/containsElement)
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
| Range | [BuildingElement](BuildingElement.md) |
| Domain Of | [Architecture](Architecture.md) |
| Slot URI | [rec:containsElement](https://w3id.org/rec/containsElement) |

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
| self | rec:containsElement |
| native | sbco:containsElement |




## LinkML Source

<details markdown="1">
```yaml
name: containsElement
description: Building element contained within this architecture
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:containsElement
domain_of:
- Architecture
range: BuildingElement
multivalued: true

```
</details>