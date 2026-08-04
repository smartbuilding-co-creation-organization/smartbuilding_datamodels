

# Slot: url 


_URL or URI pointing to the information resource_





URI: [rec:url](https://w3id.org/rec/url)
Alias: url

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

* Range: [Uri](Uri.md)




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

<details>
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
alias: url
domain_of:
- Information
range: uri

```
</details>