# BS_OS CAD Bridge

## Version

```text
v0.3-basic
```

## Purpose

CAD Bridge is the connection layer between BS_OS and the AutoCAD toolchain.

It connects:

```text
BS_OS
↓
BS CAD Bridge
↓
BS-CAD-Tools
↓
AutoCAD
```

And also references:

```text
BS-CAD-Standard
```

## Current Implementation

Current v0.3-basic does not directly control AutoCAD yet.

It provides:

- `config/cad_bridge.json`
- `scripts/cad_bridge.py`
- `modules/cad/check_cad_bridge.bat`
- `BS CAD Bridge Check` module registration in `modules.json`

## Current Check Items

The script checks:

- Whether local BS-CAD-Tools path exists
- Whether `BS_CAD_TOOLS_LOAD.lsp` exists
- Whether local BS-CAD-Standard path exists
- Writes status to `logs/cad_bridge.log`

## Expected Local Folder Layout

Recommended local structure:

```text
BS_Workspace/
├─ BS_OS/
├─ BS-CAD-Tools/
└─ BS-CAD-Standard/
```

Default config assumes:

```text
BS_OS/../BS-CAD-Tools
BS_OS/../BS-CAD-Standard
```

## Required Future Loader in BS-CAD-Tools

CAD Bridge expects this file in BS-CAD-Tools:

```text
BS_CAD_TOOLS_LOAD.lsp
```

This file should later load the real CAD commands, such as:

```text
BS_LAYER
BS_CHECK
BS_FIX_LAYER
BS_FIX_MISSING
BS_TEMPLATE_CHECK
```

## Next Step

v0.3-next should add:

- Real `BS_CAD_TOOLS_LOAD.lsp` in BS-CAD-Tools
- AutoCAD script generation
- Better AutoCAD path configuration
- Manual load instructions for first test

## Manual Test Later

When using a Windows workstation:

1. Clone these repositories side by side:

```text
BS_OS
BS-CAD-Tools
BS-CAD-Standard
```

2. Run:

```bat
run_bs_os.bat
```

3. Click:

```text
BS CAD Bridge Check
```

4. Confirm the status report.
