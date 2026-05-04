

# Slot: isPointOf 


_Equipment that this point belongs to_





URI: [brick:isPointOf](https://brickschema.org/schema/Brick#isPointOf)
Alias: isPointOf

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Point](Point.md) | A sensor, actuator, or data point associated with equipment |  no  |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  yes  |






## Properties

* Range: [Equipment](Equipment.md)




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | このポイントが属する設備 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brick:isPointOf |
| native | sbco:isPointOf |




## LinkML Source

<details>
```yaml
name: isPointOf
annotations:
  description_ja:
    tag: description_ja
    value: このポイントが属する設備
description: Equipment that this point belongs to
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: brick:isPointOf
alias: isPointOf
domain_of:
- Point
range: Equipment

```
</details>