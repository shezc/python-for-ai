# 快速开始指南

## 🚀 第一步：检查 Python 环境

```bash
# 检查 Python 版本（需要 3.8+）
python --version
# 或
python3 --version
```

## 📦 第二步：创建虚拟环境（推荐）

虚拟环境类似于 Node.js 的 `node_modules`，用于隔离项目依赖。

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows PowerShell:
venv\Scripts\Activate.ps1

# Windows CMD:
venv\Scripts\activate.bat

# macOS/Linux:
source venv/bin/activate
```

激活后，命令行提示符前会显示 `(venv)`。

## 📥 第三步：安装依赖

```bash
# 安装项目依赖（类似 npm install）
pip install -r requirements.txt
```

## ▶️ 第四步：运行示例

```bash
# 运行主程序
python main.py
```

## 📚 学习路径

### 1. 基础语法（推荐先学）

```bash
# 单独运行基础示例
python -c "from basics import variables; variables.demo()"
python -c "from basics import functions; functions.demo()"
python -c "from basics import classes; classes.demo()"
```

### 2. 进阶内容

```bash
# 文件操作
python -c "from advanced import file_io; file_io.demo()"

# JSON 处理
python -c "from advanced import json_handling; json_handling.demo()"

# 异步编程
python -m advanced.async_example
```

### 3. 工具函数

```bash
python -c "from utils import helpers; helpers.demo()"
```

## 🔍 常用命令对比

| 操作 | Node.js | Python |
|------|---------|--------|
| 包管理 | `npm install` | `pip install` |
| 运行脚本 | `node app.js` | `python app.py` |
| 查看版本 | `node --version` | `python --version` |
| 包列表 | `npm list` | `pip list` |
| 卸载包 | `npm uninstall` | `pip uninstall` |

## 💡 学习建议

1. **从基础开始**：先运行 `basics/` 目录下的示例
2. **对比学习**：利用你的 Node.js 经验，对比两种语言的差异
3. **动手实践**：修改示例代码，尝试不同的写法
4. **查阅文档**：遇到问题查看 [Python 官方文档](https://docs.python.org/zh-cn/3/)

## 🐛 常见问题

### Q: 找不到 python 命令？
A: 可能需要使用 `python3` 命令，或者检查 PATH 环境变量。

### Q: pip 命令不存在？
A: 确保 Python 安装时包含了 pip，或者使用 `python -m pip`。

### Q: 模块导入错误？
A: 确保在项目根目录运行命令，或者使用 `python -m` 方式运行。

## 📝 下一步

- 阅读 `README.md` 了解项目结构
- 查看各个示例文件中的注释
- 尝试修改代码并观察结果
- 创建自己的 Python 脚本

祝你学习愉快！🐍

