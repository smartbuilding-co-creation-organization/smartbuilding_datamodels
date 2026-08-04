param(
  [Parameter(Position=0)]
  [ValidateSet("venv","install","gen","docgen","docs","serve","build","deploy","validate","clean","help")]
  [string]$Target = "help"
)

$ErrorActionPreference = "Stop"
$env:PYTHONHASHSEED = "0"

$VENV = ".venv"
$PY  = Join-Path $VENV "Scripts\python.exe"
$PIP = Join-Path $VENV "Scripts\pip.exe"
$LINKML  = Join-Path $VENV "Scripts\linkml.exe"
$GEN_DOC = Join-Path $VENV "Scripts\gen-doc.exe"
$MKDOCS  = Join-Path $VENV "Scripts\mkdocs.exe"

function Ensure-Venv {
  if (-not (Test-Path $PY)) {
    Write-Host "Creating venv: $VENV"
    py -3 -m venv $VENV
  }
}

function Ensure-Dir([string]$Path) {
  if (-not (Test-Path $Path)) { New-Item -ItemType Directory -Path $Path | Out-Null }
}

function Invoke-Docgen {
  Ensure-Venv
  & $GEN_DOC --directory docs schema/building_model_shacl.yaml
}

function Invoke-Generation {
  Ensure-Venv
  Ensure-Dir "output"

  # stdout redirection must preserve UTF-8 on Windows PowerShell.
  & $LINKML generate owl --metadata-profile rdfs schema/building_model_owl.yaml -f ttl |
    Out-File -Encoding utf8 "output/building_model.owl.ttl"

  & $LINKML generate shacl --non-closed --suffix Shape schema/building_model_shacl.yaml |
    Out-File -Encoding utf8 "output/building_model.shacl.ttl"

  & $LINKML generate json-schema schema/building_model_shacl.yaml |
    Out-File -Encoding utf8 "output/building_model.schema.json"

  Invoke-Docgen
}

switch ($Target) {
  "venv" {
    Ensure-Venv
  }

  "install" {
    Ensure-Venv
    & $PIP install -U pip
    & $PIP install -r requirements.txt
  }

  "docgen" {
    Invoke-Docgen
  }

  "gen" {
    Invoke-Generation
  }

  "docs" {
    Invoke-Docgen
    & $MKDOCS build
  }

  "serve" {
    Invoke-Docgen
    & $MKDOCS serve
  }

  "build" {
    Invoke-Docgen
    & $MKDOCS build
  }

  "deploy" {
    Invoke-Docgen
    & $MKDOCS gh-deploy --force --clean
  }

  "validate" {
    Invoke-Generation
    & $PY scripts/generate_validation_ttl.py --schema schema/building_model_shacl.yaml --cases sample/validation/cases.yaml
    & $PY scripts/validate_rdf.py --schema schema/building_model_shacl.yaml --ontology output/building_model.owl.ttl --shacl output/building_model.shacl.ttl --cases sample/validation/cases.yaml --use-output-ttl
  }

  "clean" {
    if (Test-Path "site") { Remove-Item -Recurse -Force "site" }
  }

  "help" {
    @"
Usage:
  powershell -ExecutionPolicy Bypass -File .\make.ps1 <target>

Targets:
  venv     : create .venv if missing
  install  : venv + pip upgrade + install requirements.txt
  docgen   : gen-doc --directory docs schema/building_model_shacl.yaml
  gen      : linkml generate (owl/shacl/json-schema) + docgen
  docs     : docgen + mkdocs build
  serve    : docgen + mkdocs serve
  build    : same as docs
  deploy   : docgen + mkdocs gh-deploy --force --clean
  validate : generate_validation_ttl.py + scripts/validate_rdf.py (sample/validation)
  clean    : remove site/
"@ | Write-Host
  }
}
