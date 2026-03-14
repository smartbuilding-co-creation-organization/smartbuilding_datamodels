

# Slot: deviceIdBacnet 


_BACnet device identifier_





URI: [sbco:deviceIdBacnet](https://www.sbco.or.jp/ont/deviceIdBacnet)
Alias: deviceIdBacnet

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
| description_ja | BACnetデバイス識別子 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:deviceIdBacnet |
| native | sbco:deviceIdBacnet |




## LinkML Source

<details>
```yaml
name: deviceIdBacnet
annotations:
  description_ja:
    tag: description_ja
    value: BACnetデバイス識別子
description: BACnet device identifier
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
alias: deviceIdBacnet
domain_of:
- PointExt
range: string

```
</details>