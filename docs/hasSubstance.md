

# Slot: hasSubstance 


_Substance associated with this point_





URI: [brick:hasSubstance](https://brickschema.org/schema/Brick#hasSubstance)
Alias: hasSubstance

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |
| [Point](Point.md) | A sensor, actuator, or data point associated with equipment |  no  |






## Properties

* Range: [SubstanceEnum](SubstanceEnum.md)




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | このポイントに関連する物質 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brick:hasSubstance |
| native | sbco:hasSubstance |




## LinkML Source

<details>
```yaml
name: hasSubstance
annotations:
  description_ja:
    tag: description_ja
    value: このポイントに関連する物質
description: Substance associated with this point
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: brick:hasSubstance
alias: hasSubstance
domain_of:
- Point
range: SubstanceEnum

```
</details>