---
search:
  boost: 2.0
---


# Enum: UnitEnum 




_Allowed measurement units. Each permissible value is a canonical key; the `text` annotation carries its display symbol and `legacy_symbols` lists the raw point-list tokens (Japanese/legacy variants included, e.g. from CSV `unit` columns) that normalize to it (#35). This enum intentionally does not accept those raw tokens directly — mapping a raw token to one of these keys is a deliberate, documented normalization step upstream of this vocabulary (see README "sbco:unit 語彙と正規化"), not implicit SHACL coercion, so an unrecognized unit stays a visible validation failure instead of being silently rewritten._




URI: [sbco:UnitEnum](https://www.sbco.or.jp/ont/UnitEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| celsius | None | Degree Celsius (temperature) |
| percent | None | Percent (dimensionless ratio, for example relative humidity or valve/damper p... |
| ppm | None | Parts per million (gas concentration) |
| kilowatt_hour | None | Kilowatt hour (energy) |
| megajoule | None | Megajoule (energy) |
| megajoule_per_hour | None | Megajoule per hour (energy rate) |
| kilowatt | None | Kilowatt (power) |
| ampere | None | Ampere (electric current) |
| cubic_meter | None | Cubic meter (volume) |
| cubic_meter_per_hour | None | Cubic meter per hour (volumetric flow) |
| degree | None | Degree (angle) |
| watt_per_square_meter | None | Watt per square meter (irradiance) |
| meter_per_second | None | Meter per second (speed, for example wind or air velocity) |
| millimeter_per_hour | None | Millimeter per hour (precipitation rate) |




## Slots

| Name | Description |
| ---  | --- |
| [unit](unit.md) | Measurement unit (enum key; symbol can be taken from annotations) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema






## LinkML Source

<details markdown="1">
```yaml
name: UnitEnum
description: Allowed measurement units. Each permissible value is a canonical key;
  the `text` annotation carries its display symbol and `legacy_symbols` lists the
  raw point-list tokens (Japanese/legacy variants included, e.g. from CSV `unit` columns)
  that normalize to it (#35). This enum intentionally does not accept those raw tokens
  directly — mapping a raw token to one of these keys is a deliberate, documented
  normalization step upstream of this vocabulary (see README "sbco:unit 語彙と正規化"),
  not implicit SHACL coercion, so an unrecognized unit stays a visible validation
  failure instead of being silently rewritten.
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
permissible_values:
  celsius:
    text: celsius
    description: Degree Celsius (temperature)
    annotations:
      text:
        tag: text
        value: °C
      legacy_symbols:
        tag: legacy_symbols
        value: ℃, °C, C
  percent:
    text: percent
    description: Percent (dimensionless ratio, for example relative humidity or valve/damper
      position)
    annotations:
      text:
        tag: text
        value: '%'
      legacy_symbols:
        tag: legacy_symbols
        value: '%, ％, ％RH, %RH'
  ppm:
    text: ppm
    description: Parts per million (gas concentration)
    annotations:
      text:
        tag: text
        value: ppm
  kilowatt_hour:
    text: kilowatt_hour
    description: Kilowatt hour (energy)
    annotations:
      text:
        tag: text
        value: kWh
      legacy_symbols:
        tag: legacy_symbols
        value: KWH, kWh, kwh
  megajoule:
    text: megajoule
    description: Megajoule (energy)
    annotations:
      text:
        tag: text
        value: MJ
      legacy_symbols:
        tag: legacy_symbols
        value: MJ
  megajoule_per_hour:
    text: megajoule_per_hour
    description: Megajoule per hour (energy rate)
    annotations:
      text:
        tag: text
        value: MJ/h
      legacy_symbols:
        tag: legacy_symbols
        value: MJ/h, MJ/H
  kilowatt:
    text: kilowatt
    description: Kilowatt (power)
    annotations:
      text:
        tag: text
        value: kW
      legacy_symbols:
        tag: legacy_symbols
        value: Kw, KW, kw
  ampere:
    text: ampere
    description: Ampere (electric current)
    annotations:
      text:
        tag: text
        value: A
      legacy_symbols:
        tag: legacy_symbols
        value: A
  cubic_meter:
    text: cubic_meter
    description: Cubic meter (volume)
    annotations:
      text:
        tag: text
        value: m³
      legacy_symbols:
        tag: legacy_symbols
        value: m3, m^3
  cubic_meter_per_hour:
    text: cubic_meter_per_hour
    description: Cubic meter per hour (volumetric flow)
    annotations:
      text:
        tag: text
        value: m³/h
      legacy_symbols:
        tag: legacy_symbols
        value: m3/h, m^3/h
  degree:
    text: degree
    description: Degree (angle)
    annotations:
      text:
        tag: text
        value: °
      legacy_symbols:
        tag: legacy_symbols
        value: °, deg
  watt_per_square_meter:
    text: watt_per_square_meter
    description: Watt per square meter (irradiance)
    annotations:
      text:
        tag: text
        value: W/m²
      legacy_symbols:
        tag: legacy_symbols
        value: W/m2, W/m^2
  meter_per_second:
    text: meter_per_second
    description: Meter per second (speed, for example wind or air velocity)
    annotations:
      text:
        tag: text
        value: m/s
      legacy_symbols:
        tag: legacy_symbols
        value: m/s
  millimeter_per_hour:
    text: millimeter_per_hour
    description: Millimeter per hour (precipitation rate)
    annotations:
      text:
        tag: text
        value: mm/h
      legacy_symbols:
        tag: legacy_symbols
        value: mm/h

```
</details>
