

# Slot: servicedBy 


_Agent or resource that services this asset_





URI: [rec:servicedBy](https://w3id.org/rec/servicedBy)
Alias: servicedBy

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
| self | rec:servicedBy |
| native | sbco:servicedBy |




## LinkML Source

<details>
```yaml
name: servicedBy
description: Agent or resource that services this asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:servicedBy
alias: servicedBy
domain_of:
- Asset
range: Agent
multivalued: true

```
</details>