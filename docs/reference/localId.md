---
search:
  boost: 5.0
---

# Slot: localId 


_Local identifier for this point within the gateway or system_






URI: [sbco:localId](https://www.sbco.or.jp/ont/localId)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PointExt](PointExt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










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

<details markdown="1">
```yaml
name: localId
annotations:
  description_ja:
    tag: description_ja
    value: ゲートウェイまたはシステム内でのポイントのローカル識別子
description: Local identifier for this point within the gateway or system
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- PointExt
range: string

```
</details>