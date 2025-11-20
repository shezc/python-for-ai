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
│   ├── async_example.py  # 异步编程（类似 async/await）
│   └── sentiment_analysis.py  # Transformers 情感分析示例
└── utils/                 # 工具函数
    ├── __init__.py
    └── helpers.py
├── notebooks/             # Jupyter Notebook 示例
    ├── 01_basics.ipynb    # 基础语法示例
    ├── 02_functions.ipynb  # 函数和类示例
    └── 03_data_analysis.ipynb  # 数据分析示例
├── JUPYTER_GUIDE.md      # Jupyter Notebook 使用指南
├── setup_mirror.bat     # Windows CMD 镜像配置脚本
├── setup_mirror.ps1     # Windows PowerShell 镜像配置脚本
└── setup_mirror.sh      # Linux/macOS 镜像配置脚本
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

**使用国内镜像加速安装**（可选）:
```bash
# 使用清华大学镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 4. 运行示例

**方式 1: 运行 Python 脚本**
```bash
python main.py
```

**方式 2: 使用 Jupyter Notebook（推荐学习）**
```bash
# 启动 Jupyter Notebook
jupyter notebook

# 或使用 JupyterLab（更现代）
jupyter lab
```

然后在浏览器中打开 `notebooks/` 目录下的示例 notebook。

**方式 3: 运行情感分析示例**
```bash
# 直接运行情感分析示例
python advanced/sentiment_analysis.py

# 或作为模块运行
python -m advanced.sentiment_analysis
```

**注意**: 首次运行情感分析示例需要下载预训练模型，可能需要一些时间。请确保网络连接正常。

**使用国内镜像加速下载**（推荐）:

**快速配置**（一键设置）:
```powershell
# Windows PowerShell（推荐）
.\setup_mirror.ps1

# Windows CMD
setup_mirror.bat

# macOS/Linux
chmod +x setup_mirror.sh
./setup_mirror.sh
```

**手动配置**:
```bash
# Windows
set HF_ENDPOINT=https://hf-mirror.com

# macOS/Linux
export HF_ENDPOINT=https://hf-mirror.com
```

**详细配置说明**:

**方法 1: 使用配置脚本（推荐）**
```powershell
# Windows PowerShell
.\setup_mirror.ps1

# Windows CMD
setup_mirror.bat

# Linux/macOS
chmod +x setup_mirror.sh
./setup_mirror.sh
```

**方法 2: 手动设置环境变量**
```powershell
# Windows PowerShell（临时）
$env:HF_ENDPOINT="https://hf-mirror.com"

# Windows PowerShell（永久）
[System.Environment]::SetEnvironmentVariable("HF_ENDPOINT", "https://hf-mirror.com", "User")

# Windows CMD
setx HF_ENDPOINT "https://hf-mirror.com"

# Linux/macOS
export HF_ENDPOINT=https://hf-mirror.com
echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc
```

**方法 3: 在代码中设置**
编辑 `advanced/sentiment_analysis.py`，取消第 16 行的注释：
```python
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
```

**注意**: 环境变量设置后需要重新打开终端才能生效。

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
- [x] 异步编程
- [x] Transformers 情感分析
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
2. **使用 Jupyter Notebook**：推荐使用 notebook 进行交互式学习（见 `JUPYTER_GUIDE.md`）
3. **对比学习**：利用你的 Node.js 经验，对比两种语言的差异
4. **实践为主**：修改示例代码，尝试不同的写法
5. **查阅文档**：遇到问题查看 [Python 官方文档](https://docs.python.org/zh-cn/3/)

## 📓 Jupyter Notebook

项目包含 Jupyter Notebook 示例，适合交互式学习：

- **01_basics.ipynb** - 基础语法示例
- **02_functions.ipynb** - 函数和类示例  
- **03_data_analysis.ipynb** - 数据分析示例

详细使用指南请查看 [JUPYTER_GUIDE.md](JUPYTER_GUIDE.md)


