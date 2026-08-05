---
search:
  boost: 5.0
---

# Slot: owns 


_ Indicates ownership of some thing, e.g., a building, an asset, an organization, etc._






URI: [rec:owns](https://w3id.org/rec/owns)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Agent](Agent.md) | An entity that can act or be acted upon |  no  |
| [Organization](Organization.md) | An organization such as a company, institution, or association |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Resource](Resource.md) |
| Domain Of | [Agent](Agent.md) |
| Slot URI | [rec:owns](https://w3id.org/rec/owns) |

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
| self | rec:owns |
| native | sbco:owns |




## LinkML Source

<details markdown="1">
```yaml
name: owns
description: ' Indicates ownership of some thing, e.g., a building, an asset, an organization,
  etc.'
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:owns
domain_of:
- Agent
range: Resource
multivalued: true

```
</details>