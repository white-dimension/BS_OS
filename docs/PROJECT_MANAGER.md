# BS_OS Project Manager

## Version

```text
v0.4-alpha
```

## Purpose

Project Manager creates a standard design project folder based on `config/project_template.json`.

It is intended for exhibition, commercial and interior design workflows.

## Files

```text
project_manager_ui.py
scripts/project_manager.py
modules/project-manager/start_ui.bat
modules/project-manager/create_project.bat
config/project_template.json
```

## How to Use

### From BS_OS Launcher

1. Run:

```bat
run_bs_os.bat
```

2. Select:

```text
BS Project Manager
```

3. Click:

```text
启动模块
```

4. Fill in:

```text
项目名称
客户名称
设计师
阶段
项目根目录
```

5. Click:

```text
创建标准项目
```

## Created Structure

The folder structure is read from:

```text
config/project_template.json
```

Current standard folders include:

```text
01_资料
02_CAD
03_模型
04_效果图
05_文本
06_输出
99_归档
```

## Project Metadata

Each created project includes:

```text
project.json
```

This file records:

- project name
- folder name
- client
- designer
- stage
- CAD standard version
- created time
- updated time

## Logs

Project creation logs are written to:

```text
logs/project_manager.log
```

## Current Status

```text
Status: usable alpha
Requires: local Windows / Python test
```

## Next Step

- Add template selection
- Add recent projects list
- Add open existing project
- Add automatic CAD standard copy
- Add one-click workflow: create project + open CAD + start IME
