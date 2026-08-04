# Changelog

All notable changes to this project will be documented in this file.

The project follows [Semantic Versioning](https://semver.org/) and uses GitHub
Releases for published release notes.

## [Unreleased]

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
