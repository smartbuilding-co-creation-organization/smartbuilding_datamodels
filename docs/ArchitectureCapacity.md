

# Class: ArchitectureCapacity 


_Describes business-relevant capacity measurements typically associated with architected spaces_





URI: [rec:ArchitectureCapacity](https://w3id.org/rec/ArchitectureCapacity)





```mermaid
 classDiagram
    class ArchitectureCapacity
    click ArchitectureCapacity href "../ArchitectureCapacity/"
      Resource <|-- ArchitectureCapacity
        click Resource href "../Resource/"
      
      ArchitectureCapacity : customProperties
        
          
    
        
        
        ArchitectureCapacity --> "*" KeyMapOfStringMapEntry : customProperties
        click KeyMapOfStringMapEntry href "../KeyMapOfStringMapEntry/"
    

        
      ArchitectureCapacity : customTags
        
          
    
        
        
        ArchitectureCapacity --> "*" KeyBoolMapEntry : customTags
        click KeyBoolMapEntry href "../KeyBoolMapEntry/"
    

        
      ArchitectureCapacity : id
        
      ArchitectureCapacity : identifiers
        
          
    
        
        
        ArchitectureCapacity --> "*" KeyStringMapEntry : identifiers
        click KeyStringMapEntry href "../KeyStringMapEntry/"
    

        
      ArchitectureCapacity : name
        
      
```





## Inheritance
* [Resource](Resource.md)
    * **ArchitectureCapacity**



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
| [Architecture](Architecture.md) | [capacity](capacity.md) | range | [ArchitectureCapacity](ArchitectureCapacity.md) |
| [Site](Site.md) | [capacity](capacity.md) | range | [ArchitectureCapacity](ArchitectureCapacity.md) |
| [Building](Building.md) | [capacity](capacity.md) | range | [ArchitectureCapacity](ArchitectureCapacity.md) |
| [Level](Level.md) | [capacity](capacity.md) | range | [ArchitectureCapacity](ArchitectureCapacity.md) |
| [Room](Room.md) | [capacity](capacity.md) | range | [ArchitectureCapacity](ArchitectureCapacity.md) |
| [Zone](Zone.md) | [capacity](capacity.md) | range | [ArchitectureCapacity](ArchitectureCapacity.md) |
| [OutdoorSpace](OutdoorSpace.md) | [capacity](capacity.md) | range | [ArchitectureCapacity](ArchitectureCapacity.md) |







## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | 設計された空間に関連する業務上重要な容量測定 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:ArchitectureCapacity |
| native | sbco:ArchitectureCapacity |
| exact | rec:ArchitectureCapacity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ArchitectureCapacity
annotations:
  description_ja:
    tag: description_ja
    value: 設計された空間に関連する業務上重要な容量測定
description: Describes business-relevant capacity measurements typically associated
  with architected spaces
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:ArchitectureCapacity
is_a: Resource
slots:
- id
- name
- identifiers
- customTags
- customProperties
class_uri: rec:ArchitectureCapacity

```
</details>

### Induced

<details>
```yaml
name: ArchitectureCapacity
annotations:
  description_ja:
    tag: description_ja
    value: 設計された空間に関連する業務上重要な容量測定
description: Describes business-relevant capacity measurements typically associated
  with architected spaces
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:ArchitectureCapacity
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
    owner: ArchitectureCapacity
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
    owner: ArchitectureCapacity
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
    owner: ArchitectureCapacity
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
    owner: ArchitectureCapacity
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
    owner: ArchitectureCapacity
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
class_uri: rec:ArchitectureCapacity

```
</details>