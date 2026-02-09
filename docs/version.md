

# Slot: version 


_Version identifier for the information_





URI: [rec:version](https://w3id.org/rec/version)
Alias: version

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

* Range: [String](String.md)




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | 情報のバージョン識別子 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:version |
| native | sbco:version |




## LinkML Source

<details>
```yaml
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
domain_of:
- Information
range: string

```
</details>