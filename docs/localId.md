

# Slot: localId 


_Local identifier for this point within the gateway or system_





URI: [sbco:localId](https://www.sbco.or.jp/ont/localId)
Alias: localId

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
| description_ja | ゲートウェイまたはシステム内でのポイントのローカル識別子 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:localId |
| native | sbco:localId |




## LinkML Source

<details>
```yaml
name: localId
annotations:
  description_ja:
    tag: description_ja
    value: ゲートウェイまたはシステム内でのポイントのローカル識別子
description: Local identifier for this point within the gateway or system
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
alias: localId
domain_of:
- PointExt
range: string

```
</details>