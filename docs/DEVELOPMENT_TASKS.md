# BS_OS Development Tasks

## Current Version

```text
v0.3-cad-bridge-loader-entry
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

## Next: v0.4 Project Manager

### Goal

Create standard project folders from BS_OS.

### Tasks

- [ ] Build project creation window
- [ ] Input project name / client / designer / stage
- [ ] Read `config/project_template.json`
- [ ] Create folders
- [ ] Write `project.json`
- [ ] Open project root folder after creation

## Later

- [ ] Package as `.exe`
- [ ] Add icons
- [ ] Add dark theme
- [ ] Add module enable / disable editing UI
- [ ] Add logs panel
- [ ] Add auto-update concept
