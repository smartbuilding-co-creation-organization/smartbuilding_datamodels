---
search:
  boost: 5.0
---

# Slot: geometry 


_Polygon representing the spatial extent of this Space._



<div data-search-exclude markdown="1">



URI: [rec:geometry](https://w3id.org/rec/geometry)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Space](Space.md) | A contiguous part of the physical world that contains or can contain sub-spac... |  no  |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
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
| Range | [GeometryInfo](GeometryInfo.md) |
| Domain Of | [Space](Space.md), [Asset](Asset.md) |
| Slot URI | [rec:geometry](https://w3id.org/rec/geometry) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:geometry |
| native | sbco:geometry |




## LinkML Source

<details>
```yaml
name: geometry
description: Polygon representing the spatial extent of this Space.
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:geometry
domain_of:
- Space
- Asset
range: GeometryInfo
multivalued: false

```
</details></div>