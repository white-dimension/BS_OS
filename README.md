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

## 核心架构

```text
BS_OS/
├─ README.md
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
│  └─ MODULE_SPEC.md
├─ scripts/
├─ assets/
└─ examples/
```

## 第一阶段目标

v0.1 只做基础启动器，不做复杂功能。

### 必须完成

- [ ] 读取 `modules.json`
- [ ] 显示模块列表
- [ ] 支持启用 / 禁用模块
- [ ] 支持点击模块入口
- [ ] 支持统一配置路径
- [ ] 支持创建标准项目文件夹

### 暂不开发

- [ ] AI 自动判断工作状态
- [ ] 复杂插件市场
- [ ] 自动更新系统
- [ ] 多端同步
- [ ] 权限系统

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

## 推荐开发顺序

1. 建立 BS_OS 目录结构
2. 建立 `modules.json` 模块注册表
3. 建立基础启动器界面
4. 接入 BS-IME-Assistant
5. 接入 BS-CAD-Tools
6. 接入 BS-CAD-Standard
7. 接入 Project Manager
8. 后续接入 Max / Corona / Design Copilot

## 当前状态

```text
版本：v0.1-structure
状态：基础目录与说明文档阶段
目标：先把总入口架构固定下来，后续模块逐步接入
```
