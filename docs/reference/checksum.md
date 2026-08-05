---
search:
  boost: 5.0
---

# Slot: checksum 


_Checksum or hash of the information content_






URI: [rec:checksum](https://w3id.org/rec/checksum)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Information](Information.md) | Abstract base class for information resources such as documents, images, medi... |  no  |
| [Document](Document.md) | A document providing information about a building element or asset |  no  |
| [Image](Image.md) | An image file containing visual information |  no  |
| [Media](Media.md) | A media file such as audio or video content |  no  |
| [Schema](Schema.md) | A schema definition file |  no  |
| [PostalAddress](PostalAddress.md) | A postal address |  no  |
| [GeometryInfo](GeometryInfo.md) | Placeholder for REC Geometry; details can be supplied by extensions |  no  |
| [GeoreferenceInfo](GeoreferenceInfo.md) | Placeholder for REC Georeference; details can be supplied by extensions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Information](Information.md) |
| Slot URI | [rec:checksum](https://w3id.org/rec/checksum) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










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

<details markdown="1">
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
domain_of:
- Information
range: string

```
</details>