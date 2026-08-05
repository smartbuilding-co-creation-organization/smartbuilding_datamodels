---
search:
  boost: 5.0
---

# Slot: serialNumber 


_Serial number of the asset_






URI: [rec:serialNumber](https://w3id.org/rec/serialNumber)
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
| Slot URI | [rec:serialNumber](https://w3id.org/rec/serialNumber) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:serialNumber |
| native | sbco:serialNumber |




## LinkML Source

<details markdown="1">
```yaml
name: serialNumber
description: Serial number of the asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:serialNumber
domain_of:
- Asset
range: string

```
</details>