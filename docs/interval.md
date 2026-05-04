

# Slot: interval 


_Polling or reporting interval in seconds_





URI: [sbco:interval](https://www.sbco.or.jp/ont/interval)
Alias: interval

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |






## Properties

* Range: [Integer](Integer.md)




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | ポーリングまたはレポートの間隔（秒） |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:interval |
| native | sbco:interval |




## LinkML Source

<details>
```yaml
name: interval
annotations:
  description_ja:
    tag: description_ja
    value: ポーリングまたはレポートの間隔（秒）
description: Polling or reporting interval in seconds
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
alias: interval
domain_of:
- PointExt
range: integer

```
</details>