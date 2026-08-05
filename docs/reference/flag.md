---
search:
  boost: 5.0
---

# Slot: flag 


_Boolean flag value_






URI: [sbco:flag](https://www.sbco.or.jp/ont/flag)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KeyBoolMapEntry](KeyBoolMapEntry.md) | One entry in a map from strings to booleans |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [KeyBoolMapEntry](KeyBoolMapEntry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:flag |
| native | sbco:flag |




## LinkML Source

<details markdown="1">
```yaml
name: flag
description: Boolean flag value
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- KeyBoolMapEntry
range: boolean
required: true

```
</details>