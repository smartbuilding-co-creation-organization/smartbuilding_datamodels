

# Slot: language 


_Language code (ISO 639-1) of the information content_





URI: [rec:language](https://w3id.org/rec/language)
Alias: language

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image](Image.md) | An image file containing visual information |  no  |
| [Media](Media.md) | A media file such as audio or video content |  no  |
| [Schema](Schema.md) | A schema definition file |  no  |
| [PostalAddress](PostalAddress.md) | A postal address |  no  |
| [Document](Document.md) | A document providing information about a building element or asset |  no  |
| [Geometry](Geometry.md) | REC Geometry のプレースホルダ（詳細は別途拡張） |  no  |
| [Georeference](Georeference.md) | REC Georeference のプレースホルダ（詳細は別途拡張） |  no  |
| [Information](Information.md) | Abstract base class for information resources such as documents, images, medi... |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^[a-z]{2}(-[A-Z]{2})?$`




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | 情報コンテンツの言語コード (ISO 639-1) |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:language |
| native | sbco:language |




## LinkML Source

<details>
```yaml
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
domain_of:
- Information
range: string
pattern: ^[a-z]{2}(-[A-Z]{2})?$

```
</details>