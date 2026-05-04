

# Slot: customProperties 


_map(string -> map(string -> string))_





URI: [rec:customProperties](https://w3id.org/rec/customProperties)
Alias: customProperties

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Media](Media.md) | A media file such as audio or video content |  no  |
| [Space](Space.md) | A contiguous part of the physical world that contains or can contain sub-spac... |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [BuildingElement](BuildingElement.md) | A part of the building structure |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [Geometry](Geometry.md) | REC Geometry のプレースホルダ（詳細は別途拡張） |  no  |
| [Schema](Schema.md) | A schema definition file |  no  |
| [ArchitectureArea](ArchitectureArea.md) | Describes business-relevant area measurements typically associated with archi... |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [Agent](Agent.md) | An entity that can act or be acted upon |  no  |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [Georeference](Georeference.md) | REC Georeference のプレースホルダ（詳細は別途拡張） |  no  |
| [Organization](Organization.md) | An organization such as a company, institution, or association |  no  |
| [Point](Point.md) | A sensor, actuator, or data point associated with equipment |  no  |
| [Level](Level.md) | A building storey |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |
| [Document](Document.md) | A document providing information about a building element or asset |  no  |
| [Information](Information.md) | Abstract base class for information resources such as documents, images, medi... |  no  |
| [Image](Image.md) | An image file containing visual information |  no  |
| [ArchitectureCapacity](ArchitectureCapacity.md) | Describes business-relevant capacity measurements typically associated with a... |  no  |
| [PostalAddress](PostalAddress.md) | A postal address |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |






## Properties

* Range: [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:customProperties |
| native | sbco:customProperties |




## LinkML Source

<details>
```yaml
name: customProperties
description: map(string -> map(string -> string))
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:customProperties
alias: customProperties
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

```
</details>