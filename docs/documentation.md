

# Slot: documentation 


_Documentation related to this asset_





URI: [rec:documentation](https://w3id.org/rec/documentation)
Alias: documentation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Level](Level.md) | A building storey |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |






## Properties

* Range: [Document](Document.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:documentation |
| native | sbco:documentation |




## LinkML Source

<details>
```yaml
name: documentation
description: Documentation related to this asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:documentation
alias: documentation
domain_of:
- Architecture
- Asset
range: Document
multivalued: true

```
</details>