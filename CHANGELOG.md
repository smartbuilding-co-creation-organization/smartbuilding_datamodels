# Changelog

All notable changes to this project will be documented in this file.

The project follows [Semantic Versioning](https://semver.org/) and uses GitHub
Releases for published release notes.

## [Unreleased]

### Added

- Expanded `UnitEnum` (`sbco:unit`) with canonical keys for energy, power,
  current, volume, volumetric flow, angle, irradiance, speed, and
  precipitation, alongside the existing temperature/percent/ppm values.
  Each permissible value documents its display symbol (`text`) and the raw
  legacy/Japanese symbol variants that normalize to it (`legacy_symbols`,
  e.g. `℃`/`KWH`/`％RH`) — see README "sbco:unit 語彙と正規化" (#35).

## [0.1.0] - 2026-08-04

### Added

- Published the initial LinkML smart-building ontology schema together with
  generated OWL, SHACL, JSON Schema, and MkDocs reference documentation.
- Added RDF/SHACL validation cases and deterministic generation commands.
- Added public contribution, security, citation, licensing, and release
  metadata.

### Changed

- Aligned RDF literal generation with LinkML slot datatypes.
- Renamed the LinkML helper classes `Geometry` and `Georeference` to
  `GeometryInfo` and `GeoreferenceInfo`; their RDF class URIs are unchanged.
- Migrated GitHub Pages deployment to the official GitHub Actions workflow.

[Unreleased]: https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels/releases/tag/v0.1.0
