

# Slot: aggregate 


_Aggregation function or method for point data processing_





URI: [brick:aggregate](https://brickschema.org/schema/Brick#aggregate)
Alias: aggregate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Point](Point.md) | A sensor, actuator, or data point associated with equipment |  no  |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |






## Properties

* Range: [AggregateEnum](AggregateEnum.md)




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | ポイントデータ処理のための集約関数または方法 |
| azure_dtdl_type | DTObjectInfo |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brick:aggregate |
| native | sbco:aggregate |




## LinkML Source

<details>
```yaml
name: aggregate
annotations:
  description_ja:
    tag: description_ja
    value: ポイントデータ処理のための集約関数または方法
  azure_dtdl_type:
    tag: azure_dtdl_type
    value: DTObjectInfo
description: Aggregation function or method for point data processing
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: brick:aggregate
alias: aggregate
domain_of:
- Point
range: AggregateEnum

```
</details>