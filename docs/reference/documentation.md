---
search:
  boost: 5.0
---

# Slot: documentation 


_Documentation related to this asset_






URI: [rec:documentation](https://w3id.org/rec/documentation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
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
| Range | [Document](Document.md) |
| Domain Of | [Architecture](Architecture.md), [Asset](Asset.md) |
| Slot URI | [rec:documentation](https://w3id.org/rec/documentation) |

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
| self | rec:documentation |
| native | sbco:documentation |




## LinkML Source

<details markdown="1">
```yaml
name: documentation
description: Documentation related to this asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:documentation
domain_of:
- Architecture
- Asset
range: Document
multivalued: true

```
</details>