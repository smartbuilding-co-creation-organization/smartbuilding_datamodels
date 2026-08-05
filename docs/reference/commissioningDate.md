---
search:
  boost: 5.0
---

# Slot: commissioningDate 


_Date when the asset was commissioned_






URI: [rec:commissioningDate](https://w3id.org/rec/commissioningDate)
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
| Range | [Date](Date.md) |
| Domain Of | [Asset](Asset.md) |
| Slot URI | [rec:commissioningDate](https://w3id.org/rec/commissioningDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:commissioningDate |
| native | sbco:commissioningDate |




## LinkML Source

<details markdown="1">
```yaml
name: commissioningDate
description: Date when the asset was commissioned
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:commissioningDate
domain_of:
- Asset
range: date

```
</details>