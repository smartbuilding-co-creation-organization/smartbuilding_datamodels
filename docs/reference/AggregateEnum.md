---
search:
  boost: 2.0
---


# Enum: AggregateEnum 




_Aggregation functions for point data processing_




URI: [sbco:AggregateEnum](https://www.sbco.or.jp/ont/AggregateEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| average | None | Average value |
| sum | None | Sum of values |
| minimum | None | Minimum value |
| maximum | None | Maximum value |
| count | None | Count of values |
| first | None | First value |
| last | None | Last value |
| median | None | Median value |
| standardDeviation | None | Standard deviation |




## Slots

| Name | Description |
| ---  | --- |
| [aggregate](aggregate.md) | Aggregation function or method for point data processing |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_ja | ポイントデータ処理のための集約関数 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema






## LinkML Source

<details markdown="1">
```yaml
name: AggregateEnum
annotations:
  description_ja:
    tag: description_ja
    value: ポイントデータ処理のための集約関数
description: Aggregation functions for point data processing
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
permissible_values:
  average:
    text: average
    description: Average value
  sum:
    text: sum
    description: Sum of values
  minimum:
    text: minimum
    description: Minimum value
  maximum:
    text: maximum
    description: Maximum value
  count:
    text: count
    description: Count of values
  first:
    text: first
    description: First value
  last:
    text: last
    description: Last value
  median:
    text: median
    description: Median value
  standardDeviation:
    text: standardDeviation
    description: Standard deviation

```
</details>
