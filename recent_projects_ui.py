"""
BS_OS Recent Projects UI v0.4-beta

List and open recent projects recorded by Project Manager.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk
from typing import Any, Dict, List


ROOT_DIR = Path(__file__).resolve().parent
RECENT_PROJECTS_FILE = ROOT_DIR / "data" / "recent_projects.json"


class RecentProjectsUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("BS Recent Projects v0.4-beta")
        self.geometry("880x520")
        self.minsize(760, 440)
        self.projects: List[Dict[str, Any]] = []
        self._build_ui()
        self.reload_projects()

    def _build_ui(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        header = ttk.Frame(self, padding=(16, 14, 16, 8))
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(0, weight=1)

        ttk.Label(header, text="最近项目", font=("Microsoft YaHei UI", 18, "bold")).grid(row=0, column=0, sticky="w")
        ttk.Button(header, text="刷新", command=self.reload_projects).grid(row=0, column=1, sticky="e")

        columns = ("project_name", "client", "stage", "last_opened_at", "path")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("project_name", text="项目名称")
        self.tree.heading("client", text="客户")
        self.tree.heading("stage", text="阶段")
        self.tree.heading("last_opened_at", text="最近时间")
        self.tree.heading("path", text="路径")
        self.tree.column("project_name", width=180)
        self.tree.column("client", width=120)
        self.tree.column("stage", width=90)
        self.tree.column("last_opened_at", width=150)
        self.tree.column("path", width=320)
        self.tree.grid(row=1, column=0, sticky="nsew", padx=16, pady=8)
        self.tree.bind("<Double-1>", lambda _event: self.open_selected_project())

        footer = ttk.Frame(self, padding=(16, 8, 16, 14))
        footer.grid(row=2, column=0, sticky="ew")
        footer.columnconfigure(0, weight=1)

        self.status_var = tk.StringVar(value="准备就绪")
        ttk.Label(footer, textvariable=self.status_var).grid(row=0, column=0, sticky="w")
        ttk.Button(footer, text="打开项目目录", command=self.open_selected_project).grid(row=0, column=1, padx=(8, 0))
        ttk.Button(footer, text="打开 project.json", command=self.open_selected_project_file).grid(row=0, column=2, padx=(8, 0))

    def reload_projects(self) -> None:
        self.projects = self.load_projects()
        for item in self.tree.get_children():
            self.tree.delete(item)

        for index, project in enumerate(self.projects):
            self.tree.insert(
                "",
                tk.END,
                iid=str(index),
                values=(
                    project.get("project_name", ""),
                    project.get("client", ""),
                    project.get("stage", ""),
                    project.get("last_opened_at", ""),
                    project.get("path", ""),
                ),
            )

        self.status_var.set(f"已加载 {len(self.projects)} 个最近项目")

    def load_projects(self) -> List[Dict[str, Any]]:
        if not RECENT_PROJECTS_FILE.exists():
            return []
        try:
            with RECENT_PROJECTS_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return data.get("projects", [])
        except Exception as exc:
            messagebox.showerror("读取失败", f"无法读取 recent_projects.json\n\n{exc}")
            return []

    def get_selected_project(self) -> Dict[str, Any] | None:
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("未选择项目", "请先选择一个项目。")
            return None
        return self.projects[int(selected[0])]

    def open_selected_project(self) -> None:
        project = self.get_selected_project()
        if not project:
            return
        self.open_path(Path(project.get("path", "")))

    def open_selected_project_file(self) -> None:
        project = self.get_selected_project()
        if not project:
            return
        project_file = project.get("project_file") or str(Path(project.get("path", "")) / "project.json")
        self.open_path(Path(project_file), create_folder=False)

    def open_path(self, path: Path, create_folder: bool = True) -> None:
        if create_folder and not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            messagebox.showwarning("路径不存在", f"路径不存在：\n{path}")
            return

        if sys.platform.startswith("win"):
            os.startfile(path)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(path)])
        else:
            subprocess.Popen(["xdg-open", str(path)])


if __name__ == "__main__":
    app = RecentProjectsUI()
    app.mainloop()
