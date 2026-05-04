

# Slot: description 


_A textual description of the resource_





URI: [rec:description](https://w3id.org/rec/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [Level](Level.md) | A building storey |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [Space](Space.md) | A contiguous part of the physical world that contains or can contain sub-spac... |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |
| [Image](Image.md) | An image file containing visual information |  no  |
| [Georeference](Georeference.md) | REC Georeference のプレースホルダ（詳細は別途拡張） |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [Schema](Schema.md) | A schema definition file |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [Media](Media.md) | A media file such as audio or video content |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [Geometry](Geometry.md) | REC Geometry のプレースホルダ（詳細は別途拡張） |  no  |
| [Information](Information.md) | Abstract base class for information resources such as documents, images, medi... |  no  |
| [PostalAddress](PostalAddress.md) | A postal address |  no  |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [Document](Document.md) | A document providing information about a building element or asset |  no  |
| [Room](Room.md) | A room within a building |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | リソースのテキスト記述 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:description |
| native | sbco:description |




## LinkML Source

<details>
```yaml
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
domain_of:
- Space
- Asset
- Information
range: string

```
</details>