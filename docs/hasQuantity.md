

# Slot: hasQuantity 


_Physical quantity measured by this point_





URI: [brick:hasQuantity](https://brickschema.org/schema/Brick#hasQuantity)
Alias: hasQuantity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Point](Point.md) | A sensor, actuator, or data point associated with equipment |  no  |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |






## Properties

* Range: [QuantityEnum](QuantityEnum.md)




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | このポイントで測定される物理量 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brick:hasQuantity |
| native | sbco:hasQuantity |




## LinkML Source

<details>
```yaml
name: hasQuantity
annotations:
  description_ja:
    tag: description_ja
    value: このポイントで測定される物理量
description: Physical quantity measured by this point
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: brick:hasQuantity
alias: hasQuantity
domain_of:
- Point
range: QuantityEnum

```
</details>