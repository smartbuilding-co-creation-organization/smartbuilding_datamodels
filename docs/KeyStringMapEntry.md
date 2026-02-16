

# Class: KeyStringMapEntry 


_map(string -> string) の1エントリ_





URI: [sbco:KeyStringMapEntry](https://www.sbco.or.jp/ont/KeyStringMapEntry)





```mermaid
 classDiagram
    class KeyStringMapEntry
    click KeyStringMapEntry href "../KeyStringMapEntry/"
      KeyStringMapEntry : key
        
      KeyStringMapEntry : value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [key](key.md) | 1 <br/> [String](String.md) | Key of the map entry | direct |
| [value](value.md) | 1 <br/> [String](String.md) | Value of the map entry | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Space](Space.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Architecture](Architecture.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Site](Site.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Building](Building.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Level](Level.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Room](Room.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Zone](Zone.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [OutdoorSpace](OutdoorSpace.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Asset](Asset.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Equipment](Equipment.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [EquipmentExt](EquipmentExt.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Point](Point.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [PointExt](PointExt.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) | [entries](entries.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Information](Information.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Document](Document.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Image](Image.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Media](Media.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Schema](Schema.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [PostalAddress](PostalAddress.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Geometry](Geometry.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Georeference](Georeference.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Agent](Agent.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [Organization](Organization.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [BuildingElement](BuildingElement.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [ArchitectureArea](ArchitectureArea.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |
| [ArchitectureCapacity](ArchitectureCapacity.md) | [identifiers](identifiers.md) | range | [KeyStringMapEntry](KeyStringMapEntry.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:KeyStringMapEntry |
| native | sbco:KeyStringMapEntry |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: KeyStringMapEntry
description: map(string -> string) の1エントリ
from_schema: https://www.sbco.or.jp/ont/schema
slots:
- key
- value
slot_usage:
  key:
    name: key
    required: true
  value:
    name: value
    required: true

```
</details>

### Induced

<details>
```yaml
name: KeyStringMapEntry
description: map(string -> string) の1エントリ
from_schema: https://www.sbco.or.jp/ont/schema
slot_usage:
  key:
    name: key
    required: true
  value:
    name: value
    required: true
attributes:
  key:
    name: key
    description: Key of the map entry
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    alias: key
    owner: KeyStringMapEntry
    domain_of:
    - KeyStringMapEntry
    - KeyBoolMapEntry
    - KeyMapOfStringMapEntry
    range: string
    required: true
  value:
    name: value
    description: Value of the map entry
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    alias: value
    owner: KeyStringMapEntry
    domain_of:
    - KeyStringMapEntry
    range: string
    required: true

```
</details>