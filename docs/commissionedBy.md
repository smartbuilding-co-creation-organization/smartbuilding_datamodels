

# Slot: commissionedBy 


_Agent or resource that commissioned this asset_





URI: [rec:commissionedBy](https://w3id.org/rec/commissionedBy)
Alias: commissionedBy

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
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
| self | rec:commissionedBy |
| native | sbco:commissionedBy |




## LinkML Source

<details>
```yaml
name: commissionedBy
description: Agent or resource that commissioned this asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:commissionedBy
alias: commissionedBy
domain_of:
- Asset
range: Agent
multivalued: true

```
</details>