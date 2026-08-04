

# Slot: feeds 


_Equipment or system that this equipment feeds_





URI: [brick:feeds](https://brickschema.org/schema/Brick#feeds)
Alias: feeds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

* Range: [Resource](Resource.md)

* Multivalued: True




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

<details>
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
alias: feeds
domain_of:
- Equipment
range: Resource
multivalued: true

```
</details>