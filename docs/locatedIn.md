

# Slot: locatedIn 


_Space where this asset is located_





URI: [rec:locatedIn](https://w3id.org/rec/locatedIn)
Alias: locatedIn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  yes  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  yes  |






## Properties

* Range: [Any](Any.md)&nbsp;or&nbsp;<br />[Space](Space.md)&nbsp;or&nbsp;<br />[Site](Site.md)&nbsp;or&nbsp;<br />[Building](Building.md)&nbsp;or&nbsp;<br />[Level](Level.md)&nbsp;or&nbsp;<br />[Room](Room.md)&nbsp;or&nbsp;<br />[Zone](Zone.md)&nbsp;or&nbsp;<br />[OutdoorSpace](OutdoorSpace.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:locatedIn |
| native | sbco:locatedIn |




## LinkML Source

<details>
```yaml
name: locatedIn
description: Space where this asset is located
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:locatedIn
alias: locatedIn
domain_of:
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