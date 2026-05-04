

# Slot: id 


_Unique identifier within the schema. Must start with a letter and contain only letters, digits, underscores, hyphens, colons, semicolons, or periods. DTMI is one acceptable example._





URI: [sbco:id](https://www.sbco.or.jp/ont/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |
| [Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |  no  |
| [BuildingElement](BuildingElement.md) | A part of the building structure |  no  |
| [Level](Level.md) | A building storey |  no  |
| [Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |  no  |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |
| [Point](Point.md) | A sensor, actuator, or data point associated with equipment |  no  |
| [Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |  no  |
| [Building](Building.md) | A building which is part of a site |  no  |
| [OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |  no  |
| [ArchitectureCapacity](ArchitectureCapacity.md) | Describes business-relevant capacity measurements typically associated with a... |  no  |
| [Site](Site.md) | A piece of land upon which zero or more buildings may be situated |  no  |
| [ArchitectureArea](ArchitectureArea.md) | Describes business-relevant area measurements typically associated with archi... |  no  |
| [Equipment](Equipment.md) | An equipment asset installed in a space |  no  |
| [Space](Space.md) | A contiguous part of the physical world that contains or can contain sub-spac... |  no  |
| [Room](Room.md) | A room within a building |  no  |
| [Agent](Agent.md) | An entity that can act or be acted upon |  no  |
| [Organization](Organization.md) | An organization such as a company, institution, or association |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | スキーマ内の一意識別子。文字で開始し、DTMI形式もサポート。 |
| example | dtmi:example:Building:1 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:id |
| native | sbco:id |




## LinkML Source

<details>
```yaml
name: id
annotations:
  description_ja:
    tag: description_ja
    value: スキーマ内の一意識別子。文字で開始し、DTMI形式もサポート。
  example:
    tag: example
    value: dtmi:example:Building:1
description: Unique identifier within the schema. Must start with a letter and contain
  only letters, digits, underscores, hyphens, colons, semicolons, or periods. DTMI
  is one acceptable example.
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
identifier: true
alias: id
domain_of:
- Space
- Asset
- Point
- Agent
- Organization
- BuildingElement
- ArchitectureArea
- ArchitectureCapacity
range: string
required: true

```
</details>