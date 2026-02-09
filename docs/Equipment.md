

# Class: Equipment 


_An equipment asset installed in a space._





URI: [brick:Equipment](https://brickschema.org/schema/Brick#Equipment)





```mermaid
 classDiagram
    class Equipment
    click Equipment href "../Equipment/"
      Asset <|-- Equipment
        click Asset href "../Asset/"
      

      Equipment <|-- EquipmentExt
        click EquipmentExt href "../EquipmentExt/"
      

      Equipment : assetTag
        
      Equipment : commissionedBy
        
          
    
        
        
        Equipment --> "*" Agent : commissionedBy
        click Agent href "../Agent/"
    

        
      Equipment : commissioningDate
        
      Equipment : customProperties
        
          
    
        
        
        Equipment --> "*" KeyMapOfStringMapEntry : customProperties
        click KeyMapOfStringMapEntry href "../KeyMapOfStringMapEntry/"
    

        
      Equipment : customTags
        
          
    
        
        
        Equipment --> "*" KeyBoolMapEntry : customTags
        click KeyBoolMapEntry href "../KeyBoolMapEntry/"
    

        
      Equipment : description
        
      Equipment : documentation
        
          
    
        
        
        Equipment --> "*" Document : documentation
        click Document href "../Document/"
    

        
      Equipment : feeds
        
          
    
        
        
        Equipment --> "*" Resource : feeds
        click Resource href "../Resource/"
    

        
      Equipment : geometry
        
          
    
        
        
        Equipment --> "0..1" Geometry : geometry
        click Geometry href "../Geometry/"
    

        
      Equipment : hasPart
        
      Equipment : hasPoint
        
          
    
        
        
        Equipment --> "*" Point : hasPoint
        click Point href "../Point/"
    

        
      Equipment : id
        
      Equipment : identifiers
        
          
    
        
        
        Equipment --> "*" KeyStringMapEntry : identifiers
        click KeyStringMapEntry href "../KeyStringMapEntry/"
    

        
      Equipment : initialCost
        
      Equipment : installationDate
        
      Equipment : installedBy
        
          
    
        
        
        Equipment --> "*" Agent : installedBy
        click Agent href "../Agent/"
    

        
      Equipment : IPAddress
        
      Equipment : isFedBy
        
          
    
        
        
        Equipment --> "*" Resource : isFedBy
        click Resource href "../Resource/"
    

        
      Equipment : isPartOf
        
      Equipment : locatedIn
        
      Equipment : MACAddress
        
      Equipment : maintenanceInterval
        
      Equipment : manufacturedBy
        
          
    
        
        
        Equipment --> "*" Agent : manufacturedBy
        click Agent href "../Agent/"
    

        
      Equipment : modelNumber
        
      Equipment : mountedOn
        
          
    
        
        
        Equipment --> "0..1" BuildingElement : mountedOn
        click BuildingElement href "../BuildingElement/"
    

        
      Equipment : name
        
      Equipment : operationalStageCount
        
      Equipment : serialNumber
        
      Equipment : servicedBy
        
          
    
        
        
        Equipment --> "*" Agent : servicedBy
        click Agent href "../Agent/"
    

        
      Equipment : turnoverDate
        
      Equipment : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Asset](Asset.md)
        * **Equipment**
            * [EquipmentExt](EquipmentExt.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [feeds](feeds.md) | * <br/> [Resource](Resource.md) | Equipment or system that this equipment feeds | direct |
| [isFedBy](isFedBy.md) | * <br/> [Resource](Resource.md) | Resource that feeds this architecture | direct |
| [operationalStageCount](operationalStageCount.md) | 0..1 <br/> [Integer](Integer.md) | The number of operational stages supported by this equipment | direct |
| [id](id.md) | 1 <br/> [String](String.md) | Unique identifier within the schema | [Asset](Asset.md) |
| [commissionedBy](commissionedBy.md) | * <br/> [Agent](Agent.md) | Agent or resource that commissioned this asset | [Asset](Asset.md) |
| [documentation](documentation.md) | * <br/> [Document](Document.md) | Documentation related to this asset | [Asset](Asset.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the resource | [Asset](Asset.md) |
| [geometry](geometry.md) | 0..1 <br/> [Geometry](Geometry.md) | Polygon representing the spatial extent of this Space | [Asset](Asset.md) |
| [hasPart](hasPart.md) | * <br/> [Any](Any.md)&nbsp;or&nbsp;<br />[Space](Space.md)&nbsp;or&nbsp;<br />[Site](Site.md)&nbsp;or&nbsp;<br />[Building](Building.md)&nbsp;or&nbsp;<br />[Level](Level.md)&nbsp;or&nbsp;<br />[Room](Room.md)&nbsp;or&nbsp;<br />[Zone](Zone.md)&nbsp;or&nbsp;<br />[OutdoorSpace](OutdoorSpace.md) | The subject is composed in part of the entity given by the object | [Asset](Asset.md) |
| [hasPoint](hasPoint.md) | * <br/> [Point](Point.md)&nbsp;or&nbsp;<br />[Point](Point.md)&nbsp;or&nbsp;<br />[PointExt](PointExt.md) | Point associated with this architecture | [Asset](Asset.md) |
| [installedBy](installedBy.md) | * <br/> [Agent](Agent.md) | Agent or resource that installed this asset | [Asset](Asset.md) |
| [isPartOf](isPartOf.md) | 0..1 <br/> [Any](Any.md)&nbsp;or&nbsp;<br />[Space](Space.md)&nbsp;or&nbsp;<br />[Site](Site.md)&nbsp;or&nbsp;<br />[Building](Building.md)&nbsp;or&nbsp;<br />[Level](Level.md)&nbsp;or&nbsp;<br />[Room](Room.md)&nbsp;or&nbsp;<br />[Zone](Zone.md)&nbsp;or&nbsp;<br />[OutdoorSpace](OutdoorSpace.md) |  | [Asset](Asset.md) |
| [locatedIn](locatedIn.md) | * <br/> [Any](Any.md)&nbsp;or&nbsp;<br />[Space](Space.md)&nbsp;or&nbsp;<br />[Site](Site.md)&nbsp;or&nbsp;<br />[Building](Building.md)&nbsp;or&nbsp;<br />[Level](Level.md)&nbsp;or&nbsp;<br />[Room](Room.md)&nbsp;or&nbsp;<br />[Zone](Zone.md)&nbsp;or&nbsp;<br />[OutdoorSpace](OutdoorSpace.md) | Space where this asset is located | [Asset](Asset.md) |
| [manufacturedBy](manufacturedBy.md) | * <br/> [Agent](Agent.md) | Agent or resource that manufactured this asset | [Asset](Asset.md) |
| [mountedOn](mountedOn.md) | 0..1 <br/> [BuildingElement](BuildingElement.md) | Building element on which this asset is mounted | [Asset](Asset.md) |
| [servicedBy](servicedBy.md) | * <br/> [Agent](Agent.md) | Agent or resource that services this asset | [Asset](Asset.md) |
| [assetTag](assetTag.md) | * <br/> [String](String.md) | Asset identification tag | [Asset](Asset.md) |
| [commissioningDate](commissioningDate.md) | 0..1 <br/> [Date](Date.md) | Date when the asset was commissioned | [Asset](Asset.md) |
| [customProperties](customProperties.md) | * <br/> [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) | map(string -> map(string -> string)) | [Asset](Asset.md) |
| [customTags](customTags.md) | * <br/> [KeyBoolMapEntry](KeyBoolMapEntry.md) | map(string -> boolean) | [Asset](Asset.md) |
| [identifiers](identifiers.md) | * <br/> [KeyStringMapEntry](KeyStringMapEntry.md) | map(string -> string) | [Asset](Asset.md) |
| [initialCost](initialCost.md) | 0..1 <br/> [String](String.md) | Initial cost of the asset | [Asset](Asset.md) |
| [installationDate](installationDate.md) | 0..1 <br/> [Date](Date.md) | Date when the asset was installed | [Asset](Asset.md) |
| [IPAddress](IPAddress.md) | * <br/> [String](String.md) | IP address of the asset | [Asset](Asset.md) |
| [MACAddress](MACAddress.md) | * <br/> [String](String.md) | MAC address of the asset | [Asset](Asset.md) |
| [maintenanceInterval](maintenanceInterval.md) | * <br/> [DurationString](DurationString.md) | Maintenance interval duration | [Asset](Asset.md) |
| [modelNumber](modelNumber.md) | 0..1 <br/> [String](String.md) | Model number of the asset | [Asset](Asset.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Machine or Human-readable name | [Asset](Asset.md) |
| [serialNumber](serialNumber.md) | 0..1 <br/> [String](String.md) | Serial number of the asset | [Asset](Asset.md) |
| [turnoverDate](turnoverDate.md) | 0..1 <br/> [Date](Date.md) | Date when the asset was turned over | [Asset](Asset.md) |
| [weight](weight.md) | 0..1 <br/> [Decimal](Decimal.md) | Weight of the asset | [Asset](Asset.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Point](Point.md) | [isPointOf](isPointOf.md) | range | [Equipment](Equipment.md) |
| [PointExt](PointExt.md) | [isPointOf](isPointOf.md) | range | [Equipment](Equipment.md) |
| [PointExt](PointExt.md) | [isPointOf](isPointOf.md) | any_of[range] | [Equipment](Equipment.md) |







## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | 空間に設置された設備アセット。 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brick:Equipment |
| native | sbco:Equipment |
| exact | brick:Equipment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Equipment
annotations:
  description_ja:
    tag: description_ja
    value: 空間に設置された設備アセット。
description: An equipment asset installed in a space.
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- brick:Equipment
is_a: Asset
slots:
- feeds
- isFedBy
- operationalStageCount
slot_usage:
  locatedIn:
    name: locatedIn
    range: Any
    any_of:
    - range: Space
    - range: Site
    - range: Building
    - range: Level
    - range: Room
    - range: Zone
    - range: OutdoorSpace
class_uri: brick:Equipment

```
</details>

### Induced

<details>
```yaml
name: Equipment
annotations:
  description_ja:
    tag: description_ja
    value: 空間に設置された設備アセット。
description: An equipment asset installed in a space.
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- brick:Equipment
is_a: Asset
slot_usage:
  locatedIn:
    name: locatedIn
    range: Any
    any_of:
    - range: Space
    - range: Site
    - range: Building
    - range: Level
    - range: Room
    - range: Zone
    - range: OutdoorSpace
attributes:
  feeds:
    name: feeds
    annotations:
      substance:
        tag: substance
        value: SubstanceEnum
    description: Equipment or system that this equipment feeds
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: brick:feeds
    alias: feeds
    owner: Equipment
    domain_of:
    - Equipment
    range: Resource
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
    owner: Equipment
    domain_of:
    - Architecture
    - Equipment
    range: Resource
    multivalued: true
  operationalStageCount:
    name: operationalStageCount
    description: The number of operational stages supported by this equipment
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: brick:operationalStageCount
    alias: operationalStageCount
    owner: Equipment
    domain_of:
    - Equipment
    range: integer
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
    owner: Equipment
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
  commissionedBy:
    name: commissionedBy
    description: Agent or resource that commissioned this asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:commissionedBy
    alias: commissionedBy
    owner: Equipment
    domain_of:
    - Asset
    range: Agent
    multivalued: true
  documentation:
    name: documentation
    description: Documentation related to this asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:documentation
    alias: documentation
    owner: Equipment
    domain_of:
    - Architecture
    - Asset
    range: Document
    multivalued: true
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
    owner: Equipment
    domain_of:
    - Space
    - Asset
    - Information
    range: string
  geometry:
    name: geometry
    description: Polygon representing the spatial extent of this Space.
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:geometry
    alias: geometry
    owner: Equipment
    domain_of:
    - Space
    - Asset
    range: Geometry
    multivalued: false
  hasPart:
    name: hasPart
    description: The subject is composed in part of the entity given by the object.
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:hasPart
    alias: hasPart
    owner: Equipment
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
  hasPoint:
    name: hasPoint
    description: Point associated with this architecture
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:hasPoint
    alias: hasPoint
    owner: Equipment
    domain_of:
    - Architecture
    - Asset
    range: Point
    multivalued: true
    any_of:
    - range: Point
    - range: PointExt
  installedBy:
    name: installedBy
    description: Agent or resource that installed this asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:installedBy
    alias: installedBy
    owner: Equipment
    domain_of:
    - Asset
    range: Agent
    multivalued: true
  isPartOf:
    name: isPartOf
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:isPartOf
    alias: isPartOf
    owner: Equipment
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
  locatedIn:
    name: locatedIn
    description: Space where this asset is located
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:locatedIn
    alias: locatedIn
    owner: Equipment
    domain_of:
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
  manufacturedBy:
    name: manufacturedBy
    description: Agent or resource that manufactured this asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:manufacturedBy
    alias: manufacturedBy
    owner: Equipment
    domain_of:
    - Asset
    range: Agent
    multivalued: true
  mountedOn:
    name: mountedOn
    description: Building element on which this asset is mounted
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:mountedOn
    alias: mountedOn
    owner: Equipment
    domain_of:
    - Asset
    range: BuildingElement
  servicedBy:
    name: servicedBy
    description: Agent or resource that services this asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:servicedBy
    alias: servicedBy
    owner: Equipment
    domain_of:
    - Asset
    range: Agent
    multivalued: true
  assetTag:
    name: assetTag
    description: Asset identification tag
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:assetTag
    alias: assetTag
    owner: Equipment
    domain_of:
    - Asset
    range: string
    multivalued: true
  commissioningDate:
    name: commissioningDate
    description: Date when the asset was commissioned
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:commissioningDate
    alias: commissioningDate
    owner: Equipment
    domain_of:
    - Asset
    range: date
  customProperties:
    name: customProperties
    description: map(string -> map(string -> string))
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:customProperties
    alias: customProperties
    owner: Equipment
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
    owner: Equipment
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
    owner: Equipment
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
  initialCost:
    name: initialCost
    description: Initial cost of the asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:initialCost
    alias: initialCost
    owner: Equipment
    domain_of:
    - Asset
    range: string
  installationDate:
    name: installationDate
    description: Date when the asset was installed
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:installationDate
    alias: installationDate
    owner: Equipment
    domain_of:
    - Asset
    range: date
  IPAddress:
    name: IPAddress
    description: IP address of the asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:IPAddress
    alias: IPAddress
    owner: Equipment
    domain_of:
    - Asset
    range: string
    multivalued: true
    pattern: ^((25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(25[0-5]|2[0-4]\d|1?\d?\d)$
  MACAddress:
    name: MACAddress
    description: MAC address of the asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:MACAddress
    alias: MACAddress
    owner: Equipment
    domain_of:
    - Asset
    range: string
    multivalued: true
    pattern: ^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$
  maintenanceInterval:
    name: maintenanceInterval
    description: Maintenance interval duration
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:maintenanceInterval
    alias: maintenanceInterval
    owner: Equipment
    domain_of:
    - Asset
    range: DurationString
    multivalued: true
  modelNumber:
    name: modelNumber
    description: Model number of the asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:modelNumber
    alias: modelNumber
    owner: Equipment
    domain_of:
    - Asset
    range: string
  name:
    name: name
    description: Machine or Human-readable name
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:name
    alias: name
    owner: Equipment
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
  serialNumber:
    name: serialNumber
    description: Serial number of the asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:serialNumber
    alias: serialNumber
    owner: Equipment
    domain_of:
    - Asset
    range: string
  turnoverDate:
    name: turnoverDate
    description: Date when the asset was turned over
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:turnoverDate
    alias: turnoverDate
    owner: Equipment
    domain_of:
    - Asset
    range: date
  weight:
    name: weight
    description: Weight of the asset
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:weight
    alias: weight
    owner: Equipment
    domain_of:
    - Asset
    range: decimal
class_uri: brick:Equipment

```
</details>