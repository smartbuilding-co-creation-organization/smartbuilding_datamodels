

# Slot: serialNumber 


_Serial number of the asset_





URI: [rec:serialNumber](https://w3id.org/rec/serialNumber)
Alias: serialNumber

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:serialNumber |
| native | sbco:serialNumber |




## LinkML Source

<details>
```yaml
name: serialNumber
description: Serial number of the asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:serialNumber
alias: serialNumber
domain_of:
- Asset
range: string

```
</details>