"""
主程序入口
Python 使用 # 或三引号进行注释
类似 Node.js 的 // 或 /* */
"""

# 导入自定义模块
from basics import variables, functions, classes
from advanced import file_io, json_handling, async_example, sentiment_analysis
from utils import helpers

def main():
    """主函数"""
    print("=" * 50)
    print("欢迎来到 Python 学习项目！")
    print("=" * 50)
    print()
    
    # 运行基础示例
    print("📚 基础语法示例")
    print("-" * 50)
    variables.demo()
    print()
    
    functions.demo()
    print()
    
    classes.demo()
    print()
    
    # 运行进阶示例
    print("🚀 进阶示例")
    print("-" * 50)
    file_io.demo()
    print()
    
    json_handling.demo()
    print()
    
    # 工具函数示例
    print("🛠️ 工具函数示例")
    print("-" * 50)
    helpers.demo()
    print()
    
    # 异步编程示例（可选，需要单独运行）
    print("⚡ 异步编程示例（可选）")
    print("-" * 50)
    print("   提示: 运行 'python -m advanced.async_example' 查看异步示例")
    print()
    
    # 情感分析示例（可选，需要安装 transformers）
    print("🤖 情感分析示例（可选）")
    print("-" * 50)
    print("   提示: 运行 'python -m advanced.sentiment_analysis' 查看情感分析示例")
    print("   或直接运行: python advanced/sentiment_analysis.py")
    print()
    
    print("=" * 50)
    print("学习愉快！继续探索 Python 的世界吧 🐍")
    print("=" * 50)

if __name__ == "__main__":
    # 类似 Node.js 的 if (require.main === module)
    main()

