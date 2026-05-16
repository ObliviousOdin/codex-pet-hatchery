#!/usr/bin/env python3
"""Install one Codex pet package into ${CODEX_HOME:-~/.codex}/pets."""
from __future__ import annotations

import argparse
import shutil
import os
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pet", help="Pet slug under ./pets")
    parser.add_argument("--source-root", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--codex-home", default=os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    args = parser.parse_args()

    src = Path(args.source_root) / "pets" / args.pet
    if not (src / "pet.json").exists() or not (src / "spritesheet.webp").exists():
        raise SystemExit(f"missing pet package files in {src}")
    dest = Path(args.codex_home).expanduser() / "pets" / args.pet
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    print(dest)


if __name__ == "__main__":
    main()
