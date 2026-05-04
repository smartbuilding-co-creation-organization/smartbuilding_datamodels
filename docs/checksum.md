

# Slot: checksum 


_Checksum or hash of the information content_





URI: [rec:checksum](https://w3id.org/rec/checksum)
Alias: checksum

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image](Image.md) | An image file containing visual information |  no  |
| [Document](Document.md) | A document providing information about a building element or asset |  no  |
| [Media](Media.md) | A media file such as audio or video content |  no  |
| [Schema](Schema.md) | A schema definition file |  no  |
| [PostalAddress](PostalAddress.md) | A postal address |  no  |
| [Document](Document.md) | A document providing information about a building element or asset |  no  |
| [Geometry](Geometry.md) | REC Geometry のプレースホルダ（詳細は別途拡張） |  no  |
| [Georeference](Georeference.md) | REC Georeference のプレースホルダ（詳細は別途拡張） |  no  |
| [Information](Information.md) | Abstract base class for information resources such as documents, images, medi... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | 情報コンテンツのチェックサムまたはハッシュ |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:checksum |
| native | sbco:checksum |




## LinkML Source

<details>
```yaml
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
domain_of:
- Information
range: string

```
</details>