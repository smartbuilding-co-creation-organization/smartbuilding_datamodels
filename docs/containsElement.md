

# Slot: containsElement 


_Building element contained within this architecture_





URI: [rec:containsElement](https://w3id.org/rec/containsElement)
Alias: containsElement

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Level](Level.md) | A building storey |  no  |






## Properties

* Range: [BuildingElement](BuildingElement.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:containsElement |
| native | sbco:containsElement |




## LinkML Source

<details>
```yaml
name: containsElement
description: Building element contained within this architecture
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:containsElement
alias: containsElement
domain_of:
- Architecture
range: BuildingElement
multivalued: true

```
</details>