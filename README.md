# Python 学习项目

欢迎！这是一个专为 Node.js 开发者设计的 Python 学习项目。

## 📚 项目结构

```
python-for-ai/
├── README.md              # 项目说明
├── requirements.txt       # Python 依赖管理（类似 package.json）
├── .gitignore            # Git 忽略文件
├── main.py               # 主程序入口
├── basics/               # 基础语法示例
│   ├── __init__.py
│   ├── variables.py     # 变量和数据类型
│   ├── functions.py     # 函数
│   └── classes.py        # 类和对象
├── advanced/              # 进阶内容
│   ├── __init__.py
│   ├── file_io.py        # 文件操作
│   ├── json_handling.py  # JSON 处理
│   └── async_example.py  # 异步编程（类似 async/await）
└── utils/                 # 工具函数
    ├── __init__.py
    └── helpers.py
```

## 🚀 快速开始

### 1. 安装 Python

确保已安装 Python 3.8+：
```bash
python --version
# 或
python3 --version
```

### 2. 创建虚拟环境（推荐）

```bash
# 创建虚拟环境（类似 npm）
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 运行示例

```bash
python main.py
```

## 📖 学习路径

### 阶段 1: 基础语法
- [x] 变量和数据类型
- [x] 函数定义
- [x] 类和对象

### 阶段 2: 常用操作
- [x] 文件读写
- [x] JSON 处理
- [x] 列表推导式

### 阶段 3: 进阶特性
- [ ] 异步编程
- [ ] 装饰器
- [ ] 生成器

## 🔄 Node.js vs Python 快速对比

| 特性 | Node.js | Python |
|------|---------|--------|
| 包管理 | npm | pip |
| 包文件 | package.json | requirements.txt |
| 模块导入 | `require()` / `import` | `import` |
| 异步 | `async/await` | `async/await` |
| 函数定义 | `function` / `=>` | `def` |
| 类定义 | `class` | `class` |
| 注释 | `//` 或 `/* */` | `#` 或 `""" """` |

## 💡 学习建议

1. **从基础开始**：先运行 `basics/` 目录下的示例
2. **对比学习**：利用你的 Node.js 经验，对比两种语言的差异
3. **实践为主**：修改示例代码，尝试不同的写法
4. **查阅文档**：遇到问题查看 [Python 官方文档](https://docs.python.org/zh-cn/3/)

## 📝 笔记

在学习过程中，可以在这个 README 中添加你的学习笔记和心得。

## 🤝 贡献

欢迎提交问题和改进建议！

