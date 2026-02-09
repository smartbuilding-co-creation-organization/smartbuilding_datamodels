.PHONY: venv install gen docgen docs serve build deploy validate clean

VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
LINKML=$(VENV)/bin/linkml
GEN_DOC=$(VENV)/bin/gen-doc
MKDOCS=$(VENV)/bin/mkdocs

venv:
	python3 -m venv $(VENV)

install: venv
	$(PIP) install -U pip
	$(PIP) install -r requirements.txt

docgen:
	$(GEN_DOC) --directory docs schema/building_model_shacl.yaml

gen:
	$(LINKML) generate owl --metadata-profile rdfs schema/building_model_owl.yaml -f ttl > output/building_model.owl.ttl
	$(LINKML) generate shacl --non-closed --suffix Shape schema/building_model_shacl.yaml > output/building_model.shacl.ttl
	$(LINKML) generate json-schema schema/building_model_shacl.yaml > output/building_model.schema.json
	$(GEN_DOC) --directory docs schema/building_model_shacl.yaml

validate: gen
	$(PYTHON) scripts/generate_validation_ttl.py --schema schema/building_model_shacl.yaml --cases sample/validation/cases.yaml
	$(PYTHON) scripts/validate_rdf.py --schema schema/building_model_shacl.yaml --ontology output/building_model.owl.ttl --shacl output/building_model.shacl.ttl --cases sample/validation/cases.yaml --use-output-ttl

docs: docgen
	$(MKDOCS) build

serve: docgen
	$(MKDOCS) serve

build: docs

deploy: docgen
	$(MKDOCS) gh-deploy --force --clean

clean:
	rm -rf site
