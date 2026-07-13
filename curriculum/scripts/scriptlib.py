#!/usr/bin/env python3
"""Shared, dependency-light helpers for content operations scripts."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


CURRICULUM = Path(__file__).resolve().parents[1]
REPOSITORY = CURRICULUM.parent


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def dump_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def semantic_key(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def parse_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, text
    for index in range(1, len(lines)):
        if lines[index].strip() in {"---", "..."}:
            metadata = yaml.safe_load("".join(lines[1:index])) or {}
            if not isinstance(metadata, dict):
                raise ValueError("front matter must be a mapping")
            return metadata, "".join(lines[index + 1 :])
    raise ValueError("unterminated YAML front matter")


def flatten_ids(value: Any) -> set[str]:
    ids: set[str] = set()
    if isinstance(value, dict):
        candidate = value.get("id")
        if isinstance(candidate, str):
            ids.add(candidate)
        for child in value.values():
            ids.update(flatten_ids(child))
    elif isinstance(value, list):
        for child in value:
            ids.update(flatten_ids(child))
    return ids


def version_tuple(text: str) -> tuple[int, ...]:
    match = re.search(r"(\d+(?:\.\d+)+)", text)
    return tuple(int(part) for part in match.group(1).split(".")) if match else ()


def isolated_environment(report_dir: Path | None = None) -> dict[str, str]:
    target = report_dir or CURRICULUM / "build" / ".xdg"
    env = {
        "PATH": os.environ.get("PATH", ""),
        "LANG": os.environ.get("LANG", "C.UTF-8"),
        "LC_ALL": os.environ.get("LC_ALL", "C.UTF-8"),
        "SOURCE_DATE_EPOCH": os.environ.get("SOURCE_DATE_EPOCH", "1783900800"),
        "HOME": str(target / "home"),
        "XDG_CACHE_HOME": str(target / "cache"),
        "XDG_CONFIG_HOME": str(target / "config"),
        "XDG_DATA_HOME": str(target / "data"),
    }
    for key in ("HOME", "XDG_CACHE_HOME", "XDG_CONFIG_HOME", "XDG_DATA_HOME"):
        Path(env[key]).mkdir(parents=True, exist_ok=True)
    return env


@dataclass
class CommandResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    duration_seconds: float


def run_command(
    command: Iterable[str],
    *,
    cwd: Path,
    timeout: int = 300,
    env: dict[str, str] | None = None,
) -> CommandResult:
    argv = [str(item) for item in command]
    started = time.monotonic()
    completed = subprocess.run(
        argv,
        cwd=cwd,
        env=env or isolated_environment(),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    return CommandResult(
        command=argv,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
        duration_seconds=round(time.monotonic() - started, 3),
    )
