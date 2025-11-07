"""
工具函数示例
展示一些常用的 Python 工具函数
"""

import os
from datetime import datetime

def demo():
    """演示常用的工具函数"""
    print("1. 字符串操作")
    
    text = "  Hello Python World  "
    print(f"   原始: '{text}'")
    print(f"   去除空格: '{text.strip()}'")  # 类似 trim()
    print(f"   转大写: '{text.upper()}'")
    print(f"   转小写: '{text.lower()}'")
    print(f"   替换: '{text.replace('Python', 'Node.js')}'")
    print()
    
    print("2. 列表操作")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"   原始列表: {numbers}")
    print(f"   排序: {sorted(numbers)}")
    print(f"   去重: {list(set(numbers))}")
    print(f"   最大值: {max(numbers)}")
    print(f"   最小值: {min(numbers)}")
    print(f"   求和: {sum(numbers)}")
    print()
    
    print("3. 字典操作")
    user = {"name": "Alice", "age": 25, "city": "Beijing"}
    print(f"   原始字典: {user}")
    print(f"   所有键: {list(user.keys())}")
    print(f"   所有值: {list(user.values())}")
    print(f"   键值对: {list(user.items())}")
    print()
    
    print("4. 日期时间（类似 JavaScript Date）")
    now = datetime.now()
    print(f"   当前时间: {now}")
    print(f"   格式化: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   年份: {now.year}, 月份: {now.month}, 日期: {now.day}")
    print()
    
    print("5. 环境变量（类似 process.env）")
    # Node.js: process.env.NODE_ENV
    # Python: os.getenv('NODE_ENV')
    node_env = os.getenv("NODE_ENV", "development")
    print(f"   NODE_ENV: {node_env}")
    print()
    
    print("6. 路径操作（类似 path 模块）")
    current_dir = os.getcwd()
    print(f"   当前目录: {current_dir}")
    print(f"   路径拼接: {os.path.join('folder', 'file.txt')}")
    print()
    
    print("7. 条件表达式（类似三元运算符）")
    # Node.js: const result = x > 0 ? 'positive' : 'negative'
    x = 5
    result = "positive" if x > 0 else "negative"
    print(f"   x = {x}, result = '{result}'")
    print()
    
    print("8. 枚举（类似 Object.keys/values）")
    fruits = ["apple", "banana", "orange"]
    print("   使用 enumerate:")
    for index, fruit in enumerate(fruits, start=1):
        print(f"     {index}. {fruit}")
    print()
    
    print("9. zip 函数（合并多个列表）")
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["Beijing", "Shanghai", "Guangzhou"]
    
    print("   合并列表:")
    for name, age, city in zip(names, ages, cities):
        print(f"     {name}, {age}岁, 来自{city}")

