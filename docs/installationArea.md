

# Slot: installationArea 


_Parent installation area_





URI: [sbco:installationArea](https://www.sbco.or.jp/ont/installationArea)
Alias: installationArea

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |
| [EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:installationArea |
| native | sbco:installationArea |




## LinkML Source

<details>
```yaml
name: installationArea
description: Parent installation area
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
alias: installationArea
domain_of:
- EquipmentExt
- PointExt
range: string

```
</details>