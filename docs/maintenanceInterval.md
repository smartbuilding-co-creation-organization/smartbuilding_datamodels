---
search:
  boost: 5.0
---

# Slot: maintenanceInterval 


_Maintenance interval duration_



<div data-search-exclude markdown="1">



URI: [rec:maintenanceInterval](https://w3id.org/rec/maintenanceInterval)
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
| Range | [DurationString](DurationString.md) |
| Domain Of | [Asset](Asset.md) |
| Slot URI | [rec:maintenanceInterval](https://w3id.org/rec/maintenanceInterval) |

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
| self | rec:maintenanceInterval |
| native | sbco:maintenanceInterval |




## LinkML Source

<details>
```yaml
name: maintenanceInterval
description: Maintenance interval duration
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:maintenanceInterval
domain_of:
- Asset
range: DurationString
multivalued: true

```
</details></div>