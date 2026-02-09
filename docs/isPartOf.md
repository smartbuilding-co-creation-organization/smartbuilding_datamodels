

# Slot: isPartOf 



URI: [rec:isPartOf](https://w3id.org/rec/isPartOf)
Alias: isPartOf

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Room](Room.md) | A room within a building |  no  |
| [Space](Space.md) | A contiguous part of the physical world that contains or can contain sub-spac... |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [Level](Level.md) | A building storey |  no  |






## Properties

* Range: [Any](Any.md)&nbsp;or&nbsp;<br />[Space](Space.md)&nbsp;or&nbsp;<br />[Site](Site.md)&nbsp;or&nbsp;<br />[Building](Building.md)&nbsp;or&nbsp;<br />[Level](Level.md)&nbsp;or&nbsp;<br />[Room](Room.md)&nbsp;or&nbsp;<br />[Zone](Zone.md)&nbsp;or&nbsp;<br />[OutdoorSpace](OutdoorSpace.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:isPartOf |
| native | sbco:isPartOf |




## LinkML Source

<details>
```yaml
name: isPartOf
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:isPartOf
alias: isPartOf
domain_of:
- Space
- Asset
range: Any
multivalued: false
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