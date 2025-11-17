# Jupyter Notebook 学习指南

## 📓 什么是 Jupyter Notebook？

Jupyter Notebook 是一个交互式的编程环境，类似于：
- **Node.js 对比：** 类似在浏览器中运行 Node.js REPL，但更强大
- **特点：** 可以混合代码、文本、图片、图表
- **优势：** 适合学习、实验、数据分析和可视化

## 🚀 快速开始

### 1. 安装 Jupyter

```bash
# 确保在虚拟环境中
pip install -r requirements.txt

# 或者单独安装
pip install jupyter ipykernel
```

### 2. 启动 Jupyter Notebook

```bash
# 启动 Jupyter Notebook 服务器
jupyter notebook

# 或者使用 JupyterLab（更现代的界面）
jupyter lab
```

启动后会自动在浏览器中打开 `http://localhost:8888`

### 3. 创建第一个 Notebook

1. 在 Jupyter 界面点击 **New** → **Python 3**
2. 在单元格中输入代码
3. 按 `Shift + Enter` 运行代码

## 📝 基本操作

### 单元格类型

- **Code（代码）**：编写和执行 Python 代码
- **Markdown（文本）**：编写文档、说明、标题

### 快捷键

| 操作 | 快捷键 | 说明 |
|------|--------|------|
| 运行单元格 | `Shift + Enter` | 运行当前单元格并跳到下一个 |
| 运行并插入 | `Alt + Enter` | 运行当前单元格并在下方插入新单元格 |
| 运行单元格 | `Ctrl + Enter` | 运行当前单元格但不移动 |
| 切换单元格类型 | `Y` | 切换到代码模式 |
| 切换单元格类型 | `M` | 切换到 Markdown 模式 |
| 删除单元格 | `D D` | 按两次 D 删除单元格 |
| 撤销删除 | `Z` | 撤销删除的单元格 |
| 保存 | `Ctrl + S` | 保存 notebook |

### 单元格模式

- **命令模式（蓝色边框）**：按 `Esc` 进入，可以操作单元格
- **编辑模式（绿色边框）**：按 `Enter` 进入，可以编辑代码

## 💡 使用技巧

### 1. 导入项目模块

在 notebook 中导入项目中的模块：

```python
# 添加项目根目录到路径
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))

# 现在可以导入项目模块了
from basics import variables, functions, classes
```

### 2. 显示多个输出

```python
# 在单元格末尾，最后一个表达式会自动显示
x = 10
y = 20
x + y  # 这会自动显示结果：30
```

### 3. 使用魔法命令（Magic Commands）

```python
# 查看执行时间
%time sum(range(1000000))

# 查看变量
%whos

# 运行外部 Python 文件
%run basics/variables.py

# 显示 matplotlib 图表（在 notebook 中）
%matplotlib inline
```

### 4. 调试代码

```python
# 使用 print 调试
print("调试信息")

# 使用 pdb 调试器
import pdb
pdb.set_trace()  # 设置断点
```

## 📚 示例 Notebook

项目包含以下示例 notebook：

1. **01_basics.ipynb** - 基础语法示例
2. **02_functions.ipynb** - 函数和类示例
3. **03_data_analysis.ipynb** - 数据分析示例

## 🔄 与普通 Python 脚本对比

| 特性 | Jupyter Notebook | Python 脚本 (.py) |
|------|------------------|-------------------|
| 交互式 | ✅ 是 | ❌ 否 |
| 可视化 | ✅ 方便 | ⚠️ 需要额外配置 |
| 文档 | ✅ 可以混合 Markdown | ⚠️ 只能注释 |
| 调试 | ✅ 逐单元格调试 | ⚠️ 需要调试器 |
| 适合场景 | 学习、实验、数据分析 | 生产环境、完整程序 |

## 🎯 学习路径

### 阶段 1: 基础操作
1. 创建第一个 notebook
2. 运行简单的 Python 代码
3. 学习单元格操作

### 阶段 2: 项目集成
1. 在 notebook 中导入项目模块
2. 运行项目中的示例代码
3. 修改和实验代码

### 阶段 3: 高级功能
1. 使用 Markdown 编写文档
2. 数据可视化（matplotlib, pandas）
3. 魔法命令的使用

## ⚠️ 注意事项

1. **保存文件**：Notebook 文件是 `.ipynb` 格式（JSON）
2. **版本控制**：`.ipynb` 文件可以提交到 Git，但建议清理输出
3. **性能**：Notebook 适合学习和实验，生产环境建议使用 `.py` 文件
4. **内核**：确保使用正确的 Python 环境（虚拟环境）

## 🛠️ 常见问题

### Q: 如何切换 Python 环境？
A: 在 Jupyter 中，需要安装 ipykernel：
```bash
# 在虚拟环境中
pip install ipykernel
python -m ipykernel install --user --name=python-for-ai
```

### Q: 如何停止运行中的代码？
A: 在工具栏点击 **Interrupt** 按钮，或按 `Ctrl + C`

### Q: 如何重启内核？
A: 点击 **Kernel** → **Restart**，或按 `0 0`（命令模式下）

### Q: Notebook 文件在哪里？
A: 默认在当前目录，可以在 Jupyter 界面中看到文件列表

## 📖 下一步

1. 运行 `jupyter notebook` 启动服务
2. 打开项目中的示例 notebook
3. 尝试修改和运行代码
4. 创建自己的学习 notebook

祝你学习愉快！📓✨

