

# Slot: address 


_Address of the architecture_





URI: [rec:address](https://w3id.org/rec/address)
Alias: address

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Room](Room.md) | A room within a building |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [Level](Level.md) | A building storey |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |






## Properties

* Range: [PostalAddress](PostalAddress.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:address |
| native | sbco:address |




## LinkML Source

<details>
```yaml
name: address
description: Address of the architecture
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:address
alias: address
domain_of:
- Architecture
range: PostalAddress
multivalued: true

```
</details>