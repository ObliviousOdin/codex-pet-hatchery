#!/usr/bin/env python3
"""Autonomous hourly pet hatcher for this repo.

Creates the next original pet from the deterministic preset queue, updates the
README table, validates packages, commits, and pushes. Designed for cron jobs.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from hatch_pet import PRESETS, hatch

ROOT = Path(__file__).resolve().parents[1]
CODEX_HOME = Path.home() / ".codex"


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=check)


def update_readme() -> None:
    readme = ROOT / "README.md"
    text = readme.read_text()
    rows = []
    for spec in PRESETS:
        if (ROOT / "pets" / spec.slug / "pet.json").exists():
            rows.append(
                f"| {spec.display_name} | {spec.theme} | ![{spec.display_name} contact sheet](pets/{spec.slug}/previews/{spec.slug}-contact-sheet.png) | `pets/{spec.slug}` |"
            )
    table = "| Pet | Theme | Preview | Install path |\n| --- | --- | --- | --- |\n" + "\n".join(rows)
    text = re.sub(
        r"\| Pet \| Theme \| Preview \| Install path \|\n\| --- \| --- \| --- \| --- \|\n(?:\| .+ \|\n?)+",
        table + "\n",
        text,
    )
    readme.write_text(text)


def main() -> None:
    existing = {p.name for p in (ROOT / "pets").iterdir() if p.is_dir()} if (ROOT / "pets").exists() else set()
    next_spec = next((p for p in PRESETS if p.slug not in existing), None)
    if next_spec is None:
        print("No new preset pet available; repo is already up to date.")
        return
    dest = hatch(next_spec, ROOT, CODEX_HOME)
    update_readme()
    run(["python3", "scripts/validate_all.py"])
    run(["git", "diff", "--check"])
    status = run(["git", "status", "--porcelain"]).stdout.strip()
    if not status:
        print("No changes after hatch.")
        return
    run(["git", "add", "README.md", "pets", "scripts"])
    run(["git", "commit", "-m", f"feat: hatch {next_spec.slug} pet"])
    push = run(["git", "push"], check=False)
    print(push.stdout)
    if push.returncode != 0:
        print(push.stderr)
        raise SystemExit(push.returncode)
    print(f"Hatched {next_spec.display_name}: {dest}")


if __name__ == "__main__":
    main()
