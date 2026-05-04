

# Slot: supplier 


_Supplier or vendor of the device associated with this point_





URI: [sbco:supplier](https://www.sbco.or.jp/ont/supplier)
Alias: supplier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | このポイントに関連するデバイスのサプライヤーまたはベンダー |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:supplier |
| native | sbco:supplier |




## LinkML Source

<details>
```yaml
name: supplier
annotations:
  description_ja:
    tag: description_ja
    value: このポイントに関連するデバイスのサプライヤーまたはベンダー
description: Supplier or vendor of the device associated with this point
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
alias: supplier
domain_of:
- PointExt
range: string

```
</details>