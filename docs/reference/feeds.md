---
search:
  boost: 5.0
---

# Slot: feeds 


_Equipment or system that this equipment feeds_






URI: [brick:feeds](https://brickschema.org/schema/Brick#feeds)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Resource](Resource.md) |
| Domain Of | [Equipment](Equipment.md) |
| Slot URI | [brick:feeds](https://brickschema.org/schema/Brick#feeds) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| substance | SubstanceEnum |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brick:feeds |
| native | sbco:feeds |




## LinkML Source

<details markdown="1">
```yaml
name: feeds
annotations:
  substance:
    tag: substance
    value: SubstanceEnum
description: Equipment or system that this equipment feeds
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: brick:feeds
domain_of:
- Equipment
range: Resource
multivalued: true

```
</details>