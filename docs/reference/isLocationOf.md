---
search:
  boost: 5.0
---

# Slot: isLocationOf 


_Subject is the physical location encapsulating the object._






URI: [rec:isLocationOf](https://w3id.org/rec/isLocationOf)
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
| Range | [EquipmentExt](EquipmentExt.md) |
| Domain Of | [Space](Space.md) |
| Slot URI | [rec:isLocationOf](https://w3id.org/rec/isLocationOf) |

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
| self | rec:isLocationOf |
| native | sbco:isLocationOf |




## LinkML Source

<details markdown="1">
```yaml
name: isLocationOf
description: Subject is the physical location encapsulating the object.
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:isLocationOf
domain_of:
- Space
range: EquipmentExt
multivalued: true

```
</details>