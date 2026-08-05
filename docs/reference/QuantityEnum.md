---
search:
  boost: 2.0
---


# Enum: QuantityEnum 




_Physical quantities that can be measured or monitored by points_




URI: [sbco:QuantityEnum](https://www.sbco.or.jp/ont/QuantityEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Absolute_Humidity | None | Absolute humidity measurement |
| Acceleration_Time | None | Time required for acceleration |
| Active_Energy | None | Active electrical energy |
| Active_Power | None | Active electrical power |
| Air_Quality | None | Air quality measurement |
| Alternating_Current_Frequency | None | AC frequency measurement |
| Ammonia_Concentration | None | Ammonia concentration in air |
| Angle | None | Angular measurement |
| Apparent_Energy | None | Apparent electrical energy |
| Apparent_Power | None | Apparent electrical power |
| Atmospheric_Pressure | None | Atmospheric pressure measurement |
| CO2_Concentration | None | Carbon dioxide concentration |
| CO_Concentration | None | Carbon monoxide concentration |
| Capacity | None | Storage or processing capacity |
| Cloudage | None | Cloud coverage measurement |
| Complex_Power | None | Complex electrical power |
| Conductivity | None | Electrical or thermal conductivity |
| Current_Angle | None | Electrical current phase angle |
| Current_Imbalance | None | Current imbalance in multi-phase systems |
| Current_Total_Harmonic_Distortion | None | Total harmonic distortion of current |
| Deceleration_Time | None | Time required for deceleration |
| Dewpoint | None | Dew point temperature |
| Differential_CO2_Concentration | None | Differential carbon dioxide concentration |
| Differential_CO_Concentration | None | Differential carbon monoxide concentration |
| Differential_Dry_Bulb_Temperature | None | Temperature difference (dry bulb) |
| Differential_Dynamic_Pressure | None | Dynamic pressure difference |
| Differential_Pressure | None | Pressure difference measurement |
| Differential_Static_Pressure | None | Static pressure difference |
| Differential_Temperature | None | Temperature difference |
| Direction | None | Directional measurement |
| Dry_Bulb_Temperature | None | Dry bulb temperature |
| Dynamic_Pressure | None | Dynamic pressure measurement |
| Electric_Current | None | Electrical current measurement |
| Electric_Energy | None | Electrical energy measurement |
| Electric_Power | None | Electrical power measurement |
| Energy | None | General energy measurement |
| Enthalpy | None | Enthalpy measurement |
| Flow | None | Flow rate measurement |
| Flow_Loss | None | Flow loss measurement |
| Formaldehyde_Concentration | None | Formaldehyde concentration in air |
| Frequency | None | Frequency measurement |
| GrainsOfMoisture | None | Moisture content in grains per pound |
| Humidity | None | General humidity measurement |
| Illuminance | None | Illuminance measurement |
| Irradiance | None | Irradiance measurement |
| Level | None | Level measurement |
| Linear_Speed | None | Linear speed measurement |
| Luminance | None | Luminance measurement |
| Luminous_Flux | None | Luminous flux measurement |
| Luminous_Intensity | None | Luminance intensity measurement |
| Mass | None | Mass measurement |
| Methane_Concentration | None | Methane concentration in air |
| NO2_Concentration | None | Nitrogen dioxide concentration |
| Occupancy | None | Occupancy detection |
| Occupancy_Count | None | Number of occupants |
| Occupancy_Percentage | None | Occupancy percentage |
| Operative_Temperature | None | Operative temperature measurement |
| Ozone_Concentration | None | Ozone concentration in air |
| PM10_Concentration | None | PM10 particulate matter concentration |
| PM1_Concentration | None | PM1 particulate matter concentration |
| PM2_5_Concentration | None | PM2 |
| Peak_Power | None | Peak power measurement |
| Phasor | None | Phasor measurement |
| Phasor_Angle | None | Phasor angle measurement |
| Phasor_Magnitude | None | Phasor magnitude measurement |
| Position | None | Position measurement |
| Power | None | General power measurement |
| Power_Factor | None | Power factor measurement |
| Precipitation | None | Precipitation measurement |
| Pressure | None | General pressure measurement |
| Radiance | None | Radiance measurement |
| Radiant_Temperature | None | Radiant temperature measurement |
| Radioactivity_Concentration | None | Radioactivity concentration |
| Radon_Concentration | None | Radon concentration in air |
| Reactive_Energy | None | Reactive electrical energy |
| Reactive_Power | None | Reactive electrical power |
| Real_Power | None | Real electrical power |
| Relative_Humidity | None | Relative humidity measurement |
| Rotational_Speed | None | Rotational speed measurement |
| Solar_Irradiance | None | Solar irradiance measurement |
| Solar_Radiance | None | Solar radiance measurement |
| Speed | None | General speed measurement |
| Static_Pressure | None | Static pressure measurement |
| TVOC_Concentration | None | Total volatile organic compounds concentration |
| Temperature | None | General temperature measurement |
| Thermal_Energy | None | Thermal energy measurement |
| Thermal_Power | None | Thermal power measurement |
| Time | None | Time measurement |
| Torque | None | Torque measurement |
| Velocity_Pressure | None | Velocity pressure measurement |
| Voltage | None | Electrical voltage measurement |
| Voltage_Angle | None | Voltage phase angle |
| Voltage_Imbalance | None | Voltage imbalance in multi-phase systems |
| Weather_Condition | None | Weather condition measurement |
| Wet_Bulb_Temperature | None | Wet bulb temperature measurement |
| Wind_Direction | None | Wind direction measurement |




## Slots

| Name | Description |
| ---  | --- |
| [hasQuantity](hasQuantity.md) | Physical quantity measured by this point |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_ja | ポイントで測定・監視可能な物理量 |




### Schema Source


* from schema: https://www.sbco.or.jp/ont/schema






## LinkML Source

<details markdown="1">
```yaml
name: QuantityEnum
annotations:
  description_ja:
    tag: description_ja
    value: ポイントで測定・監視可能な物理量
description: Physical quantities that can be measured or monitored by points
from_schema: https://www.sbco.or.jp/ont/schema
rank: 1000
permissible_values:
  Absolute_Humidity:
    text: Absolute_Humidity
    description: Absolute humidity measurement
  Acceleration_Time:
    text: Acceleration_Time
    description: Time required for acceleration
  Active_Energy:
    text: Active_Energy
    description: Active electrical energy
  Active_Power:
    text: Active_Power
    description: Active electrical power
  Air_Quality:
    text: Air_Quality
    description: Air quality measurement
  Alternating_Current_Frequency:
    text: Alternating_Current_Frequency
    description: AC frequency measurement
  Ammonia_Concentration:
    text: Ammonia_Concentration
    description: Ammonia concentration in air
  Angle:
    text: Angle
    description: Angular measurement
  Apparent_Energy:
    text: Apparent_Energy
    description: Apparent electrical energy
  Apparent_Power:
    text: Apparent_Power
    description: Apparent electrical power
  Atmospheric_Pressure:
    text: Atmospheric_Pressure
    description: Atmospheric pressure measurement
  CO2_Concentration:
    text: CO2_Concentration
    description: Carbon dioxide concentration
  CO_Concentration:
    text: CO_Concentration
    description: Carbon monoxide concentration
  Capacity:
    text: Capacity
    description: Storage or processing capacity
  Cloudage:
    text: Cloudage
    description: Cloud coverage measurement
  Complex_Power:
    text: Complex_Power
    description: Complex electrical power
  Conductivity:
    text: Conductivity
    description: Electrical or thermal conductivity
  Current_Angle:
    text: Current_Angle
    description: Electrical current phase angle
  Current_Imbalance:
    text: Current_Imbalance
    description: Current imbalance in multi-phase systems
  Current_Total_Harmonic_Distortion:
    text: Current_Total_Harmonic_Distortion
    description: Total harmonic distortion of current
  Deceleration_Time:
    text: Deceleration_Time
    description: Time required for deceleration
  Dewpoint:
    text: Dewpoint
    description: Dew point temperature
  Differential_CO2_Concentration:
    text: Differential_CO2_Concentration
    description: Differential carbon dioxide concentration
  Differential_CO_Concentration:
    text: Differential_CO_Concentration
    description: Differential carbon monoxide concentration
  Differential_Dry_Bulb_Temperature:
    text: Differential_Dry_Bulb_Temperature
    description: Temperature difference (dry bulb)
  Differential_Dynamic_Pressure:
    text: Differential_Dynamic_Pressure
    description: Dynamic pressure difference
  Differential_Pressure:
    text: Differential_Pressure
    description: Pressure difference measurement
  Differential_Static_Pressure:
    text: Differential_Static_Pressure
    description: Static pressure difference
  Differential_Temperature:
    text: Differential_Temperature
    description: Temperature difference
  Direction:
    text: Direction
    description: Directional measurement
  Dry_Bulb_Temperature:
    text: Dry_Bulb_Temperature
    description: Dry bulb temperature
  Dynamic_Pressure:
    text: Dynamic_Pressure
    description: Dynamic pressure measurement
  Electric_Current:
    text: Electric_Current
    description: Electrical current measurement
  Electric_Energy:
    text: Electric_Energy
    description: Electrical energy measurement
  Electric_Power:
    text: Electric_Power
    description: Electrical power measurement
  Energy:
    text: Energy
    description: General energy measurement
  Enthalpy:
    text: Enthalpy
    description: Enthalpy measurement
  Flow:
    text: Flow
    description: Flow rate measurement
  Flow_Loss:
    text: Flow_Loss
    description: Flow loss measurement
  Formaldehyde_Concentration:
    text: Formaldehyde_Concentration
    description: Formaldehyde concentration in air
  Frequency:
    text: Frequency
    description: Frequency measurement
  GrainsOfMoisture:
    text: GrainsOfMoisture
    description: Moisture content in grains per pound
  Humidity:
    text: Humidity
    description: General humidity measurement
  Illuminance:
    text: Illuminance
    description: Illuminance measurement
  Irradiance:
    text: Irradiance
    description: Irradiance measurement
  Level:
    text: Level
    description: Level measurement
  Linear_Speed:
    text: Linear_Speed
    description: Linear speed measurement
  Luminance:
    text: Luminance
    description: Luminance measurement
  Luminous_Flux:
    text: Luminous_Flux
    description: Luminous flux measurement
  Luminous_Intensity:
    text: Luminous_Intensity
    description: Luminance intensity measurement
  Mass:
    text: Mass
    description: Mass measurement
  Methane_Concentration:
    text: Methane_Concentration
    description: Methane concentration in air
  NO2_Concentration:
    text: NO2_Concentration
    description: Nitrogen dioxide concentration
  Occupancy:
    text: Occupancy
    description: Occupancy detection
  Occupancy_Count:
    text: Occupancy_Count
    description: Number of occupants
  Occupancy_Percentage:
    text: Occupancy_Percentage
    description: Occupancy percentage
  Operative_Temperature:
    text: Operative_Temperature
    description: Operative temperature measurement
  Ozone_Concentration:
    text: Ozone_Concentration
    description: Ozone concentration in air
  PM10_Concentration:
    text: PM10_Concentration
    description: PM10 particulate matter concentration
  PM1_Concentration:
    text: PM1_Concentration
    description: PM1 particulate matter concentration
  PM2_5_Concentration:
    text: PM2_5_Concentration
    description: PM2.5 particulate matter concentration
  Peak_Power:
    text: Peak_Power
    description: Peak power measurement
  Phasor:
    text: Phasor
    description: Phasor measurement
  Phasor_Angle:
    text: Phasor_Angle
    description: Phasor angle measurement
  Phasor_Magnitude:
    text: Phasor_Magnitude
    description: Phasor magnitude measurement
  Position:
    text: Position
    description: Position measurement
  Power:
    text: Power
    description: General power measurement
  Power_Factor:
    text: Power_Factor
    description: Power factor measurement
  Precipitation:
    text: Precipitation
    description: Precipitation measurement
  Pressure:
    text: Pressure
    description: General pressure measurement
  Radiance:
    text: Radiance
    description: Radiance measurement
  Radiant_Temperature:
    text: Radiant_Temperature
    description: Radiant temperature measurement
  Radioactivity_Concentration:
    text: Radioactivity_Concentration
    description: Radioactivity concentration
  Radon_Concentration:
    text: Radon_Concentration
    description: Radon concentration in air
  Reactive_Energy:
    text: Reactive_Energy
    description: Reactive electrical energy
  Reactive_Power:
    text: Reactive_Power
    description: Reactive electrical power
  Real_Power:
    text: Real_Power
    description: Real electrical power
  Relative_Humidity:
    text: Relative_Humidity
    description: Relative humidity measurement
  Rotational_Speed:
    text: Rotational_Speed
    description: Rotational speed measurement
  Solar_Irradiance:
    text: Solar_Irradiance
    description: Solar irradiance measurement
  Solar_Radiance:
    text: Solar_Radiance
    description: Solar radiance measurement
  Speed:
    text: Speed
    description: General speed measurement
  Static_Pressure:
    text: Static_Pressure
    description: Static pressure measurement
  TVOC_Concentration:
    text: TVOC_Concentration
    description: Total volatile organic compounds concentration
  Temperature:
    text: Temperature
    description: General temperature measurement
  Thermal_Energy:
    text: Thermal_Energy
    description: Thermal energy measurement
  Thermal_Power:
    text: Thermal_Power
    description: Thermal power measurement
  Time:
    text: Time
    description: Time measurement
  Torque:
    text: Torque
    description: Torque measurement
  Velocity_Pressure:
    text: Velocity_Pressure
    description: Velocity pressure measurement
  Voltage:
    text: Voltage
    description: Electrical voltage measurement
  Voltage_Angle:
    text: Voltage_Angle
    description: Voltage phase angle
  Voltage_Imbalance:
    text: Voltage_Imbalance
    description: Voltage imbalance in multi-phase systems
  Weather_Condition:
    text: Weather_Condition
    description: Weather condition measurement
  Wet_Bulb_Temperature:
    text: Wet_Bulb_Temperature
    description: Wet bulb temperature measurement
  Wind_Direction:
    text: Wind_Direction
    description: Wind direction measurement

```
</details>
