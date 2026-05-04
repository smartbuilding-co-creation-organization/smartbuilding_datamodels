

# Slot: ownedBy 


_Agent or resource that owns this architecture_





URI: [rec:ownedBy](https://w3id.org/rec/ownedBy)
Alias: ownedBy

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [Level](Level.md) | A building storey |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [Room](Room.md) | A room within a building |  no  |






## Properties

* Range: [Agent](Agent.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:ownedBy |
| native | sbco:ownedBy |




## LinkML Source

<details>
```yaml
name: ownedBy
description: Agent or resource that owns this architecture
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:ownedBy
alias: ownedBy
domain_of:
- Architecture
range: Agent
multivalued: true

```
</details>