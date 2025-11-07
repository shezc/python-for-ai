"""
f-string 详解
对比 Node.js 的模板字符串（Template Literals）
"""

def demo():
    """详细解释 f-string 的用法"""
    print("=" * 60)
    print("Python f-string 详解")
    print("=" * 60)
    print()
    
    print("1. 什么是 f-string？")
    print("   f-string 是 Python 3.6+ 引入的字符串格式化语法")
    print("   在字符串前加 'f' 或 'F' 前缀，可以在字符串中直接嵌入变量")
    print()
    
    print("2. 基本用法")
    print("-" * 60)
    
    # 基本变量插入
    name = "Python"
    age = 30
    
    # Python f-string（类似 Node.js 的模板字符串）
    # Node.js: `Hello, ${name}!`
    message = f"Hello, {name}!"
    print(f"   f-string: {message}")
    
    # Node.js 对比
    print("   Node.js 等价写法: `Hello, ${name}!`")
    print()
    
    print("3. 多种用法示例")
    print("-" * 60)
    
    # 变量插入
    name = "Alice"
    age = 25
    print(f"   变量插入: 我叫 {name}，今年 {age} 岁")
    
    # 表达式计算
    x = 10
    y = 20
    print(f"   表达式: {x} + {y} = {x + y}")
    
    # 调用函数
    def get_greeting(name):
        return f"你好, {name}!"
    
    print(f"   函数调用: {get_greeting('Python')}")
    
    # 方法调用
    text = "hello world"
    print(f"   方法调用: {text.upper()}")
    print()
    
    print("4. 格式化数字")
    print("-" * 60)
    
    price = 99.99
    print(f"   原价: {price}")
    print(f"   保留2位小数: {price:.2f}")
    print(f"   百分比: {0.25:.2%}")
    print(f"   整数: {int(price)}")
    print()
    
    print("5. 对齐和填充")
    print("-" * 60)
    
    name = "Python"
    print(f"   左对齐（10字符）: |{name:<10}|")
    print(f"   右对齐（10字符）: |{name:>10}|")
    print(f"   居中（10字符）: |{name:^10}|")
    print(f"   填充字符: |{name:*^10}|")
    print()
    
    print("6. 日期时间格式化")
    print("-" * 60)
    
    from datetime import datetime
    now = datetime.now()
    print(f"   当前时间: {now}")
    print(f"   格式化: {now:%Y-%m-%d %H:%M:%S}")
    print()
    
    print("7. 多行 f-string")
    print("-" * 60)
    
    name = "Python"
    version = "3.11"
    message = (
        f"项目名称: {name}\n"
        f"版本号: {version}\n"
        f"状态: 学习中"
    )
    print(f"   多行字符串:\n{message}")
    print()
    
    print("8. 嵌套 f-string")
    print("-" * 60)
    
    name = "Python"
    greeting = f"Hello, {name}!"
    full_message = f"消息: {greeting}"
    print(f"   嵌套: {full_message}")
    print()
    
    print("9. 与 Node.js 模板字符串对比")
    print("-" * 60)
    print("   Python f-string:        f'Hello, {name}!'")
    print("   Node.js 模板字符串:     `Hello, ${name}!`")
    print()
    print("   相同点:")
    print("     - 都可以直接嵌入变量和表达式")
    print("     - 都支持多行字符串")
    print("     - 语法简洁易读")
    print()
    print("   不同点:")
    print("     - Python 用 {} 包裹变量，Node.js 用 ${}")
    print("     - Python 用 f 前缀，Node.js 用反引号 `")
    print("     - Python 支持格式化选项（如 :.2f），Node.js 需要额外处理")
    print()
    
    print("10. 其他字符串格式化方法（对比）")
    print("-" * 60)
    
    name = "Python"
    age = 30
    
    # 方法1: f-string（推荐，Python 3.6+）
    msg1 = f"我是 {name}，{age} 岁"
    print(f"   f-string: {msg1}")
    
    # 方法2: .format() 方法
    msg2 = "我是 {}，{} 岁".format(name, age)
    print(f"   .format(): {msg2}")
    
    # 方法3: % 格式化（旧式，类似 C 语言）
    msg3 = "我是 %s，%d 岁" % (name, age)
    print(f"   % 格式化: {msg3}")
    
    print()
    print("   💡 推荐使用 f-string，最简洁易读！")
    print()
    
    print("=" * 60)
    print("总结：f-string 是 Python 的模板字符串，类似 Node.js 的反引号语法")
    print("=" * 60)

if __name__ == "__main__":
    demo()

