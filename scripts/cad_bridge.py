"""
BS_OS CAD Bridge v0.3

This script prepares the connection between BS_OS, AutoCAD, BS-CAD-Tools and BS-CAD-Standard.

Current scope:
- Read config/cad_bridge.json
- Check whether configured local paths exist
- Check whether the CAD tools loader file exists
- Generate a readable status report
- Write a log file

Future scope:
- Add AutoCAD running detection
- Add real AutoCAD LISP loading bridge
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT_DIR / "config" / "cad_bridge.json"
LOG_DIR = ROOT_DIR / "logs"
LOG_FILE = LOG_DIR / "cad_bridge.log"


def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def resolve_path(path_text: str) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path
    return (ROOT_DIR / path).resolve()


def write_log(lines: List[str]) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write("\n".join(lines))
        file.write("\n" + "-" * 60 + "\n")


def build_status() -> List[str]:
    config = read_json(CONFIG_FILE)

    cad_tools_path = resolve_path(config.get("bs_cad_tools", {}).get("local_path", "../BS-CAD-Tools"))
    cad_standard_path = resolve_path(config.get("bs_cad_standard", {}).get("local_path", "../BS-CAD-Standard"))
    main_loader = config.get("bs_cad_tools", {}).get("main_loader", "BS_CAD_TOOLS_LOAD.lsp")
    loader_path = cad_tools_path / main_loader

    lines = [
        "BS_OS CAD Bridge Status",
        f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"Platform: {sys.platform}",
        "",
        f"BS-CAD-Tools path: {cad_tools_path}",
        f"BS-CAD-Tools exists: {'YES' if cad_tools_path.exists() else 'NO'}",
        f"Main loader: {loader_path}",
        f"Main loader exists: {'YES' if loader_path.exists() else 'NO'}",
        "",
        f"BS-CAD-Standard path: {cad_standard_path}",
        f"BS-CAD-Standard exists: {'YES' if cad_standard_path.exists() else 'NO'}",
        "",
        "Next action:",
    ]

    if not cad_tools_path.exists():
        lines.append("- BS-CAD-Tools local path is missing. Clone or place BS-CAD-Tools beside BS_OS.")
    elif not loader_path.exists():
        lines.append("- Main LISP loader is missing. Create BS_CAD_TOOLS_LOAD.lsp in BS-CAD-Tools.")
    elif not cad_standard_path.exists():
        lines.append("- BS-CAD-Standard local path is missing. Clone or place BS-CAD-Standard beside BS_OS.")
    else:
        lines.append("- Basic path checks passed. Ready for AutoCAD loading integration.")

    return lines


def main() -> int:
    try:
        lines = build_status()
        print("\n".join(lines))
        write_log(lines)
        return 0
    except Exception as exc:
        error_lines = [
            "BS_OS CAD Bridge Error",
            f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            str(exc),
        ]
        print("\n".join(error_lines))
        write_log(error_lines)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
