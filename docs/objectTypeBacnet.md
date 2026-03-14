

# Slot: objectTypeBacnet 


_BACnet object type (e.g., Analog-Input, Binary-Output)_





URI: [sbco:objectTypeBacnet](https://www.sbco.or.jp/ont/objectTypeBacnet)
Alias: objectTypeBacnet

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
| description_ja | BACnetオブジェクトタイプ（例：Analog-Input、Binary-Output） |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:objectTypeBacnet |
| native | sbco:objectTypeBacnet |




## LinkML Source

<details>
```yaml
name: objectTypeBacnet
annotations:
  description_ja:
    tag: description_ja
    value: BACnetオブジェクトタイプ（例：Analog-Input、Binary-Output）
description: BACnet object type (e.g., Analog-Input, Binary-Output)
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
alias: objectTypeBacnet
domain_of:
- PointExt
range: string

```
</details>