#!/usr/bin/env python3
from __future__ import annotations

import argparse
import logging
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

LOGGER = logging.getLogger(__name__)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping at root of {path}, got {type(data)}")
    return data


def parse_cases(path: Path) -> list[dict[str, Any]]:
    raw = load_yaml(path)
    cases_raw = raw.get("cases")
    if not isinstance(cases_raw, list):
        raise ValueError("cases must be a list")
    return cases_raw


def run_converter(schema: Path, case: dict[str, Any]) -> None:
    name = case.get("name", "<unnamed>")
    input_path = Path(case["input"])
    output_ttl = case.get("output_ttl")
    if not output_ttl:
        raise ValueError(f"Case {name} missing output_ttl")
    output_path = Path(output_ttl)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        sys.executable,
        "scripts/convert_yaml_to_ttl.py",
        str(schema),
        str(input_path),
        str(output_path),
        "--root-class",
        str(case.get("root_class", "Site")),
        "--class-chain",
        ",".join(case.get("class_chain", ["Site", "Building", "Level", "Room"])),
    ]
    if case.get("inject_is_part_of", False):
        cmd.append("--inject-is-part-of")

    LOGGER.info("Converting case %s", name)
    subprocess.run(cmd, check=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate TTL files for validation cases using convert_yaml_to_ttl.py.",
    )
    parser.add_argument(
        "--schema",
        default="schema/building_model_shacl.yaml",
        type=Path,
        help="LinkML schema YAML path.",
    )
    parser.add_argument(
        "--cases",
        default="sample/validation/cases.yaml",
        type=Path,
        help="YAML file describing validation cases.",
    )
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = parse_args()
    cases = parse_cases(args.cases)
    if not cases:
        raise ValueError("No cases found")
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("each case must be a mapping")
        run_converter(args.schema, case)
    LOGGER.info("All case TTL files generated")


if __name__ == "__main__":
    main()
