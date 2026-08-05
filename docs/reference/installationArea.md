---
search:
  boost: 5.0
---

# Slot: installationArea 


_Parent installation area_






URI: [sbco:installationArea](https://www.sbco.or.jp/ont/installationArea)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [EquipmentExt](EquipmentExt.md), [PointExt](PointExt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:installationArea |
| native | sbco:installationArea |




## LinkML Source

<details markdown="1">
```yaml
name: installationArea
description: Parent installation area
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- EquipmentExt
- PointExt
range: string

```
</details>