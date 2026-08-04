---
search:
  boost: 5.0
---

# Slot: installationDate 


_Date when the asset was installed_



<div data-search-exclude markdown="1">



URI: [rec:installationDate](https://w3id.org/rec/installationDate)
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
| Range | [Date](Date.md) |
| Domain Of | [Asset](Asset.md) |
| Slot URI | [rec:installationDate](https://w3id.org/rec/installationDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:installationDate |
| native | sbco:installationDate |




## LinkML Source

<details>
```yaml
name: installationDate
description: Date when the asset was installed
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:installationDate
domain_of:
- Asset
range: date

```
</details></div>