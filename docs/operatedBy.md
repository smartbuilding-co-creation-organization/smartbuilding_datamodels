

# Slot: operatedBy 


_Agent or resource that operates this architecture_





URI: [rec:operatedBy](https://w3id.org/rec/operatedBy)
Alias: operatedBy

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
| self | rec:operatedBy |
| native | sbco:operatedBy |




## LinkML Source

<details>
```yaml
name: operatedBy
description: Agent or resource that operates this architecture
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:operatedBy
alias: operatedBy
domain_of:
- Architecture
range: Agent
multivalued: true

```
</details>