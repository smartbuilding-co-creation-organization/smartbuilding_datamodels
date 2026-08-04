

# Slot: key 


_Key of the map entry_





URI: [sbco:key](https://www.sbco.or.jp/ont/key)
Alias: key

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KeyStringMapEntry](KeyStringMapEntry.md) | One entry in a map from strings to strings |  yes  |
| [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) | One entry in a map from strings to string-to-string maps |  yes  |
| [KeyBoolMapEntry](KeyBoolMapEntry.md) | One entry in a map from strings to booleans |  yes  |






## Properties

* Range: [String](String.md)




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
alias: key
domain_of:
- KeyStringMapEntry
- KeyBoolMapEntry
- KeyMapOfStringMapEntry
range: string

```
</details>