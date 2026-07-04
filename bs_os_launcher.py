"""
BS_OS Launcher v0.2

A minimal desktop launcher for BS Toolkit modules.

Features:
- Read modules.json
- Group modules by category
- Show enabled / disabled module status
- Launch module entry scripts
- Open module config files
- Open project template config

This version intentionally uses only Python standard library.
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


APP_TITLE = "BS_OS Launcher v0.2"
ROOT_DIR = Path(__file__).resolve().parent
MODULES_FILE = ROOT_DIR / "modules.json"
APP_CONFIG_FILE = ROOT_DIR / "config" / "app.json"
PATHS_CONFIG_FILE = ROOT_DIR / "config" / "paths.json"
PROJECT_TEMPLATE_FILE = ROOT_DIR / "config" / "project_template.json"


class BSOSLauncher(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("980x640")
        self.minsize(860, 560)

        self.modules: List[Dict[str, Any]] = []
        self.selected_module: Dict[str, Any] | None = None

        self._build_ui()
        self.reload_modules()

    def _build_ui(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        header = ttk.Frame(self, padding=(16, 14, 16, 8))
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(0, weight=1)

        title = ttk.Label(header, text="BS_OS", font=("Microsoft YaHei UI", 22, "bold"))
        title.grid(row=0, column=0, sticky="w")

        subtitle = ttk.Label(
            header,
            text="启动器 / 模块管理器 / 项目入口",
            font=("Microsoft YaHei UI", 10),
        )
        subtitle.grid(row=1, column=0, sticky="w", pady=(4, 0))

        reload_btn = ttk.Button(header, text="刷新模块", command=self.reload_modules)
        reload_btn.grid(row=0, column=1, rowspan=2, sticky="e")

        main = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        main.grid(row=1, column=0, sticky="nsew", padx=16, pady=10)

        left = ttk.Frame(main, padding=8)
        right = ttk.Frame(main, padding=8)
        main.add(left, weight=3)
        main.add(right, weight=2)

        left.columnconfigure(0, weight=1)
        left.rowconfigure(1, weight=1)

        ttk.Label(left, text="模块列表", font=("Microsoft YaHei UI", 12, "bold")).grid(row=0, column=0, sticky="w")

        columns = ("name", "type", "category", "status", "enabled")
        self.tree = ttk.Treeview(left, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("name", text="名称")
        self.tree.heading("type", text="类型")
        self.tree.heading("category", text="分类")
        self.tree.heading("status", text="状态")
        self.tree.heading("enabled", text="启用")
        self.tree.column("name", width=210)
        self.tree.column("type", width=130)
        self.tree.column("category", width=100)
        self.tree.column("status", width=140)
        self.tree.column("enabled", width=70, anchor="center")
        self.tree.grid(row=1, column=0, sticky="nsew", pady=(8, 0))
        self.tree.bind("<<TreeviewSelect>>", self.on_module_select)

        scrollbar = ttk.Scrollbar(left, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=1, column=1, sticky="ns", pady=(8, 0))
        self.tree.configure(yscrollcommand=scrollbar.set)

        right.columnconfigure(0, weight=1)
        right.rowconfigure(1, weight=1)

        ttk.Label(right, text="模块详情", font=("Microsoft YaHei UI", 12, "bold")).grid(row=0, column=0, sticky="w")

        self.detail_text = tk.Text(right, height=16, wrap="word", state="disabled")
        self.detail_text.grid(row=1, column=0, sticky="nsew", pady=(8, 10))

        actions = ttk.Frame(right)
        actions.grid(row=2, column=0, sticky="ew")
        actions.columnconfigure((0, 1), weight=1)

        ttk.Button(actions, text="启动模块", command=self.launch_selected_module).grid(row=0, column=0, sticky="ew", padx=(0, 6))
        ttk.Button(actions, text="打开配置", command=self.open_selected_config).grid(row=0, column=1, sticky="ew", padx=(6, 0))
        ttk.Button(actions, text="打开项目模板", command=lambda: self.open_path(PROJECT_TEMPLATE_FILE)).grid(row=1, column=0, sticky="ew", pady=(8, 0), padx=(0, 6))
        ttk.Button(actions, text="打开仓库目录", command=lambda: self.open_path(ROOT_DIR)).grid(row=1, column=1, sticky="ew", pady=(8, 0), padx=(6, 0))

        footer = ttk.Frame(self, padding=(16, 0, 16, 12))
        footer.grid(row=2, column=0, sticky="ew")
        footer.columnconfigure(0, weight=1)
        self.status_var = tk.StringVar(value="准备就绪")
        ttk.Label(footer, textvariable=self.status_var).grid(row=0, column=0, sticky="w")

    def reload_modules(self) -> None:
        try:
            data = self.read_json(MODULES_FILE)
            self.modules = data.get("modules", [])
        except Exception as exc:
            messagebox.showerror("读取失败", f"无法读取 modules.json\n\n{exc}")
            self.modules = []

        for item in self.tree.get_children():
            self.tree.delete(item)

        for index, module in enumerate(self.modules):
            enabled_text = "是" if module.get("enabled") else "否"
            self.tree.insert(
                "",
                tk.END,
                iid=str(index),
                values=(
                    module.get("name", ""),
                    module.get("type", ""),
                    module.get("category", ""),
                    module.get("status", ""),
                    enabled_text,
                ),
            )

        self.status_var.set(f"已加载 {len(self.modules)} 个模块")
        self.clear_detail()

    def on_module_select(self, _event: tk.Event) -> None:
        selected = self.tree.selection()
        if not selected:
            self.selected_module = None
            self.clear_detail()
            return

        index = int(selected[0])
        self.selected_module = self.modules[index]
        self.show_module_detail(self.selected_module)

    def show_module_detail(self, module: Dict[str, Any]) -> None:
        lines = [
            f"名称：{module.get('name', '')}",
            f"ID：{module.get('id', '')}",
            f"类型：{module.get('type', '')}",
            f"分类：{module.get('category', '')}",
            f"状态：{module.get('status', '')}",
            f"启用：{'是' if module.get('enabled') else '否'}",
            f"仓库：{module.get('repo', '')}",
            f"入口：{module.get('entry', '')}",
            f"配置：{module.get('config', '')}",
            "",
            "说明：",
            module.get("description", ""),
        ]
        self.set_detail("\n".join(lines))

    def clear_detail(self) -> None:
        self.set_detail("请选择左侧模块。")

    def set_detail(self, content: str) -> None:
        self.detail_text.configure(state="normal")
        self.detail_text.delete("1.0", tk.END)
        self.detail_text.insert(tk.END, content)
        self.detail_text.configure(state="disabled")

    def launch_selected_module(self) -> None:
        module = self.selected_module
        if not module:
            messagebox.showinfo("未选择模块", "请先选择一个模块。")
            return

        if not module.get("enabled"):
            messagebox.showwarning("模块未启用", "该模块当前未启用。")
            return

        entry = module.get("entry")
        if not entry:
            messagebox.showwarning("缺少入口", "该模块没有设置 entry。")
            return

        entry_path = ROOT_DIR / entry
        if not entry_path.exists():
            messagebox.showwarning(
                "入口不存在",
                f"模块入口文件暂未创建：\n{entry_path}\n\n这说明模块已注册，但还未接入真实启动脚本。",
            )
            return

        try:
            if sys.platform.startswith("win"):
                os.startfile(entry_path)  # type: ignore[attr-defined]
            else:
                subprocess.Popen([str(entry_path)], cwd=str(ROOT_DIR))
            self.status_var.set(f"已启动：{module.get('name', '')}")
        except Exception as exc:
            messagebox.showerror("启动失败", str(exc))

    def open_selected_config(self) -> None:
        module = self.selected_module
        if not module:
            messagebox.showinfo("未选择模块", "请先选择一个模块。")
            return

        config = module.get("config")
        if not config:
            messagebox.showinfo("无配置文件", "该模块没有配置文件。")
            return

        self.open_path(ROOT_DIR / config)

    def open_path(self, path: Path) -> None:
        try:
            if not path.exists():
                messagebox.showwarning("路径不存在", f"路径不存在：\n{path}")
                return

            if sys.platform.startswith("win"):
                os.startfile(path)  # type: ignore[attr-defined]
            elif sys.platform == "darwin":
                subprocess.Popen(["open", str(path)])
            else:
                subprocess.Popen(["xdg-open", str(path)])
        except Exception as exc:
            messagebox.showerror("打开失败", str(exc))

    @staticmethod
    def read_json(path: Path) -> Dict[str, Any]:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)


if __name__ == "__main__":
    app = BSOSLauncher()
    app.mainloop()
