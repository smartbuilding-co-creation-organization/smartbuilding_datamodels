

# Slot: isFedBy 


_Resource that feeds this architecture_





URI: [rec:isFedBy](https://w3id.org/rec/isFedBy)
Alias: isFedBy

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Level](Level.md) | A building storey |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |






## Properties

* Range: [Resource](Resource.md)

* Multivalued: True




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
alias: isFedBy
domain_of:
- Architecture
- Equipment
range: Resource
multivalued: true

```
</details>