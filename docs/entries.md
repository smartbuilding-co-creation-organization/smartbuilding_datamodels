

# Slot: entries 


_Nested map entries_





URI: [sbco:entries](https://www.sbco.or.jp/ont/entries)
Alias: entries

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) | One entry in a map from strings to string-to-string maps |  yes  |






## Properties

* Range: [KeyStringMapEntry](KeyStringMapEntry.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:entries |
| native | sbco:entries |




## LinkML Source

<details>
```yaml
name: entries
description: Nested map entries
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
alias: entries
domain_of:
- KeyMapOfStringMapEntry
range: KeyStringMapEntry
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>