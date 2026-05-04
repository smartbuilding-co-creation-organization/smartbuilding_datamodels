

# Slot: assetTag 


_Asset identification tag_





URI: [rec:assetTag](https://w3id.org/rec/assetTag)
Alias: assetTag

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




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:assetTag |
| native | sbco:assetTag |




## LinkML Source

<details>
```yaml
name: assetTag
description: Asset identification tag
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:assetTag
alias: assetTag
domain_of:
- Asset
range: string
multivalued: true

```
</details>