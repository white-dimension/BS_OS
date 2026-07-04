# BS_OS Module Spec

## 1. 模块注册字段

每个模块必须在 `modules.json` 中注册。

```json
{
  "id": "bs-cad-tools",
  "name": "BS CAD Tools",
  "type": "cad_plugin",
  "category": "CAD",
  "description": "AutoCAD efficiency commands and CAD standard tools.",
  "repo": "white-dimension/BS-CAD-Tools",
  "entry": "modules/cad/load_cad_tools.bat",
  "config": "config/cad_tools.json",
  "enabled": true,
  "status": "active_development"
}
```

## 2. 字段说明

| 字段 | 必填 | 说明 |
|---|---:|---|
| `id` | 是 | 模块唯一 ID，建议小写短横线 |
| `name` | 是 | 显示名称 |
| `type` | 是 | 模块类型 |
| `category` | 是 | 界面分类 |
| `description` | 否 | 模块说明 |
| `repo` | 否 | 对应 GitHub 仓库 |
| `entry` | 是 | 启动入口 |
| `config` | 否 | 模块配置文件 |
| `enabled` | 是 | 是否启用 |
| `status` | 是 | 当前状态 |

## 3. 模块类型

```text
background_app      后台常驻程序
cad_plugin          AutoCAD 插件
standard_pack       标准数据包
max_plugin          3ds Max 插件
floating_assistant  悬浮助手
project_tool        项目工具
external_link       外部链接或文件夹入口
```

## 4. 模块状态

```text
planned              计划中
active_development   正在开发
completed_baseline   已完成基础版
future_backlog       未来功能
paused               暂停
deprecated           废弃
```

## 5. 启动行为建议

### background_app

用于 IME Assistant。

点击后：

```text
检查是否已运行
↓
未运行则启动
↓
运行后进入后台或托盘
```

### cad_plugin

用于 BS-CAD-Tools。

点击后：

```text
检查 AutoCAD 是否打开
↓
如果打开，加载 LISP / DLL / 插件
↓
如果未打开，提示打开 AutoCAD
```

### standard_pack

用于 BS-CAD-Standard。

点击后：

```text
打开标准目录
或
同步标准配置到 CAD Tools
```

### project_tool

用于 Project Manager。

点击后：

```text
输入项目名
↓
选择项目根目录
↓
根据 project_template.json 创建文件夹
↓
写入 project.json
```
