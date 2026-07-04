# BS_OS Architecture

## 1. 核心思想

BS_OS 采用“稳定外壳 + 可变模块”的结构。

```text
BS_OS Core
│
├─ Module Registry
├─ Config Center
├─ Project Center
├─ Launcher UI
└─ External Tool Bridge
```

## 2. BS_OS 不负责什么

BS_OS 不直接承担 CAD 绘图、Max 建模、Corona 渲染、输入法切换等具体工作。

这些工作由独立模块完成。

## 3. BS_OS 负责什么

BS_OS 负责：

- 读取模块注册表
- 显示模块入口
- 启动后台程序
- 加载外部插件
- 管理统一配置
- 创建标准项目目录
- 记录模块状态

## 4. 模块接入流程

```text
新增工具
↓
放入 modules/ 对应分类目录
↓
在 modules.json 注册
↓
BS_OS 读取配置
↓
界面自动显示入口
↓
点击后执行 entry
```

## 5. 推荐目录分层

```text
config/     全局配置
modules/    模块入口与适配脚本
docs/       架构与规范
scripts/    通用脚本
assets/     图标、图片、界面资源
examples/   示例配置与项目样例
```

## 6. 阶段路线

### v0.1 Structure

- 建立目录
- 建立 README
- 建立模块注册表
- 建立配置模板

### v0.2 Launcher

- 做基础界面
- 读取 modules.json
- 显示模块卡片
- 点击启动模块

### v0.3 CAD Bridge

- 接入 BS-CAD-Tools
- 接入 BS-CAD-Standard
- 支持 AutoCAD 检测与插件加载

### v0.4 Project Manager

- 一键创建项目
- 写入 project.json
- 打开项目目录

### v0.5 Assistant Layer

- 接入 Design Copilot
- 接入 Max / Corona 参数助手
