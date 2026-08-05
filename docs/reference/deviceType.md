---
search:
  boost: 5.0
---

# Slot: deviceType 


_Device Type_






URI: [sbco:deviceType](https://www.sbco.or.jp/ont/deviceType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [EquipmentExt](EquipmentExt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:deviceType |
| native | sbco:deviceType |




## LinkML Source

<details markdown="1">
```yaml
name: deviceType
description: Device Type
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- EquipmentExt
range: string

```
</details>