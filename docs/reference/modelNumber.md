---
search:
  boost: 5.0
---

# Slot: modelNumber 


_Model number of the asset_






URI: [rec:modelNumber](https://w3id.org/rec/modelNumber)
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
| Range | [String](String.md) |
| Domain Of | [Asset](Asset.md) |
| Slot URI | [rec:modelNumber](https://w3id.org/rec/modelNumber) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:modelNumber |
| native | sbco:modelNumber |




## LinkML Source

<details markdown="1">
```yaml
name: modelNumber
description: Model number of the asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:modelNumber
domain_of:
- Asset
range: string

```
</details>