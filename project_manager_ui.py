"""
BS_OS Project Manager UI v0.4-alpha

A small Tkinter interface for creating standard design project folders.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


ROOT_DIR = Path(__file__).resolve().parent
PATHS_FILE = ROOT_DIR / "config" / "paths.json"
SCRIPT_FILE = ROOT_DIR / "scripts" / "project_manager.py"


class ProjectManagerUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("BS Project Manager v0.4-alpha")
        self.geometry("640x420")
        self.minsize(560, 380)
        self.project_root_var = tk.StringVar(value=str(self.get_default_projects_root()))
        self.project_name_var = tk.StringVar()
        self.client_var = tk.StringVar()
        self.designer_var = tk.StringVar()
        self.stage_var = tk.StringVar(value="concept")
        self._build_ui()

    def _build_ui(self) -> None:
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="BS Project Manager", font=("Microsoft YaHei UI", 18, "bold")).grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 16))

        ttk.Label(frame, text="项目名称 *").grid(row=1, column=0, sticky="w", pady=6)
        ttk.Entry(frame, textvariable=self.project_name_var).grid(row=1, column=1, columnspan=2, sticky="ew", pady=6)

        ttk.Label(frame, text="客户名称").grid(row=2, column=0, sticky="w", pady=6)
        ttk.Entry(frame, textvariable=self.client_var).grid(row=2, column=1, columnspan=2, sticky="ew", pady=6)

        ttk.Label(frame, text="设计师").grid(row=3, column=0, sticky="w", pady=6)
        ttk.Entry(frame, textvariable=self.designer_var).grid(row=3, column=1, columnspan=2, sticky="ew", pady=6)

        ttk.Label(frame, text="阶段").grid(row=4, column=0, sticky="w", pady=6)
        stage_box = ttk.Combobox(frame, textvariable=self.stage_var, values=["concept", "design", "drawing", "rendering", "delivery", "archive"])
        stage_box.grid(row=4, column=1, columnspan=2, sticky="ew", pady=6)

        ttk.Label(frame, text="项目根目录").grid(row=5, column=0, sticky="w", pady=6)
        ttk.Entry(frame, textvariable=self.project_root_var).grid(row=5, column=1, sticky="ew", pady=6)
        ttk.Button(frame, text="选择", command=self.choose_root).grid(row=5, column=2, sticky="e", padx=(8, 0), pady=6)

        ttk.Separator(frame).grid(row=6, column=0, columnspan=3, sticky="ew", pady=16)

        ttk.Button(frame, text="创建标准项目", command=self.create_project).grid(row=7, column=0, columnspan=3, sticky="ew", ipady=6)
        ttk.Button(frame, text="打开项目根目录", command=self.open_projects_root).grid(row=8, column=0, columnspan=3, sticky="ew", pady=(10, 0))

        self.status_var = tk.StringVar(value="准备就绪")
        ttk.Label(frame, textvariable=self.status_var).grid(row=9, column=0, columnspan=3, sticky="w", pady=(16, 0))

    def choose_root(self) -> None:
        selected = filedialog.askdirectory(title="选择项目根目录")
        if selected:
            self.project_root_var.set(selected)

    def create_project(self) -> None:
        name = self.project_name_var.get().strip()
        if not name:
            messagebox.showwarning("缺少项目名称", "请输入项目名称。")
            return

        command = [
            sys.executable,
            str(SCRIPT_FILE),
            "--name",
            name,
            "--client",
            self.client_var.get().strip(),
            "--designer",
            self.designer_var.get().strip(),
            "--stage",
            self.stage_var.get().strip() or "concept",
            "--root",
            self.project_root_var.get().strip(),
        ]

        try:
            result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="ignore", check=False)
            if result.returncode == 0:
                created_path = result.stdout.strip().splitlines()[-1]
                self.status_var.set(f"已创建：{created_path}")
                messagebox.showinfo("创建完成", f"项目已创建：\n{created_path}")
                self.open_path(Path(created_path))
            else:
                messagebox.showerror("创建失败", result.stderr or result.stdout)
        except Exception as exc:
            messagebox.showerror("创建失败", str(exc))

    def open_projects_root(self) -> None:
        self.open_path(Path(self.project_root_var.get().strip()))

    def open_path(self, path: Path) -> None:
        path.mkdir(parents=True, exist_ok=True)
        if sys.platform.startswith("win"):
            os.startfile(path)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(path)])
        else:
            subprocess.Popen(["xdg-open", str(path)])

    @staticmethod
    def get_default_projects_root() -> Path:
        try:
            with PATHS_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)
            configured = data.get("paths", {}).get("projects_root", "")
            if configured:
                return Path(configured).expanduser()
        except Exception:
            pass
        return ROOT_DIR / "projects"


if __name__ == "__main__":
    app = ProjectManagerUI()
    app.mainloop()
