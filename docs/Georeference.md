

# Class: Georeference 


_REC Georeference のプレースホルダ（詳細は別途拡張）_





URI: [rec:Georeference](https://w3id.org/rec/Georeference)





```mermaid
 classDiagram
    class Georeference
    click Georeference href "../Georeference/"
      Information <|-- Georeference
        click Information href "../Information/"
      
      Georeference : checksum
        
      Georeference : customProperties
        
          
    
        
        
        Georeference --> "*" KeyMapOfStringMapEntry : customProperties
        click KeyMapOfStringMapEntry href "../KeyMapOfStringMapEntry/"
    

        
      Georeference : customTags
        
          
    
        
        
        Georeference --> "*" KeyBoolMapEntry : customTags
        click KeyBoolMapEntry href "../KeyBoolMapEntry/"
    

        
      Georeference : description
        
      Georeference : format
        
      Georeference : identifiers
        
          
    
        
        
        Georeference --> "*" KeyStringMapEntry : identifiers
        click KeyStringMapEntry href "../KeyStringMapEntry/"
    

        
      Georeference : language
        
      Georeference : name
        
      Georeference : size
        
      Georeference : url
        
      Georeference : version
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Information](Information.md)
        * **Georeference**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Machine or Human-readable name | [Information](Information.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the resource | [Information](Information.md) |
| [identifiers](identifiers.md) | * <br/> [KeyStringMapEntry](KeyStringMapEntry.md) | map(string -> string) | [Information](Information.md) |
| [customTags](customTags.md) | * <br/> [KeyBoolMapEntry](KeyBoolMapEntry.md) | map(string -> boolean) | [Information](Information.md) |
| [customProperties](customProperties.md) | * <br/> [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) | map(string -> map(string -> string)) | [Information](Information.md) |
| [format](format.md) | 0..1 <br/> [String](String.md) | MIME type or format identifier for the information | [Information](Information.md) |
| [url](url.md) | 0..1 <br/> [Uri](Uri.md) | URL or URI pointing to the information resource | [Information](Information.md) |
| [version](version.md) | 0..1 <br/> [String](String.md) | Version identifier for the information | [Information](Information.md) |
| [language](language.md) | 0..1 <br/> [String](String.md) | Language code (ISO 639-1) of the information content | [Information](Information.md) |
| [size](size.md) | 0..1 <br/> [Integer](Integer.md) | Size of the information resource in bytes | [Information](Information.md) |
| [checksum](checksum.md) | 0..1 <br/> [String](String.md) | Checksum or hash of the information content | [Information](Information.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Space](Space.md) | [georeference](georeference.md) | range | [Georeference](Georeference.md) |
| [Architecture](Architecture.md) | [georeference](georeference.md) | range | [Georeference](Georeference.md) |
| [Site](Site.md) | [georeference](georeference.md) | range | [Georeference](Georeference.md) |
| [Building](Building.md) | [georeference](georeference.md) | range | [Georeference](Georeference.md) |
| [Level](Level.md) | [georeference](georeference.md) | range | [Georeference](Georeference.md) |
| [Room](Room.md) | [georeference](georeference.md) | range | [Georeference](Georeference.md) |
| [Zone](Zone.md) | [georeference](georeference.md) | range | [Georeference](Georeference.md) |
| [OutdoorSpace](OutdoorSpace.md) | [georeference](georeference.md) | range | [Georeference](Georeference.md) |







## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | 地理参照情報のプレースホルダ |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:Georeference |
| native | sbco:Georeference |
| exact | rec:Georeference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Georeference
annotations:
  description_ja:
    tag: description_ja
    value: 地理参照情報のプレースホルダ
description: REC Georeference のプレースホルダ（詳細は別途拡張）
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:Georeference
is_a: Information
class_uri: rec:Georeference

```
</details>

### Induced

<details>
```yaml
name: Georeference
annotations:
  description_ja:
    tag: description_ja
    value: 地理参照情報のプレースホルダ
description: REC Georeference のプレースホルダ（詳細は別途拡張）
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:Georeference
is_a: Information
attributes:
  name:
    name: name
    description: Machine or Human-readable name
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:name
    alias: name
    owner: Georeference
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
    owner: Georeference
    domain_of:
    - Space
    - Asset
    - Information
    range: string
  identifiers:
    name: identifiers
    description: map(string -> string)
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:identifiers
    alias: identifiers
    owner: Georeference
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
    owner: Georeference
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
    owner: Georeference
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
  format:
    name: format
    annotations:
      description_ja:
        tag: description_ja
        value: 情報のMIMEタイプまたはフォーマット識別子
    description: MIME type or format identifier for the information
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:format
    alias: format
    owner: Georeference
    domain_of:
    - Information
    range: string
  url:
    name: url
    annotations:
      description_ja:
        tag: description_ja
        value: 情報リソースを指すURLまたはURI
    description: URL or URI pointing to the information resource
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:url
    alias: url
    owner: Georeference
    domain_of:
    - Information
    range: uri
  version:
    name: version
    annotations:
      description_ja:
        tag: description_ja
        value: 情報のバージョン識別子
    description: Version identifier for the information
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:version
    alias: version
    owner: Georeference
    domain_of:
    - Information
    range: string
  language:
    name: language
    annotations:
      description_ja:
        tag: description_ja
        value: 情報コンテンツの言語コード (ISO 639-1)
    description: Language code (ISO 639-1) of the information content
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:language
    alias: language
    owner: Georeference
    domain_of:
    - Information
    range: string
    pattern: ^[a-z]{2}(-[A-Z]{2})?$
  size:
    name: size
    annotations:
      description_ja:
        tag: description_ja
        value: 情報リソースのサイズ（バイト）
    description: Size of the information resource in bytes
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:size
    alias: size
    owner: Georeference
    domain_of:
    - Information
    range: integer
  checksum:
    name: checksum
    annotations:
      description_ja:
        tag: description_ja
        value: 情報コンテンツのチェックサムまたはハッシュ
    description: Checksum or hash of the information content
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:checksum
    alias: checksum
    owner: Georeference
    domain_of:
    - Information
    range: string
class_uri: rec:Georeference

```
</details>