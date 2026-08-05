---
search:
  boost: 5.0
---

# Slot: targetArea 


_Target area for this resource_






URI: [sbco:targetArea](https://www.sbco.or.jp/ont/targetArea)
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
| self | sbco:targetArea |
| native | sbco:targetArea |




## LinkML Source

<details markdown="1">
```yaml
name: targetArea
description: Target area for this resource
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- EquipmentExt
- PointExt
range: string

```
</details>