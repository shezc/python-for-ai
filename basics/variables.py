"""
变量和数据类型示例
对比 Node.js 的变量声明
"""

def demo():
    """演示 Python 的变量和数据类型"""
    print("1. 变量声明（无需 var/let/const）")
    
    # Python 是动态类型语言，无需声明类型
    # Node.js: const name = "Python"
    name = "Python"
    age = 30
    is_learning = True
    height = 1.75
    
    print(f"   name: {name} (类型: {type(name).__name__})")
    print(f"   age: {age} (类型: {type(age).__name__})")
    print(f"   is_learning: {is_learning} (类型: {type(is_learning).__name__})")
    print(f"   height: {height} (类型: {type(height).__name__})")
    print()
    
    print("2. 列表（类似 JavaScript 数组）")
    # Node.js: const fruits = ["apple", "banana", "orange"]
    fruits = ["apple", "banana", "orange"]
    print(f"   fruits: {fruits}")
    print(f"   第一个元素: {fruits[0]}")
    print(f"   列表长度: {len(fruits)}")
    print()
    
    print("3. 字典（类似 JavaScript 对象）")
    # Node.js: const person = { name: "John", age: 30 }
    person = {
        "name": "John",
        "age": 30,
        "city": "Beijing"
    }
    print(f"   person: {person}")
    print(f"   访问属性: person['name'] = {person['name']}")
    print(f"   访问属性: person.get('age') = {person.get('age')}")
    print()
    
    print("4. 元组（不可变列表）")
    # Python 特有，类似不可变数组
    coordinates = (10, 20)
    print(f"   coordinates: {coordinates}")
    print(f"   x: {coordinates[0]}, y: {coordinates[1]}")
    print()
    
    print("5. 集合（类似 JavaScript Set）")
    # Node.js: const unique = new Set([1, 2, 3, 2])
    unique_numbers = {1, 2, 3, 2, 1}
    print(f"   unique_numbers: {unique_numbers}")
    print()
    
    print("6. 字符串格式化（类似模板字符串）")
    # Node.js: `Hello, ${name}!`
    message = f"Hello, {name}! You are {age} years old."
    print(f"   {message}")
    print()
    
    print("7. 类型转换")
    # Node.js: Number("123") 或 parseInt("123")
    number_str = "123"
    number_int = int(number_str)
    number_float = float(number_str)
    print(f"   字符串 '{number_str}' 转整数: {number_int}")
    print(f"   字符串 '{number_str}' 转浮点数: {number_float}")

