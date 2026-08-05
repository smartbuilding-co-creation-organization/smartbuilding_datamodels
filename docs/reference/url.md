---
search:
  boost: 5.0
---

# Slot: url 


_URL or URI pointing to the information resource_






URI: [rec:url](https://w3id.org/rec/url)
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
| Range | [Uri](Uri.md) |
| Domain Of | [Information](Information.md) |
| Slot URI | [rec:url](https://w3id.org/rec/url) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_ja | 情報リソースを指すURLまたはURI |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:url |
| native | sbco:url |




## LinkML Source

<details markdown="1">
```yaml
name: url
annotations:
  description_ja:
    tag: description_ja
    value: 情報リソースを指すURLまたはURI
description: URL or URI pointing to the information resource
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:url
domain_of:
- Information
range: uri

```
</details>