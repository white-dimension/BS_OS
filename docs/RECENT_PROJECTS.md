# BS_OS Recent Projects

## Version

```text
v0.4-beta
```

## Purpose

Recent Projects records projects created by BS Project Manager and provides a quick way to reopen them.

## Files

```text
data/recent_projects.json
recent_projects_ui.py
modules/project-manager/recent_projects.bat
scripts/project_manager.py
```

## How It Works

When a project is created through Project Manager:

```text
Create project
↓
Create standard folders
↓
Write project.json
↓
Record project into data/recent_projects.json
```

## From BS_OS Launcher

1. Run:

```bat
run_bs_os.bat
```

2. Select:

```text
BS Recent Projects
```

3. Click:

```text
启动模块
```

4. Select a project and open:

```text
打开项目目录
```

or double-click the project row.

## Data Format

```json
{
  "schema_version": "0.1",
  "projects": [
    {
      "project_name": "示例项目",
      "client": "示例客户",
      "designer": "BS Design",
      "stage": "concept",
      "path": "D:/BS_Projects/示例项目",
      "project_file": "D:/BS_Projects/示例项目/project.json",
      "last_opened_at": "2026-07-04 20:00:00",
      "created_at": "2026-07-04 20:00:00"
    }
  ]
}
```

## Current Status

```text
Status: usable beta
Requires: local Windows / Python test
```

## Next Step

- Update `last_opened_at` when reopening a project
- Add remove-from-recent action
- Add pin project action
- Add project search
- Integrate recent projects directly into BS_OS home dashboard
