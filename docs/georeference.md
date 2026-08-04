---
search:
  boost: 5.0
---

# Slot: georeference 


_A georeference creates a relationship between the local coordinate system used within a building (e.g., measured in meters) and a geographic coordinate system (e.g., lat, long, alt), such that locally placed Spaces can be resolved and rendered in that geographic coordinate system (e.g., for mapping purposes)._



<div data-search-exclude markdown="1">



URI: [rec:georeference](https://w3id.org/rec/georeference)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Space](Space.md) | A contiguous part of the physical world that contains or can contain sub-spac... |  no  |
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
| Range | [GeoreferenceInfo](GeoreferenceInfo.md) |
| Domain Of | [Space](Space.md) |
| Slot URI | [rec:georeference](https://w3id.org/rec/georeference) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:georeference |
| native | sbco:georeference |




## LinkML Source

<details>
```yaml
name: georeference
description: A georeference creates a relationship between the local coordinate system
  used within a building (e.g., measured in meters) and a geographic coordinate system
  (e.g., lat, long, alt), such that locally placed Spaces can be resolved and rendered
  in that geographic coordinate system (e.g., for mapping purposes).
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:georeference
domain_of:
- Space
range: GeoreferenceInfo
multivalued: false

```
</details></div>