---
search:
  boost: 5.0
---

# Slot: commissionedBy 


_Agent or resource that commissioned this asset_



<div data-search-exclude markdown="1">



URI: [rec:commissionedBy](https://w3id.org/rec/commissionedBy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain Of | [Asset](Asset.md) |
| Slot URI | [rec:commissionedBy](https://w3id.org/rec/commissionedBy) |

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
| self | rec:commissionedBy |
| native | sbco:commissionedBy |




## LinkML Source

<details>
```yaml
name: commissionedBy
description: Agent or resource that commissioned this asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:commissionedBy
domain_of:
- Asset
range: Agent
multivalued: true

```
</details></div>