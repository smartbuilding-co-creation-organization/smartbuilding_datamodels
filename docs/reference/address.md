---
search:
  boost: 5.0
---

# Slot: address 


_Address of the architecture_






URI: [rec:address](https://w3id.org/rec/address)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [Level](Level.md) | A building storey |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PostalAddress](PostalAddress.md) |
| Domain Of | [Architecture](Architecture.md) |
| Slot URI | [rec:address](https://w3id.org/rec/address) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:address |
| native | sbco:address |




## LinkML Source

<details markdown="1">
```yaml
name: address
description: Address of the architecture
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:address
domain_of:
- Architecture
range: PostalAddress
multivalued: true

```
</details>