---
search:
  boost: 2.0
---


# Enum: PointSpecificationEnum 




_Point specification categories for equipment point lists_




URI: [sbco:PointSpecificationEnum](https://www.sbco.or.jp/ont/PointSpecificationEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Alarm | None | Alarm point |
| Command | None | Control command point |
| Setpoint | None | Setpoint configuration point |
| Measurement | None | Measurement point |
| Metering | None | Metering point |
| Status | None | Status indication point |




## Slots

| Name | Description |
| ---  | --- |
| [pointSpecification](pointSpecification.md) | Point specification category as shown in equipment point list |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_ja | 設備のポイントリストで示される、ポイントの区分 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema






## LinkML Source

<details markdown="1">
```yaml
name: PointSpecificationEnum
annotations:
  description_ja:
    tag: description_ja
    value: 設備のポイントリストで示される、ポイントの区分
description: Point specification categories for equipment point lists
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
permissible_values:
  Alarm:
    text: Alarm
    description: Alarm point
    annotations:
      description_ja:
        tag: description_ja
        value: 警報
  Command:
    text: Command
    description: Control command point
    annotations:
      description_ja:
        tag: description_ja
        value: 制御
  Setpoint:
    text: Setpoint
    description: Setpoint configuration point
    annotations:
      description_ja:
        tag: description_ja
        value: 設定
  Measurement:
    text: Measurement
    description: Measurement point
    annotations:
      description_ja:
        tag: description_ja
        value: 計測
  Metering:
    text: Metering
    description: Metering point
    annotations:
      description_ja:
        tag: description_ja
        value: 計量
  Status:
    text: Status
    description: Status indication point
    annotations:
      description_ja:
        tag: description_ja
        value: 状態

```
</details>
