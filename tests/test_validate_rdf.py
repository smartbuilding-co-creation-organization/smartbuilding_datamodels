from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_rdf


def make_case() -> validate_rdf.ValidationCase:
    return validate_rdf.ValidationCase(
        name="test",
        input_path=ROOT / "sample" / "buildingA.yaml",
        output_ttl=None,
        root_class="Site",
        class_chain=["Site", "Building", "Level", "Room"],
        inject_is_part_of=False,
        expected=validate_rdf.CaseExpectation(shacl_conforms=True, inferred_types=[]),
    )


def test_build_conversion_config_uses_defaults() -> None:
    case = make_case()
    config = validate_rdf.build_conversion_config(case)

    assert config.root_class == "Site"
    assert config.class_chain == ["Site", "Building", "Level", "Room"]
    assert config.inject_is_part_of is False
    assert config.instance_prefix == "ex"
    assert config.instance_base == "https://example.com/"
