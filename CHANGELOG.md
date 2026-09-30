# Changelog

All notable changes to this project will be documented in this file.

The project follows [Semantic Versioning](https://semver.org/) and uses GitHub
Releases for published release notes.

## [Unreleased]

## [1.0.0] - 2026-09-30

### Added

- Added a `--unify-prefix sbco` option to `scripts/convert_yaml_to_ttl.py` that
  emits `sbco:`-only RDF for consumers that do not run OWL-RL reasoning. The
  default (canonical `rec:`/`brick:`) output is unchanged (#34).
- Added `scripts/check_ttl_drift.py`, used by CI to detect generated-artifact
  drift in `output/*.ttl` via graph isomorphism rather than a raw text diff (#34).
- Expanded `UnitEnum` (`sbco:unit`) with canonical keys for energy, power,
  current, volume, volumetric flow, angle, irradiance, speed, and
  precipitation, alongside the existing temperature/percent/ppm values.
  Each permissible value documents its display symbol (`text`) and the raw
  legacy/Japanese symbol variants that normalize to it (`legacy_symbols`,
  e.g. `℃`/`KWH`/`％RH`) — see README "sbco:unit 語彙と正規化" (#35).
- Added `scripts/postprocess_shacl.py`, run as part of `make gen`: downgrades
  `sbco:unit`'s `sh:in` constraint from the default blocking `sh:Violation`
  to advisory `sh:Warning` severity, since the unit vocabulary is still
  provisional pending SBCO/GUTP working-group agreement. An out-of-vocabulary
  unit is now reported in the SHACL validation results but no longer fails
  `conforms` / blocks an otherwise-valid import (#36).

### Changed

- The generated OWL now contains real `owl:equivalentClass` /
  `owl:equivalentProperty` axioms derived from `exact_mappings`, so a reasoner
  can treat `sbco:` terms and their `rec:`/`brick:` counterparts as equivalent.
  `hasPoint`/`isPointOf` now declare `range: Resource` and are emitted as
  `owl:ObjectProperty` (#34).
- Restructured the getting-started guide (`docs/guide/getting_started.md`) into
  concept, implementation-example, and project parts, following the review
  feedback in #37 (#38).

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

[Unreleased]: https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels/releases/tag/v1.0.0
[0.1.0]: https://github.com/smartbuilding-co-creation-organization/smartbuilding_datamodels/releases/tag/v0.1.0
