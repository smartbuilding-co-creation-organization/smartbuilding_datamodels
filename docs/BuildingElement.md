

# Class: BuildingElement 


_A part of the building structure_





URI: [rec:BuildingElement](https://w3id.org/rec/BuildingElement)





```mermaid
 classDiagram
    class BuildingElement
    click BuildingElement href "../BuildingElement/"
      Resource <|-- BuildingElement
        click Resource href "../Resource/"
      
      BuildingElement : customProperties
        
          
    
        
        
        BuildingElement --> "*" KeyMapOfStringMapEntry : customProperties
        click KeyMapOfStringMapEntry href "../KeyMapOfStringMapEntry/"
    

        
      BuildingElement : customTags
        
          
    
        
        
        BuildingElement --> "*" KeyBoolMapEntry : customTags
        click KeyBoolMapEntry href "../KeyBoolMapEntry/"
    

        
      BuildingElement : id
        
      BuildingElement : identifiers
        
          
    
        
        
        BuildingElement --> "*" KeyStringMapEntry : identifiers
        click KeyStringMapEntry href "../KeyStringMapEntry/"
    

        
      BuildingElement : name
        
      
```





## Inheritance
* [Resource](Resource.md)
    * **BuildingElement**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | Unique identifier within the schema | direct |
| [name](name.md) | 1 <br/> [String](String.md) | Machine or Human-readable name | direct |
| [identifiers](identifiers.md) | * <br/> [KeyStringMapEntry](KeyStringMapEntry.md) | map(string -> string) | direct |
| [customTags](customTags.md) | * <br/> [KeyBoolMapEntry](KeyBoolMapEntry.md) | map(string -> boolean) | direct |
| [customProperties](customProperties.md) | * <br/> [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) | map(string -> map(string -> string)) | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Architecture](Architecture.md) | [adjacentElement](adjacentElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Architecture](Architecture.md) | [containsElement](containsElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Architecture](Architecture.md) | [intersectingElement](intersectingElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Site](Site.md) | [adjacentElement](adjacentElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Site](Site.md) | [containsElement](containsElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Site](Site.md) | [intersectingElement](intersectingElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Building](Building.md) | [adjacentElement](adjacentElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Building](Building.md) | [containsElement](containsElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Building](Building.md) | [intersectingElement](intersectingElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Level](Level.md) | [adjacentElement](adjacentElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Level](Level.md) | [containsElement](containsElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Level](Level.md) | [intersectingElement](intersectingElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Room](Room.md) | [adjacentElement](adjacentElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Room](Room.md) | [containsElement](containsElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Room](Room.md) | [intersectingElement](intersectingElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Zone](Zone.md) | [adjacentElement](adjacentElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Zone](Zone.md) | [containsElement](containsElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Zone](Zone.md) | [intersectingElement](intersectingElement.md) | range | [BuildingElement](BuildingElement.md) |
| [OutdoorSpace](OutdoorSpace.md) | [adjacentElement](adjacentElement.md) | range | [BuildingElement](BuildingElement.md) |
| [OutdoorSpace](OutdoorSpace.md) | [containsElement](containsElement.md) | range | [BuildingElement](BuildingElement.md) |
| [OutdoorSpace](OutdoorSpace.md) | [intersectingElement](intersectingElement.md) | range | [BuildingElement](BuildingElement.md) |
| [Asset](Asset.md) | [mountedOn](mountedOn.md) | range | [BuildingElement](BuildingElement.md) |
| [Equipment](Equipment.md) | [mountedOn](mountedOn.md) | range | [BuildingElement](BuildingElement.md) |
| [EquipmentExt](EquipmentExt.md) | [mountedOn](mountedOn.md) | range | [BuildingElement](BuildingElement.md) |







## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | 建物構造の一部 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:BuildingElement |
| native | sbco:BuildingElement |
| exact | rec:BuildingElement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BuildingElement
annotations:
  description_ja:
    tag: description_ja
    value: 建物構造の一部
description: A part of the building structure
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:BuildingElement
is_a: Resource
slots:
- id
- name
- identifiers
- customTags
- customProperties
class_uri: rec:BuildingElement

```
</details>

### Induced

<details>
```yaml
name: BuildingElement
annotations:
  description_ja:
    tag: description_ja
    value: 建物構造の一部
description: A part of the building structure
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:BuildingElement
is_a: Resource
attributes:
  id:
    name: id
    annotations:
      description_ja:
        tag: description_ja
        value: スキーマ内の一意識別子。文字で開始し、DTMI形式もサポート。
      example:
        tag: example
        value: dtmi:example:Building:1
    description: Unique identifier within the schema. Must start with a letter and
      contain only letters, digits, underscores, hyphens, colons, semicolons, or periods.
      DTMI is one acceptable example.
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    identifier: true
    alias: id
    owner: BuildingElement
    domain_of:
    - Space
    - Asset
    - Point
    - Agent
    - Organization
    - BuildingElement
    - ArchitectureArea
    - ArchitectureCapacity
    range: string
    required: true
  name:
    name: name
    description: Machine or Human-readable name
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:name
    alias: name
    owner: BuildingElement
    domain_of:
    - Space
    - Asset
    - Point
    - Information
    - PostalAddress
    - Agent
    - Organization
    - BuildingElement
    - ArchitectureArea
    - ArchitectureCapacity
    range: string
    required: true
  identifiers:
    name: identifiers
    description: map(string -> string)
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:identifiers
    alias: identifiers
    owner: BuildingElement
    domain_of:
    - Space
    - Asset
    - Point
    - Information
    - PostalAddress
    - Agent
    - Organization
    - BuildingElement
    - ArchitectureArea
    - ArchitectureCapacity
    range: KeyStringMapEntry
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  customTags:
    name: customTags
    description: map(string -> boolean)
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:customTags
    alias: customTags
    owner: BuildingElement
    domain_of:
    - Space
    - Asset
    - Point
    - Information
    - PostalAddress
    - Agent
    - Organization
    - BuildingElement
    - ArchitectureArea
    - ArchitectureCapacity
    range: KeyBoolMapEntry
    multivalued: true
    inlined: true
    inlined_as_list: true
  customProperties:
    name: customProperties
    description: map(string -> map(string -> string))
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:customProperties
    alias: customProperties
    owner: BuildingElement
    domain_of:
    - Space
    - Asset
    - Point
    - Information
    - PostalAddress
    - Agent
    - Organization
    - BuildingElement
    - ArchitectureArea
    - ArchitectureCapacity
    range: KeyMapOfStringMapEntry
    multivalued: true
    inlined: true
    inlined_as_list: true
class_uri: rec:BuildingElement

```
</details>