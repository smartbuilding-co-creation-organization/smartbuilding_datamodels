

# Slot: format 


_MIME type or format identifier for the information_





URI: [rec:format](https://w3id.org/rec/format)
Alias: format

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PostalAddress](PostalAddress.md) | A postal address |  no  |
| [GeoreferenceInfo](GeoreferenceInfo.md) | Placeholder for REC Georeference; details can be supplied by extensions |  no  |
| [GeometryInfo](GeometryInfo.md) | Placeholder for REC Geometry; details can be supplied by extensions |  no  |
| [Schema](Schema.md) | A schema definition file |  no  |
| [Media](Media.md) | A media file such as audio or video content |  no  |
| [Image](Image.md) | An image file containing visual information |  no  |
| [Information](Information.md) | Abstract base class for information resources such as documents, images, medi... |  no  |
| [Document](Document.md) | A document providing information about a building element or asset |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | 情報のMIMEタイプまたはフォーマット識別子 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:format |
| native | sbco:format |




## LinkML Source

<details>
```yaml
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
domain_of:
- Information
range: string

```
</details>