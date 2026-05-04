

# Slot: labels 


_Labels or tags associated with this point_





URI: [sbco:labels](https://www.sbco.or.jp/ont/labels)
Alias: labels

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True




## Identifier and Mapping Information




### Annotations

| property | value |
| --- | --- |
| description_ja | このポイントに関連するラベルまたはタグ |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sbco:labels |
| native | sbco:labels |




## LinkML Source

<details>
```yaml
name: labels
annotations:
  description_ja:
    tag: description_ja
    value: このポイントに関連するラベルまたはタグ
description: Labels or tags associated with this point
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
alias: labels
domain_of:
- PointExt
range: string
multivalued: true

```
</details>