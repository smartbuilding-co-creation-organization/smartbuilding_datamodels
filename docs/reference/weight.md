---
search:
  boost: 5.0
---

# Slot: weight 


_Weight of the asset_






URI: [rec:weight](https://w3id.org/rec/weight)
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
| Range | [Decimal](Decimal.md) |
| Domain Of | [Asset](Asset.md) |
| Slot URI | [rec:weight](https://w3id.org/rec/weight) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:weight |
| native | sbco:weight |




## LinkML Source

<details markdown="1">
```yaml
name: weight
description: Weight of the asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:weight
domain_of:
- Asset
range: decimal

```
</details>