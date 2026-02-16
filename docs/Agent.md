

# Class: Agent 


_An entity that can act or be acted upon_





URI: [rec:Agent](https://w3id.org/rec/Agent)





```mermaid
 classDiagram
    class Agent
    click Agent href "../Agent/"
      Resource <|-- Agent
        click Resource href "../Resource/"
      

      Agent <|-- Organization
        click Organization href "../Organization/"
      

      Agent : customProperties
        
          
    
        
        
        Agent --> "*" KeyMapOfStringMapEntry : customProperties
        click KeyMapOfStringMapEntry href "../KeyMapOfStringMapEntry/"
    

        
      Agent : customTags
        
          
    
        
        
        Agent --> "*" KeyBoolMapEntry : customTags
        click KeyBoolMapEntry href "../KeyBoolMapEntry/"
    

        
      Agent : id
        
      Agent : identifiers
        
          
    
        
        
        Agent --> "*" KeyStringMapEntry : identifiers
        click KeyStringMapEntry href "../KeyStringMapEntry/"
    

        
      Agent : memberOf
        
          
    
        
        
        Agent --> "*" Organization : memberOf
        click Organization href "../Organization/"
    

        
      Agent : name
        
      Agent : owns
        
          
    
        
        
        Agent --> "*" Resource : owns
        click Resource href "../Resource/"
    

        
      
```





## Inheritance
* [Resource](Resource.md)
    * **Agent**
        * [Organization](Organization.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | Unique identifier within the schema | direct |
| [name](name.md) | 1 <br/> [String](String.md) | Machine or Human-readable name | direct |
| [identifiers](identifiers.md) | * <br/> [KeyStringMapEntry](KeyStringMapEntry.md) | map(string -> string) | direct |
| [customTags](customTags.md) | * <br/> [KeyBoolMapEntry](KeyBoolMapEntry.md) | map(string -> boolean) | direct |
| [customProperties](customProperties.md) | * <br/> [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) | map(string -> map(string -> string)) | direct |
| [memberOf](memberOf.md) | * <br/> [Organization](Organization.md) | Indicates membership in an organization | direct |
| [owns](owns.md) | * <br/> [Resource](Resource.md) |  Indicates ownership of some thing, e | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Architecture](Architecture.md) | [architectedBy](architectedBy.md) | range | [Agent](Agent.md) |
| [Architecture](Architecture.md) | [constructedBy](constructedBy.md) | range | [Agent](Agent.md) |
| [Architecture](Architecture.md) | [operatedBy](operatedBy.md) | range | [Agent](Agent.md) |
| [Architecture](Architecture.md) | [ownedBy](ownedBy.md) | range | [Agent](Agent.md) |
| [Site](Site.md) | [architectedBy](architectedBy.md) | range | [Agent](Agent.md) |
| [Site](Site.md) | [constructedBy](constructedBy.md) | range | [Agent](Agent.md) |
| [Site](Site.md) | [operatedBy](operatedBy.md) | range | [Agent](Agent.md) |
| [Site](Site.md) | [ownedBy](ownedBy.md) | range | [Agent](Agent.md) |
| [Building](Building.md) | [architectedBy](architectedBy.md) | range | [Agent](Agent.md) |
| [Building](Building.md) | [constructedBy](constructedBy.md) | range | [Agent](Agent.md) |
| [Building](Building.md) | [operatedBy](operatedBy.md) | range | [Agent](Agent.md) |
| [Building](Building.md) | [ownedBy](ownedBy.md) | range | [Agent](Agent.md) |
| [Level](Level.md) | [architectedBy](architectedBy.md) | range | [Agent](Agent.md) |
| [Level](Level.md) | [constructedBy](constructedBy.md) | range | [Agent](Agent.md) |
| [Level](Level.md) | [operatedBy](operatedBy.md) | range | [Agent](Agent.md) |
| [Level](Level.md) | [ownedBy](ownedBy.md) | range | [Agent](Agent.md) |
| [Room](Room.md) | [architectedBy](architectedBy.md) | range | [Agent](Agent.md) |
| [Room](Room.md) | [constructedBy](constructedBy.md) | range | [Agent](Agent.md) |
| [Room](Room.md) | [operatedBy](operatedBy.md) | range | [Agent](Agent.md) |
| [Room](Room.md) | [ownedBy](ownedBy.md) | range | [Agent](Agent.md) |
| [Zone](Zone.md) | [architectedBy](architectedBy.md) | range | [Agent](Agent.md) |
| [Zone](Zone.md) | [constructedBy](constructedBy.md) | range | [Agent](Agent.md) |
| [Zone](Zone.md) | [operatedBy](operatedBy.md) | range | [Agent](Agent.md) |
| [Zone](Zone.md) | [ownedBy](ownedBy.md) | range | [Agent](Agent.md) |
| [OutdoorSpace](OutdoorSpace.md) | [architectedBy](architectedBy.md) | range | [Agent](Agent.md) |
| [OutdoorSpace](OutdoorSpace.md) | [constructedBy](constructedBy.md) | range | [Agent](Agent.md) |
| [OutdoorSpace](OutdoorSpace.md) | [operatedBy](operatedBy.md) | range | [Agent](Agent.md) |
| [OutdoorSpace](OutdoorSpace.md) | [ownedBy](ownedBy.md) | range | [Agent](Agent.md) |
| [Asset](Asset.md) | [commissionedBy](commissionedBy.md) | range | [Agent](Agent.md) |
| [Asset](Asset.md) | [installedBy](installedBy.md) | range | [Agent](Agent.md) |
| [Asset](Asset.md) | [manufacturedBy](manufacturedBy.md) | range | [Agent](Agent.md) |
| [Asset](Asset.md) | [servicedBy](servicedBy.md) | range | [Agent](Agent.md) |
| [Equipment](Equipment.md) | [commissionedBy](commissionedBy.md) | range | [Agent](Agent.md) |
| [Equipment](Equipment.md) | [installedBy](installedBy.md) | range | [Agent](Agent.md) |
| [Equipment](Equipment.md) | [manufacturedBy](manufacturedBy.md) | range | [Agent](Agent.md) |
| [Equipment](Equipment.md) | [servicedBy](servicedBy.md) | range | [Agent](Agent.md) |
| [EquipmentExt](EquipmentExt.md) | [commissionedBy](commissionedBy.md) | range | [Agent](Agent.md) |
| [EquipmentExt](EquipmentExt.md) | [installedBy](installedBy.md) | range | [Agent](Agent.md) |
| [EquipmentExt](EquipmentExt.md) | [manufacturedBy](manufacturedBy.md) | range | [Agent](Agent.md) |
| [EquipmentExt](EquipmentExt.md) | [servicedBy](servicedBy.md) | range | [Agent](Agent.md) |







## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | 行動することができる、または行動される主体 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:Agent |
| native | sbco:Agent |
| exact | rec:Agent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Agent
annotations:
  description_ja:
    tag: description_ja
    value: 行動することができる、または行動される主体
description: An entity that can act or be acted upon
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:Agent
is_a: Resource
slots:
- id
- name
- identifiers
- customTags
- customProperties
- memberOf
- owns
class_uri: rec:Agent

```
</details>

### Induced

<details>
```yaml
name: Agent
annotations:
  description_ja:
    tag: description_ja
    value: 行動することができる、または行動される主体
description: An entity that can act or be acted upon
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
  memberOf:
    name: memberOf
    description: Indicates membership in an organization. Note that componency (e.g.,
      departments of a corporation) are expressed using the more generic Organization.isPartOf
      property.
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:memberOf
    alias: memberOf
    owner: Agent
    domain_of:
    - Agent
    range: Organization
    multivalued: true
  owns:
    name: owns
    description: ' Indicates ownership of some thing, e.g., a building, an asset,
      an organization, etc.'
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:owns
    alias: owns
    owner: Agent
    domain_of:
    - Agent
    range: Resource
    multivalued: true
class_uri: rec:Agent

```
</details>