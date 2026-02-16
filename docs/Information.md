

# Class: Information 


_Abstract base class for information resources such as documents, images, media files, etc._





URI: [rec:Information](https://w3id.org/rec/Information)





```mermaid
 classDiagram
    class Information
    click Information href "../Information/"
      Resource <|-- Information
        click Resource href "../Resource/"
      

      Information <|-- Document
        click Document href "../Document/"
      Information <|-- Image
        click Image href "../Image/"
      Information <|-- Media
        click Media href "../Media/"
      Information <|-- Schema
        click Schema href "../Schema/"
      Information <|-- PostalAddress
        click PostalAddress href "../PostalAddress/"
      Information <|-- Geometry
        click Geometry href "../Geometry/"
      Information <|-- Georeference
        click Georeference href "../Georeference/"
      

      Information : checksum
        
      Information : customProperties
        
          
    
        
        
        Information --> "*" KeyMapOfStringMapEntry : customProperties
        click KeyMapOfStringMapEntry href "../KeyMapOfStringMapEntry/"
    

        
      Information : customTags
        
          
    
        
        
        Information --> "*" KeyBoolMapEntry : customTags
        click KeyBoolMapEntry href "../KeyBoolMapEntry/"
    

        
      Information : description
        
      Information : format
        
      Information : identifiers
        
          
    
        
        
        Information --> "*" KeyStringMapEntry : identifiers
        click KeyStringMapEntry href "../KeyStringMapEntry/"
    

        
      Information : language
        
      Information : name
        
      Information : size
        
      Information : url
        
      Information : version
        
      
```





## Inheritance
* [Resource](Resource.md)
    * **Information**
        * [Document](Document.md)
        * [Image](Image.md)
        * [Media](Media.md)
        * [Schema](Schema.md)
        * [PostalAddress](PostalAddress.md)
        * [Geometry](Geometry.md)
        * [Georeference](Georeference.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Machine or Human-readable name | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the resource | direct |
| [identifiers](identifiers.md) | * <br/> [KeyStringMapEntry](KeyStringMapEntry.md) | map(string -> string) | direct |
| [customTags](customTags.md) | * <br/> [KeyBoolMapEntry](KeyBoolMapEntry.md) | map(string -> boolean) | direct |
| [customProperties](customProperties.md) | * <br/> [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) | map(string -> map(string -> string)) | direct |
| [format](format.md) | 0..1 <br/> [String](String.md) | MIME type or format identifier for the information | direct |
| [url](url.md) | 0..1 <br/> [Uri](Uri.md) | URL or URI pointing to the information resource | direct |
| [version](version.md) | 0..1 <br/> [String](String.md) | Version identifier for the information | direct |
| [language](language.md) | 0..1 <br/> [String](String.md) | Language code (ISO 639-1) of the information content | direct |
| [size](size.md) | 0..1 <br/> [Integer](Integer.md) | Size of the information resource in bytes | direct |
| [checksum](checksum.md) | 0..1 <br/> [String](String.md) | Checksum or hash of the information content | direct |










## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | ドキュメント、画像、メディアファイルなどの情報リソースの抽象基底クラス |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:Information |
| native | sbco:Information |
| exact | rec:Information |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Information
annotations:
  description_ja:
    tag: description_ja
    value: ドキュメント、画像、メディアファイルなどの情報リソースの抽象基底クラス
description: Abstract base class for information resources such as documents, images,
  media files, etc.
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:Information
is_a: Resource
slots:
- name
- description
- identifiers
- customTags
- customProperties
- format
- url
- version
- language
- size
- checksum
class_uri: rec:Information

```
</details>

### Induced

<details>
```yaml
name: Information
annotations:
  description_ja:
    tag: description_ja
    value: ドキュメント、画像、メディアファイルなどの情報リソースの抽象基底クラス
description: Abstract base class for information resources such as documents, images,
  media files, etc.
from_schema: https://www.sbco.or.jp/ont/schema
exact_mappings:
- rec:Information
is_a: Resource
attributes:
  name:
    name: name
    description: Machine or Human-readable name
    from_schema: https://www.sbco.or.jp/ont/schema
    rank: 1000
    slot_uri: rec:name
    alias: name
    owner: Information
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
    owner: Information
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
    owner: Information
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
    owner: Information
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
    owner: Information
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
    owner: Information
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
    owner: Information
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
    owner: Information
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
    owner: Information
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
    owner: Information
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
    owner: Information
    domain_of:
    - Information
    range: string
class_uri: rec:Information

```
</details>