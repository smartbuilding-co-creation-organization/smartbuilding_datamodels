---
search:
  boost: 5.0
---

# Slot: IPAddress 


_IP address of the asset_



<div data-search-exclude markdown="1">



URI: [rec:IPAddress](https://w3id.org/rec/IPAddress)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Asset](Asset.md) |
| Slot URI | [rec:IPAddress](https://w3id.org/rec/IPAddress) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^((25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(25[0-5]|2[0-4]\d|1?\d?\d)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:IPAddress |
| native | sbco:IPAddress |




## LinkML Source

<details>
```yaml
name: IPAddress
description: IP address of the asset
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:IPAddress
domain_of:
- Asset
range: string
multivalued: true
pattern: ^((25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(25[0-5]|2[0-4]\d|1?\d?\d)$

```
</details></div>