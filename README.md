# BS_OS

BS_OS 是 BS Toolkit 的总入口系统，用于统一管理、启动和连接 CAD、3ds Max、输入法助手、设计助手等独立模块。

## 定位

BS_OS 不直接替代各个专业软件，也不把所有功能写进一个程序里。

它的定位是：

```text
BS_OS = 启动器 / 控制台 / 模块管理器 / 项目入口
```

其他工具作为独立模块接入：

```text
BS-IME-Assistant  -> 后台常驻输入法助手
BS-CAD-Tools      -> 加载到 AutoCAD 的 CAD 工具集
BS-CAD-Standard   -> CAD 标准数据与检查规则
Max Assistant     -> 3ds Max 辅助工具
Design Copilot    -> 悬浮设计助手
Project Manager   -> 项目创建与归档工具
```

## 当前版本

```text
v0.2-launcher-basic
```

当前已经实现最小可运行启动器：

- 读取 `modules.json`
- 显示模块列表
- 显示模块详情
- 点击启动已启用模块
- 打开模块配置文件
- 打开项目模板配置
- 打开仓库目录

## 如何运行

Windows 环境：

```bat
run_bs_os.bat
```

或直接运行：

```bash
python bs_os_launcher.py
```

要求：

```text
Python 3.x
Tkinter
```

Tkinter 通常随 Python 自带安装。

## 核心架构

```text
BS_OS/
├─ README.md
├─ bs_os_launcher.py
├─ run_bs_os.bat
├─ modules.json
├─ config/
│  ├─ app.json
│  ├─ paths.json
│  └─ project_template.json
├─ modules/
│  ├─ cad/
│  ├─ ime/
│  ├─ max/
│  ├─ design-copilot/
│  └─ project-manager/
├─ docs/
│  ├─ ARCHITECTURE.md
│  ├─ MODULE_SPEC.md
│  └─ DEVELOPMENT_TASKS.md
├─ scripts/
├─ assets/
└─ examples/
```

## 模块连接逻辑

每个模块通过 `modules.json` 注册。

示例：

```json
{
  "id": "bs-ime-assistant",
  "name": "BS IME Assistant",
  "type": "background_app",
  "category": "Input",
  "entry": "modules/ime/start.bat",
  "enabled": true
}
```

BS_OS 启动后读取模块配置，然后在界面中生成入口。

## 模块类型

| type | 说明 |
|---|---|
| `background_app` | 后台常驻程序，例如 IME Assistant |
| `cad_plugin` | AutoCAD 插件，例如 BS-CAD-Tools |
| `standard_pack` | 标准数据包，例如 BS-CAD-Standard |
| `max_plugin` | 3ds Max 工具 |
| `floating_assistant` | 悬浮窗助手 |
| `project_tool` | 项目管理工具 |

## 当前模块状态

| 模块 | 状态 |
|---|---|
| BS IME Assistant | 已注册，已有启动占位 |
| BS CAD Tools | 已注册，已有加载占位 |
| BS CAD Standard | 已注册，已有标准入口占位 |
| BS Project Manager | 已注册，已有启动占位 |
| BS Design Copilot | 已注册，暂未启用 |
| BS Max Assistant | 已注册，暂未启用 |

## 下一步

```text
v0.3 CAD Bridge
```

目标：让 BS_OS 真正检测 AutoCAD，并加载 BS-CAD-Tools。 

重点任务：

- 检测 AutoCAD 是否运行
- 配置 AutoCAD 路径
- 配置 BS-CAD-Tools 本地路径
- 接入真实 LISP / 插件加载逻辑
- 同步 BS-CAD-Standard 标准配置
