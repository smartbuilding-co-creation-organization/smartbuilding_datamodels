

# Slot: isLocationOf 


_Subject is the physical location encapsulating the object._





URI: [rec:isLocationOf](https://w3id.org/rec/isLocationOf)
Alias: isLocationOf

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Space](Space.md) | A contiguous part of the physical world that contains or can contain sub-spac... |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Level](Level.md) | A building storey |  no  |






## Properties

* Range: [EquipmentExt](EquipmentExt.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:isLocationOf |
| native | sbco:isLocationOf |




## LinkML Source

<details>
```yaml
name: isLocationOf
description: Subject is the physical location encapsulating the object.
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:isLocationOf
alias: isLocationOf
domain_of:
- Space
range: EquipmentExt
multivalued: true

```
</details>