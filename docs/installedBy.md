

# Slot: installedBy 


_Agent or resource that installed this asset_





URI: [rec:installedBy](https://w3id.org/rec/installedBy)
Alias: installedBy

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
| self | rec:installedBy |
| native | sbco:installedBy |




## LinkML Source

<details>
```yaml
name: installedBy
description: Agent or resource that installed this asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:installedBy
alias: installedBy
domain_of:
- Asset
range: Agent
multivalued: true

```
</details>