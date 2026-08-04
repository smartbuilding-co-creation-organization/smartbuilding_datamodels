---
search:
  boost: 2.0
---


# Enum: UnitEnum 




_Allowed measurement units_



<div data-search-exclude markdown="1">

URI: [sbco:UnitEnum](https://www.sbco.or.jp/ont/UnitEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| celsius | None | Degree Celsius |
| percent | None | Percent |
| ppm | None | Parts per million |




## Slots

| Name | Description |
| ---  | --- |
| [unit](unit.md) | Measurement unit (enum key; symbol can be taken from annotations) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema






## LinkML Source

<details>
```yaml
name: UnitEnum
description: Allowed measurement units
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
permissible_values:
  celsius:
    text: celsius
    description: Degree Celsius
    annotations:
      text:
        tag: text
        value: °C
  percent:
    text: percent
    description: Percent
    annotations:
      text:
        tag: text
        value: '%'
  ppm:
    text: ppm
    description: Parts per million
    annotations:
      text:
        tag: text
        value: ppm

```
</details>

</div>