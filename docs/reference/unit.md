---
search:
  boost: 5.0
---

# Slot: unit 


_Measurement unit (enum key; symbol can be taken from annotations)_






URI: [sbco:unit](https://www.sbco.or.jp/ont/unit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [UnitEnum](UnitEnum.md) |
| Domain Of | [PointExt](PointExt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:unit |
| native | sbco:unit |




## LinkML Source

<details markdown="1">
```yaml
name: unit
description: Measurement unit (enum key; symbol can be taken from annotations)
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- PointExt
range: UnitEnum

```
</details>