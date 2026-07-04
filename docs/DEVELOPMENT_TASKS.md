# BS_OS Development Tasks

## Current Version

```text
v0.4-project-manager-alpha
```

## Completed

### v0.1 Structure

- [x] Create repository structure
- [x] Add README
- [x] Add modules.json registry
- [x] Add config templates
- [x] Add architecture documentation
- [x] Add module specification

### v0.2 Launcher Basic

- [x] Add Python Tkinter launcher
- [x] Read modules.json
- [x] Display module list
- [x] Show module details
- [x] Launch enabled module entry scripts
- [x] Open module config path
- [x] Add Windows run script
- [x] Add placeholder module startup scripts

### v0.3 CAD Bridge Basic

- [x] Add `config/cad_bridge.json`
- [x] Add `scripts/cad_bridge.py`
- [x] Add `modules/cad/check_cad_bridge.bat`
- [x] Register `BS CAD Bridge Check` in `modules.json`
- [x] Check BS-CAD-Tools local path
- [x] Check BS-CAD-Standard local path
- [x] Check expected CAD tools loader path
- [x] Write CAD Bridge log file
- [x] Add `docs/CAD_BRIDGE.md`

### v0.3 CAD Bridge Loader Entry

- [x] Add `BS_CAD_TOOLS_LOAD.lsp` to `white-dimension/BS-CAD-Tools`
- [x] Add `BS_TOOLS_STATUS` command placeholder
- [x] Add `BS_RELOAD_TOOLS` command placeholder
- [x] Add safe-load function template
- [x] Add `docs/BS_OS_BRIDGE.md` to BS-CAD-Tools

### v0.4 Project Manager Alpha

- [x] Add `scripts/project_manager.py`
- [x] Add command-line project creation
- [x] Read `config/project_template.json`
- [x] Create standard folder structure
- [x] Write `project.json`
- [x] Write `logs/project_manager.log`
- [x] Add `project_manager_ui.py`
- [x] Add `modules/project-manager/start_ui.bat`
- [x] Add `modules/project-manager/create_project.bat`
- [x] Point Project Manager module to UI entry in `modules.json`
- [x] Add `docs/PROJECT_MANAGER.md`

## Tomorrow Verification Checklist

- [ ] Pull latest `BS_OS`
- [ ] Run `run_bs_os.bat`
- [ ] Confirm launcher opens
- [ ] Confirm `BS Project Manager` appears
- [ ] Launch `BS Project Manager`
- [ ] Create a test project
- [ ] Confirm folders are created
- [ ] Confirm `project.json` is created
- [ ] Confirm project folder opens automatically
- [ ] Confirm `logs/project_manager.log` is written
- [ ] Run `BS CAD Bridge Check`
- [ ] Confirm CAD Bridge path report

## Next: v0.4 Project Manager Beta

### Goal

Improve Project Manager after first local test.

### Tasks

- [ ] Add recent projects list
- [ ] Add open existing project
- [ ] Add template selection
- [ ] Add project stage presets for interior / exhibition workflow
- [ ] Add one-click workflow: create project + open CAD + start IME
- [ ] Add validation for duplicate project names
- [ ] Add settings UI for default projects root

## Next: v0.3 CAD Bridge Real Loading

### Goal

Connect BS_OS to real AutoCAD command files.

### Tasks

- [ ] Map actual BS-CAD-Tools command file paths
- [ ] Connect actual command files inside `BS_CAD_TOOLS_LOAD.lsp`
- [ ] Generate AutoCAD script file from BS_OS
- [ ] Add manual AutoCAD load instructions in BS_OS
- [ ] Add AutoCAD executable path config UI
- [ ] Detect whether AutoCAD is running
- [ ] Add BS-CAD-Standard sync logic
- [ ] Add CAD Tools status display in launcher
- [ ] Add error messages for missing paths

## Later

- [ ] Package as `.exe`
- [ ] Add icons
- [ ] Add dark theme
- [ ] Add module enable / disable editing UI
- [ ] Add logs panel
- [ ] Add auto-update concept
