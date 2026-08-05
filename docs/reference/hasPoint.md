---
search:
  boost: 5.0
---

# Slot: hasPoint 


_Point associated with this architecture_






URI: [rec:hasPoint](https://w3id.org/rec/hasPoint)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  yes  |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  yes  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [Level](Level.md) | A building storey |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Point](Point.md) |
| Domain Of | [Architecture](Architecture.md), [Asset](Asset.md) |
| Slot URI | [rec:hasPoint](https://w3id.org/rec/hasPoint) |

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
| self | rec:hasPoint |
| native | sbco:hasPoint |




## LinkML Source

<details markdown="1">
```yaml
name: hasPoint
description: Point associated with this architecture
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:hasPoint
domain_of:
- Architecture
- Asset
range: Point
multivalued: true

```
</details>