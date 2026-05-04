

# Slot: georeference 


_A georeference creates a relationship between the local coordinate system used within a building (e.g., measured in meters) and a geographic coordinate system (e.g., lat, long, alt), such that locally placed Spaces can be resolved and rendered in that geographic coordinate system (e.g., for mapping purposes)._





URI: [rec:georeference](https://w3id.org/rec/georeference)
Alias: georeference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Level](Level.md) | A building storey |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Space](Space.md) | A contiguous part of the physical world that contains or can contain sub-spac... |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |






## Properties

* Range: [Georeference](Georeference.md)




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
alias: georeference
domain_of:
- Space
range: Georeference
multivalued: false

```
</details>