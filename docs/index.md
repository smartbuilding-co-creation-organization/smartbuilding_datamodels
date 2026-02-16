# Smart Building Model

A LinkML schema for sites, buildings, spaces, equipment, and points used in smart-building data exchanges.


URI: https://www.sbco.or.jp/ont/schema

Name: building_model



## Classes

| Class | Description |
| --- | --- |
| [KeyBoolMapEntry](KeyBoolMapEntry.md) | map(string -> boolean) の1エントリ |
| [KeyMapOfStringMapEntry](KeyMapOfStringMapEntry.md) | map(string -> map(string -> string)) の1エントリ |
| [KeyStringMapEntry](KeyStringMapEntry.md) | map(string -> string) の1エントリ |
| [Point](Point.md) | A sensor, actuator, or data point associated with equipment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PointExt](PointExt.md) | A point (sensor/actuator) in a smart building context |
| [Resource](Resource.md) | Base class for all resources |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Agent](Agent.md) | An entity that can act or be acted upon |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Organization](Organization.md) | An organization such as a company, institution, or association |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ArchitectureArea](ArchitectureArea.md) | Describes business-relevant area measurements typically associated with archi... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ArchitectureCapacity](ArchitectureCapacity.md) | Describes business-relevant capacity measurements typically associated with a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Asset](Asset.md) | Something which is placed inside of a building, but is not an integral part o... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Equipment](Equipment.md) | An equipment asset installed in a space |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EquipmentExt](EquipmentExt.md) | An equipment asset installed in a space |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BuildingElement](BuildingElement.md) | A part of the building structure |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Information](Information.md) | Abstract base class for information resources such as documents, images, medi... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Document](Document.md) | A document providing information about a building element or asset |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Geometry](Geometry.md) | REC Geometry のプレースホルダ（詳細は別途拡張） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Georeference](Georeference.md) | REC Georeference のプレースホルダ（詳細は別途拡張） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image](Image.md) | An image file containing visual information |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Media](Media.md) | A media file such as audio or video content |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PostalAddress](PostalAddress.md) | A postal address |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Schema](Schema.md) | A schema definition file |
| [Space](Space.md) | A contiguous part of the physical world that contains or can contain sub-spac... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Architecture](Architecture.md) | A designed/landscaped (or potentially designed/landscaped) part of the physic... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Building](Building.md) | A building which is part of a site |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Level](Level.md) | A building storey |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OutdoorSpace](OutdoorSpace.md) | An outdoor space associated with a site or building |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Room](Room.md) | A room within a building |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Site](Site.md) | A piece of land upon which zero or more buildings may be situated |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Zone](Zone.md) | A sub-zone within or outside of a building defined to support some technology... |



## Slots

| Slot | Description |
| --- | --- |
| [address](address.md) | Address of the architecture |
| [adjacentElement](adjacentElement.md) | Building element adjacent to this architecture |
| [aggregate](aggregate.md) | Aggregation function or method for point data processing |
| [altitude](altitude.md) | Altitude above sea level in meters |
| [architectedBy](architectedBy.md) | Agent or resource that architected this structure |
| [area](area.md) | Area of the architecture |
| [assetTag](assetTag.md) | Asset identification tag |
| [capacity](capacity.md) | Capacity of the architecture |
| [checksum](checksum.md) | Checksum or hash of the information content |
| [commissionedBy](commissionedBy.md) | Agent or resource that commissioned this asset |
| [commissioningDate](commissioningDate.md) | Date when the asset was commissioned |
| [constructedBy](constructedBy.md) | Agent or resource that constructed this architecture |
| [containsElement](containsElement.md) | Building element contained within this architecture |
| [coordinates](coordinates.md) | Geographic coordinates defining the geofence boundary |
| [customProperties](customProperties.md) | map(string -> map(string -> string)) |
| [customTags](customTags.md) | map(string -> boolean) |
| [description](description.md) | A textual description of the resource |
| [deviceType](deviceType.md) | Device Type |
| [documentation](documentation.md) | Documentation related to this asset |
| [entries](entries.md) | Nested map entries |
| [feeds](feeds.md) | Equipment or system that this equipment feeds |
| [flag](flag.md) | Boolean flag value |
| [format](format.md) | MIME type or format identifier for the information |
| [geometry](geometry.md) | Polygon representing the spatial extent of this Space |
| [georeference](georeference.md) | A georeference creates a relationship between the local coordinate system use... |
| [hasPart](hasPart.md) | The subject is composed in part of the entity given by the object |
| [hasPoint](hasPoint.md) | Point associated with this architecture |
| [hasQuantity](hasQuantity.md) | Physical quantity measured by this point |
| [hasSubstance](hasSubstance.md) | Substance associated with this point |
| [id](id.md) | Unique identifier within the schema |
| [identifiers](identifiers.md) | map(string -> string) |
| [initialCost](initialCost.md) | Initial cost of the asset |
| [installationArea](installationArea.md) | Parent installation area |
| [installationDate](installationDate.md) | Date when the asset was installed |
| [installedBy](installedBy.md) | Agent or resource that installed this asset |
| [intersectingElement](intersectingElement.md) | Building element intersecting with this architecture |
| [intervalCapability](intervalCapability.md) | Polling period (period speed that the device is capable of) |
| [IPAddress](IPAddress.md) | IP address of the asset |
| [isFedBy](isFedBy.md) | Resource that feeds this architecture |
| [isLocationOf](isLocationOf.md) | Subject is the physical location encapsulating the object |
| [isPartOf](isPartOf.md) |  |
| [isPointOf](isPointOf.md) | Equipment that this point belongs to |
| [key](key.md) | Key of the map entry |
| [language](language.md) | Language code (ISO 639-1) of the information content |
| [levelNumber](levelNumber.md) | Floor or level number within a building |
| [locatedIn](locatedIn.md) | Space where this asset is located |
| [MACAddress](MACAddress.md) | MAC address of the asset |
| [maintenanceInterval](maintenanceInterval.md) | Maintenance interval duration |
| [manufacturedBy](manufacturedBy.md) | Agent or resource that manufactured this asset |
| [maxPresValue](maxPresValue.md) | Maximum plausible reading |
| [memberOf](memberOf.md) | Indicates membership in an organization |
| [minPresValue](minPresValue.md) | Minimum plausible reading |
| [modelNumber](modelNumber.md) | Model number of the asset |
| [mountedOn](mountedOn.md) | Building element on which this asset is mounted |
| [name](name.md) | Machine or Human-readable name |
| [operatedBy](operatedBy.md) | Agent or resource that operates this architecture |
| [operationalStageCount](operationalStageCount.md) | The number of operational stages supported by this equipment |
| [ownedBy](ownedBy.md) | Agent or resource that owns this architecture |
| [owns](owns.md) |  Indicates ownership of some thing, e |
| [panel](panel.md) | Parent panel |
| [pointSpecification](pointSpecification.md) | Point specification category as shown in equipment point list |
| [pointType](pointType.md) | Point type - a profile or template name used to refer to the telemetry format... |
| [radius](radius.md) | Radius in meters for circular geofences |
| [scale](scale.md) | Scale factor for raw value conversion |
| [serialNumber](serialNumber.md) | Serial number of the asset |
| [servicedBy](servicedBy.md) | Agent or resource that services this asset |
| [size](size.md) | Size of the information resource in bytes |
| [targetArea](targetArea.md) | Target area for this resource |
| [turnoverDate](turnoverDate.md) | Date when the asset was turned over |
| [unit](unit.md) | Measurement unit (enum key; symbol can be taken from annotations) |
| [url](url.md) | URL or URI pointing to the information resource |
| [value](value.md) | Value of the map entry |
| [version](version.md) | Version identifier for the information |
| [weight](weight.md) | Weight of the asset |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AggregateEnum](AggregateEnum.md) | Aggregation functions for point data processing |
| [PointSpecificationEnum](PointSpecificationEnum.md) | Point specification categories for equipment point lists |
| [QuantityEnum](QuantityEnum.md) | Physical quantities that can be measured or monitored by points |
| [SubstanceEnum](SubstanceEnum.md) | Types of substances that can be fed between equipment |
| [UnitEnum](UnitEnum.md) | Allowed measurement units |


## Types

| Type | Description |
| --- | --- |
| [Any](Any.md) | Any resource or value |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [DurationString](DurationString.md) | ISO 8601 duration format |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
