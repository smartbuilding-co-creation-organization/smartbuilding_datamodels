

# Slot: memberOf 


_Indicates membership in an organization. Note that componency (e.g., departments of a corporation) are expressed using the more generic Organization.isPartOf property._





URI: [rec:memberOf](https://w3id.org/rec/memberOf)
Alias: memberOf

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Agent](Agent.md) | An entity that can act or be acted upon |  no  |
| [Organization](Organization.md) | An organization such as a company, institution, or association |  no  |






## Properties

* Range: [Organization](Organization.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rec:memberOf |
| native | sbco:memberOf |




## LinkML Source

<details>
```yaml
name: memberOf
description: Indicates membership in an organization. Note that componency (e.g.,
  departments of a corporation) are expressed using the more generic Organization.isPartOf
  property.
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
slot_uri: rec:memberOf
alias: memberOf
domain_of:
- Agent
range: Organization
multivalued: true

```
</details>