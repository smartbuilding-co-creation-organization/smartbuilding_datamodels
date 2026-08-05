---
search:
  boost: 5.0
---

# Slot: assetTag 


_Asset identification tag_






URI: [rec:assetTag](https://w3id.org/rec/assetTag)
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
| Slot URI | [rec:assetTag](https://w3id.org/rec/assetTag) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:assetTag |
| native | sbco:assetTag |




## LinkML Source

<details markdown="1">
```yaml
name: assetTag
description: Asset identification tag
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:assetTag
domain_of:
- Asset
range: string
multivalued: true

```
</details>