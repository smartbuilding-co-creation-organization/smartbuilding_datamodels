

# Class: Level 


_A building storey. Levels can also be treated as a kind of space._





URI: [rec:Level](https://w3id.org/rec/Level)





```mermaid
 classDiagram
    class Level
    click Level href "../Level/"
      Architecture <|-- Level
        click Architecture href "../Architecture/"
      
      Level : address
        
          
    
        
        
        Level --> "*" PostalAddress : address
        click PostalAddress href "../PostalAddress/"
    

        
      Level : adjacentElement
        
          
    
        
        
        Level --> "*" BuildingElement : adjacentElement
        click BuildingElement href "../BuildingElement/"
    

        
      Level : architectedBy
        
          
    
        
        
        Level --> "*" Agent : architectedBy
        click Agent href "../Agent/"
    

        
      Level : area
        
          
    
        
        
        Level --> "0..1" ArchitectureArea : area
        click ArchitectureArea href "../ArchitectureArea/"
    

        
      Level : capacity
        
          
    
        
        
        Level --> "0..1" ArchitectureCapacity : capacity
        click ArchitectureCapacity href "../ArchitectureCapacity/"
    

        
      Level : constructedBy
        
          
    
        
        
        Level --> "*" Agent : constructedBy
        click Agent href "../Agent/"
    

        
      Level : containsElement
        
          
    
        
        
        Level --> "*" BuildingElement : containsElement
        click BuildingElement href "../BuildingElement/"
    

        
      Level : customProperties
        
          
    
        
        
        Level --> "*" KeyMapOfStringMapEntry : customProperties
        click KeyMapOfStringMapEntry href "../KeyMapOfStringMapEntry/"
    

        
      Level : customTags
        
          
    
        
        
        Level --> "*" KeyBoolMapEntry : customTags
        click KeyBoolMapEntry href "../KeyBoolMapEntry/"
    

        
      Level : description
        
      Level : documentation
        
          
    
        
        
        Level --> "*" Document : documentation
        click Document href "../Document/"
    

        
      Level : geometry
        
          
    
        
        
        Level --> "0..1" Geometry : geometry
        click Geometry href "../Geometry/"
    

        
      Level : georeference
        
          
    
        
        
        Level --> "0..1" Georeference : georeference
        click Georeference href "../Georeference/"
    

        
      Level : hasPart
        
      Level : hasPoint
        
          
    
        
        
        Level --> "*" Point : hasPoint
        click Point href "../Point/"
    

        
      Level : id
        
      Level : identifiers
        
          
    
        
        
        Level --> "*" KeyStringMapEntry : identifiers
        click KeyStringMapEntry href "../KeyStringMapEntry/"
    

        
      Level : intersectingElement
        
          
    
        
        
        Level --> "*" BuildingElement : intersectingElement
        click BuildingElement href "../BuildingElement/"
    

        
      Level : isFedBy
        
          
    
        
        
        Level --> "*" Resource : isFedBy
        click Resource href "../Resource/"
    

        
      Level : isLocationOf
        
          
    
        
        
        Level --> "*" EquipmentExt : isLocationOf
        click EquipmentExt href "../EquipmentExt/"
    

        
      Level : isPartOf
        
      Level : levelNumber
        
      Level : name
        
      Level : operatedBy
        
          
    
        
        
        Level --> "*" Agent : operatedBy
        click Agent href "../Agent/"
    

        
      Level : ownedBy
        
          
    
        
        
        Level --> "*" Agent : ownedBy
        click Agent href "../Agent/"
    

        
      
```





## Inheritance
* [Space](Space.md)
    * [Architecture](Architecture.md)
        * **Level**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [levelNumber](levelNumber.md) | 0..1 <br/> [Integer](Integer.md) | Floor or level number within a building | direct |
| [area](area.md) | 0..1 <br/> [ArchitectureArea](ArchitectureArea.md) | Area of the architecture | [Architecture](Architecture.md) |
| [capacity](capacity.md) | 0..1 <br/> [ArchitectureCapacity](ArchitectureCapacity.md) | Capacity of the architecture | [Architecture](Architecture.md) |
| [address](address.md) | * <br/> [PostalAddress](PostalAddress.md) | Address of the architecture | [Architecture](Architecture.md) |
| [adjacentElement](adjacentElement.md) | * <br/> [BuildingElement](BuildingElement.md) | Building element adjacent to this architecture | [Architecture](Architecture.md) |
| [architectedBy](architectedBy.md) | * <br/> [Agent](Agent.md) | Agent or resource that architected this structure | [Architecture](Architecture.md) |
| [constructedBy](constructedBy.md) | * <br/> [Agent](Agent.md) | Agent or resource that constructed this architecture | [Architecture](Architecture.md) |
| [containsElement](containsElement.md) | * <br/> [BuildingElement](BuildingElement.md) | Building element contained within this architecture | [Architecture](Architecture.md) |
| [documentation](documentation.md) | * <br/> [Document](Document.md) | Documentation related to this asset | [Architecture](Architecture.md) |
| [hasPoint](hasPoint.md) | * <br/> [Point](Point.md)&nbsp;or&nbsp;<br />[Point](Point.md)&nbsp;or&nbsp;<br />[PointExt](PointExt.md) | Point associated with this architecture | [Architecture](Architecture.md) |
| [intersectingElement](intersectingElement.md) | * <br/> [BuildingElement](BuildingElement.md) | Building element intersecting with this architecture | [Architecture](Architecture.md) |
| [isFedBy](isFedBy.md) | * <br/> [Resource](Resource.md) | Resource that feeds this architecture | [Architecture](Architecture.md) |
| [operatedBy](operatedBy.md) | * <br/> [Agent](Agent.md) | Agent or resource that operates this architecture | [Architecture](Architecture.md) |
| [ownedBy](ownedBy.md) | * <br/> [Agent](Agent.md) | Agent or resource that owns this architecture | [Architecture](Architecture.md) |
| [id](id.md) | 1 <br/> [String](String.md) | Unique identifier within the schema | [Space](Space.md) |
| [geometry](geometry.md) | 0..1 <br/> [Geometry](Geometry.md) | Polygon representing the spatial extent of this Space | [Space](Space.md) |
| [georeference](georeference.md) | 0..1 <br/> [Georeference](Georeference.md) | A georeference creates a relationship between the local coordinate system use... | [Space](Space.md) |
| [hasPart](hasPart.md) | * <br/> [Any](Any.md)&nbsp;or&nbsp;<br />[Space](Space.md)&nbsp;or&nbsp;<br />[Site](Site.md)&nbsp;or&nbsp;<br />[Building](Building.md)&nbsp;or&nbsp;<br />[Level](Level.md)&nbsp;or&nbsp;<br />[Room](Room.md)&nbsp;or&nbsp;<br />[Zone](Zone.md)&nbsp;or&nbsp;<br />[OutdoorSpace](OutdoorSpace.md) | The subject is composed in part of the entity given by the object | [Space](Space.md) |
| [isLocationOf](isLocationOf.md) | * <br/> [EquipmentExt](EquipmentExt.md) | Subject is the physical location encapsulating the object | [Space](Space.md) |
| [isPartOf](isPartOf.md) | 0..1 <br/> [Any](Any.md)&nbsp;or&nbsp;<br />[Space](Space.md)&nbsp;or&nbsp;<br />[Site](Site.md)&nbsp;or&nbsp;<br />[Building](Building.md)&nbsp;or&nbsp;<br />[Level](Level.md)&nbsp;or&nbsp;<br />[Room](Room.md)&nbsp;or&nbsp;<br />[Zone](Zone.md)&nbsp;or&nbsp;<br />[OutdoorSpace](OutdoorSpace.md) |  | [Space](Space.md) |
| [customProperties](customProperties.md) | * <br/> [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) | map(string -> map(string -> string)) | [Space](Space.md) |
| [customTags](customTags.md) | * <br/> [KeyBoolMapEntry](KeyBoolMapEntry.md) | map(string -> boolean) | [Space](Space.md) |
| [identifiers](identifiers.md) | * <br/> [KeyStringMapEntry](KeyStringMapEntry.md) | map(string -> string) | [Space](Space.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Machine or Human-readable name | [Space](Space.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the resource | [Space](Space.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Space](Space.md) | [hasPart](hasPart.md) | any_of[range] | [Level](Level.md) |
| [Space](Space.md) | [isPartOf](isPartOf.md) | any_of[range] | [Level](Level.md) |
| [Architecture](Architecture.md) | [hasPart](hasPart.md) | any_of[range] | [Level](Level.md) |
| [Architecture](Architecture.md) | [isPartOf](isPartOf.md) | any_of[range] | [Level](Level.md) |
| [Site](Site.md) | [hasPart](hasPart.md) | any_of[range] | [Level](Level.md) |
| [Site](Site.md) | [isPartOf](isPartOf.md) | any_of[range] | [Level](Level.md) |
| [Building](Building.md) | [hasPart](hasPart.md) | any_of[range] | [Level](Level.md) |
| [Building](Building.md) | [isPartOf](isPartOf.md) | any_of[range] | [Level](Level.md) |
| [Level](Level.md) | [hasPart](hasPart.md) | any_of[range] | [Level](Level.md) |
| [Level](Level.md) | [isPartOf](isPartOf.md) | any_of[range] | [Level](Level.md) |
| [Room](Room.md) | [hasPart](hasPart.md) | any_of[range] | [Level](Level.md) |
| [Room](Room.md) | [isPartOf](isPartOf.md) | any_of[range] | [Level](Level.md) |
| [Zone](Zone.md) | [hasPart](hasPart.md) | any_of[range] | [Level](Level.md) |
| [Zone](Zone.md) | [isPartOf](isPartOf.md) | any_of[range] | [Level](Level.md) |
| [OutdoorSpace](OutdoorSpace.md) | [hasPart](hasPart.md) | any_of[range] | [Level](Level.md) |
| [OutdoorSpace](OutdoorSpace.md) | [isPartOf](isPartOf.md) | any_of[range] | [Level](Level.md) |
| [Asset](Asset.md) | [hasPart](hasPart.md) | any_of[range] | [Level](Level.md) |
| [Asset](Asset.md) | [isPartOf](isPartOf.md) | any_of[range] | [Level](Level.md) |
| [Asset](Asset.md) | [locatedIn](locatedIn.md) | any_of[range] | [Level](Level.md) |
| [Equipment](Equipment.md) | [hasPart](hasPart.md) | any_of[range] | [Level](Level.md) |
| [Equipment](Equipment.md) | [isPartOf](isPartOf.md) | any_of[range] | [Level](Level.md) |
| [Equipment](Equipment.md) | [locatedIn](locatedIn.md) | any_of[range] | [Level](Level.md) |
| [EquipmentExt](EquipmentExt.md) | [hasPart](hasPart.md) | any_of[range] | [Level](Level.md) |
| [EquipmentExt](EquipmentExt.md) | [isPartOf](isPartOf.md) | any_of[range] | [Level](Level.md) |
| [EquipmentExt](EquipmentExt.md) | [locatedIn](locatedIn.md) | any_of[range] | [Level](Level.md) |







## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | 建物のフロア。スペースの一種として扱える。 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:Level |
| native | sbco:Level |
| exact | rec:Level |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Level
annotations:
  description_ja:
    tag: description_ja
    value: 建物のフロア。スペースの一種として扱える。
description: A building storey. Levels can also be treated as a kind of space.
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:Level
is_a: Architecture
slots:
- levelNumber
class_uri: rec:Level

```
</details>

### Induced

<details>
```yaml
name: Level
annotations:
  description_ja:
    tag: description_ja
    value: 建物のフロア。スペースの一種として扱える。
description: A building storey. Levels can also be treated as a kind of space.
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:Level
is_a: Architecture
attributes:
  levelNumber:
    name: levelNumber
    annotations:
      description_ja:
        tag: description_ja
        value: 建物内のフロアまたはレベル番号
    description: Floor or level number within a building
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:levelNumber
    alias: levelNumber
    owner: Level
    domain_of:
    - Level
    range: integer
  area:
    name: area
    description: Area of the architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:area
    alias: area
    owner: Level
    domain_of:
    - Architecture
    range: ArchitectureArea
  capacity:
    name: capacity
    description: Capacity of the architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:capacity
    alias: capacity
    owner: Level
    domain_of:
    - Architecture
    range: ArchitectureCapacity
  address:
    name: address
    description: Address of the architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:address
    alias: address
    owner: Level
    domain_of:
    - Architecture
    range: PostalAddress
    multivalued: true
  adjacentElement:
    name: adjacentElement
    description: Building element adjacent to this architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:adjacentElement
    alias: adjacentElement
    owner: Level
    domain_of:
    - Architecture
    range: BuildingElement
    multivalued: true
  architectedBy:
    name: architectedBy
    description: Agent or resource that architected this structure
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:architectedBy
    alias: architectedBy
    owner: Level
    domain_of:
    - Architecture
    range: Agent
    multivalued: true
  constructedBy:
    name: constructedBy
    description: Agent or resource that constructed this architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:constructedBy
    alias: constructedBy
    owner: Level
    domain_of:
    - Architecture
    range: Agent
    multivalued: true
  containsElement:
    name: containsElement
    description: Building element contained within this architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:containsElement
    alias: containsElement
    owner: Level
    domain_of:
    - Architecture
    range: BuildingElement
    multivalued: true
  documentation:
    name: documentation
    description: Documentation related to this asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:documentation
    alias: documentation
    owner: Level
    domain_of:
    - Architecture
    - Asset
    range: Document
    multivalued: true
  hasPoint:
    name: hasPoint
    description: Point associated with this architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:hasPoint
    alias: hasPoint
    owner: Level
    domain_of:
    - Architecture
    - Asset
    range: Point
    multivalued: true
    any_of:
    - range: Point
    - range: PointExt
  intersectingElement:
    name: intersectingElement
    description: Building element intersecting with this architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:intersectingElement
    alias: intersectingElement
    owner: Level
    domain_of:
    - Architecture
    range: BuildingElement
    multivalued: true
  isFedBy:
    name: isFedBy
    annotations:
      substance:
        tag: substance
        value: SubstanceEnum
    description: Resource that feeds this architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:isFedBy
    alias: isFedBy
    owner: Level
    domain_of:
    - Architecture
    - Equipment
    range: Resource
    multivalued: true
  operatedBy:
    name: operatedBy
    description: Agent or resource that operates this architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:operatedBy
    alias: operatedBy
    owner: Level
    domain_of:
    - Architecture
    range: Agent
    multivalued: true
  ownedBy:
    name: ownedBy
    description: Agent or resource that owns this architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:ownedBy
    alias: ownedBy
    owner: Level
    domain_of:
    - Architecture
    range: Agent
    multivalued: true
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
    owner: Level
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
  geometry:
    name: geometry
    description: Polygon representing the spatial extent of this Space.
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:geometry
    alias: geometry
    owner: Level
    domain_of:
    - Space
    - Asset
    range: Geometry
    multivalued: false
  georeference:
    name: georeference
    description: A georeference creates a relationship between the local coordinate
      system used within a building (e.g., measured in meters) and a geographic coordinate
      system (e.g., lat, long, alt), such that locally placed Spaces can be resolved
      and rendered in that geographic coordinate system (e.g., for mapping purposes).
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:georeference
    alias: georeference
    owner: Level
    domain_of:
    - Space
    range: Georeference
    multivalued: false
  hasPart:
    name: hasPart
    description: The subject is composed in part of the entity given by the object.
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:hasPart
    alias: hasPart
    owner: Level
    domain_of:
    - Space
    - Asset
    range: Any
    multivalued: true
    any_of:
    - range: Space
    - range: Site
    - range: Building
    - range: Level
    - range: Room
    - range: Zone
    - range: OutdoorSpace
  isLocationOf:
    name: isLocationOf
    description: Subject is the physical location encapsulating the object.
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:isLocationOf
    alias: isLocationOf
    owner: Level
    domain_of:
    - Space
    range: EquipmentExt
    multivalued: true
  isPartOf:
    name: isPartOf
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:isPartOf
    alias: isPartOf
    owner: Level
    domain_of:
    - Space
    - Asset
    range: Any
    multivalued: false
    any_of:
    - range: Space
    - range: Site
    - range: Building
    - range: Level
    - range: Room
    - range: Zone
    - range: OutdoorSpace
  customProperties:
    name: customProperties
    description: map(string -> map(string -> string))
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:customProperties
    alias: customProperties
    owner: Level
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
  customTags:
    name: customTags
    description: map(string -> boolean)
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:customTags
    alias: customTags
    owner: Level
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
  identifiers:
    name: identifiers
    description: map(string -> string)
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:identifiers
    alias: identifiers
    owner: Level
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
  name:
    name: name
    description: Machine or Human-readable name
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:name
    alias: name
    owner: Level
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
  description:
    name: description
    annotations:
      description_ja:
        tag: description_ja
        value: リソースのテキスト記述
    description: A textual description of the resource
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:description
    alias: description
    owner: Level
    domain_of:
    - Space
    - Asset
    - Information
    range: string
class_uri: rec:Level

```
</details>