"""
BS_OS Project Manager v0.4-alpha

Create a standard design project folder from config/project_template.json.

Usage:
  python scripts/project_manager.py --name "Project Name"
  python scripts/project_manager.py --name "Project Name" --client "Client" --designer "Designer" --stage "concept"
  python scripts/project_manager.py --name "Project Name" --root "D:/BS_Projects"

This script uses only Python standard library.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


ROOT_DIR = Path(__file__).resolve().parent.parent
PROJECT_TEMPLATE_FILE = ROOT_DIR / "config" / "project_template.json"
PATHS_FILE = ROOT_DIR / "config" / "paths.json"
LOG_DIR = ROOT_DIR / "logs"
LOG_FILE = LOG_DIR / "project_manager.log"


def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, data: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def sanitize_folder_name(name: str) -> str:
    cleaned = re.sub(r'[\\/:*?"<>|]', "_", name).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned or "未命名项目"


def get_default_projects_root() -> Path:
    try:
        paths_data = read_json(PATHS_FILE)
        configured = paths_data.get("paths", {}).get("projects_root", "")
        if configured:
            return Path(configured).expanduser()
    except Exception:
        pass
    return ROOT_DIR / "projects"


def write_log(lines: List[str]) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write("\n".join(lines))
        file.write("\n" + "-" * 60 + "\n")


def create_project(args: argparse.Namespace) -> Path:
    template = read_json(PROJECT_TEMPLATE_FILE)
    root = Path(args.root).expanduser() if args.root else get_default_projects_root()
    project_name = sanitize_folder_name(args.name)
    project_root = root / project_name

    folders = template.get("folders", [])
    project_root.mkdir(parents=True, exist_ok=True)

    for folder in folders:
        (project_root / folder).mkdir(parents=True, exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    project_data = template.get("default_project_data", {}).copy()
    project_data.update(
        {
            "project_name": args.name,
            "folder_name": project_name,
            "client": args.client or project_data.get("client", ""),
            "designer": args.designer or project_data.get("designer", ""),
            "stage": args.stage or project_data.get("stage", "concept"),
            "created_at": now,
            "updated_at": now,
            "created_by": "BS_OS Project Manager v0.4-alpha",
        }
    )

    project_file_name = template.get("project_file", "project.json")
    write_json(project_root / project_file_name, project_data)

    lines = [
        "BS_OS Project Manager",
        f"Time: {now}",
        f"Project: {args.name}",
        f"Root: {project_root}",
        f"Folders created: {len(folders)}",
        f"Project file: {project_root / project_file_name}",
    ]
    write_log(lines)
    return project_root


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create BS standard project folder.")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--client", default="", help="Client name")
    parser.add_argument("--designer", default="", help="Designer name")
    parser.add_argument("--stage", default="concept", help="Project stage")
    parser.add_argument("--root", default="", help="Projects root folder")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        project_root = create_project(args)
        print("Project created successfully.")
        print(project_root)
        return 0
    except Exception as exc:
        error_lines = [
            "BS_OS Project Manager Error",
            f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            str(exc),
        ]
        print("\n".join(error_lines), file=sys.stderr)
        write_log(error_lines)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
