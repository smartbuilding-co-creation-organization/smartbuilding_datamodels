

# Slot: turnoverDate 


_Date when the asset was turned over_





URI: [rec:turnoverDate](https://w3id.org/rec/turnoverDate)
Alias: turnoverDate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

* Range: [Date](Date.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:turnoverDate |
| native | sbco:turnoverDate |




## LinkML Source

<details>
```yaml
name: turnoverDate
description: Date when the asset was turned over
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:turnoverDate
alias: turnoverDate
domain_of:
- Asset
range: date

```
</details>