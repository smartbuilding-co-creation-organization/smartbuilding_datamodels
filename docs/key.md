---
search:
  boost: 5.0
---

# Slot: key 


_Key of the map entry_



<div data-search-exclude markdown="1">



URI: [sbco:key](https://www.sbco.or.jp/ont/key)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KeyStringMapEntry](KeyStringMapEntry.md) | One entry in a map from strings to strings |  yes  |
| [KeyBoolMapEntry](KeyBoolMapEntry.md) | One entry in a map from strings to booleans |  yes  |
| [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) | One entry in a map from strings to string-to-string maps |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [KeyStringMapEntry](KeyStringMapEntry.md), [KeyBoolMapEntry](KeyBoolMapEntry.md), [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:key |
| native | sbco:key |




## LinkML Source

<details>
```yaml
name: key
description: Key of the map entry
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
domain_of:
- KeyStringMapEntry
- KeyBoolMapEntry
- KeyMapOfStringMapEntry
range: string

```
</details></div>