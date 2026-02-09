

# Slot: size 


_Size of the information resource in bytes_





URI: [rec:size](https://w3id.org/rec/size)
Alias: size

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Georeference](Georeference.md) | REC Georeference のプレースホルダ（詳細は別途拡張） |  no  |
| [Document](Document.md) | A document providing information about a building element or asset |  no  |
| [Information](Information.md) | Abstract base class for information resources such as documents, images, medi... |  no  |
| [PostalAddress](PostalAddress.md) | A postal address |  no  |
| [Geometry](Geometry.md) | REC Geometry のプレースホルダ（詳細は別途拡張） |  no  |
| [Image](Image.md) | An image file containing visual information |  no  |
| [Media](Media.md) | A media file such as audio or video content |  no  |
| [Schema](Schema.md) | A schema definition file |  no  |






## Properties

* Range: [Integer](Integer.md)




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | 情報リソースのサイズ（バイト） |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:size |
| native | sbco:size |




## LinkML Source

<details>
```yaml
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
domain_of:
- Information
range: integer

```
</details>