

# Slot: hasPart 


_The subject is composed in part of the entity given by the object._





URI: [rec:hasPart](https://w3id.org/rec/hasPart)
Alias: hasPart

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Space](Space.md) | A contiguous part of the physical world that contains or can contain sub-spac... |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [Level](Level.md) | A building storey |  no  |






## Properties

* Range: [Any](Any.md)&nbsp;or&nbsp;<br />[Space](Space.md)&nbsp;or&nbsp;<br />[Site](Site.md)&nbsp;or&nbsp;<br />[Building](Building.md)&nbsp;or&nbsp;<br />[Level](Level.md)&nbsp;or&nbsp;<br />[Room](Room.md)&nbsp;or&nbsp;<br />[Zone](Zone.md)&nbsp;or&nbsp;<br />[OutdoorSpace](OutdoorSpace.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:hasPart |
| native | sbco:hasPart |




## LinkML Source

<details>
```yaml
name: hasPart
description: The subject is composed in part of the entity given by the object.
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:hasPart
alias: hasPart
domain_of:
- Space
- Asset
range: Any
multivalued: true
any_of:
- range: Space
- range: Site
- range: Building
- range: Level
- range: Room
- range: Zone
- range: OutdoorSpace

```
</details>