

# Slot: manufacturedBy 


_Agent or resource that manufactured this asset_





URI: [rec:manufacturedBy](https://w3id.org/rec/manufacturedBy)
Alias: manufacturedBy

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

* Range: [Agent](Agent.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:manufacturedBy |
| native | sbco:manufacturedBy |




## LinkML Source

<details>
```yaml
name: manufacturedBy
description: Agent or resource that manufactured this asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:manufacturedBy
alias: manufacturedBy
domain_of:
- Asset
range: Agent
multivalued: true

```
</details>