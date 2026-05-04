

# Slot: MACAddress 


_MAC address of the asset_





URI: [rec:MACAddress](https://w3id.org/rec/MACAddress)
Alias: MACAddress

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True

* Regex pattern: `^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:MACAddress |
| native | sbco:MACAddress |




## LinkML Source

<details>
```yaml
name: MACAddress
description: MAC address of the asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:MACAddress
alias: MACAddress
domain_of:
- Asset
range: string
multivalued: true
pattern: ^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$

```
</details>