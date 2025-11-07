"""
函数定义示例
对比 Node.js 的函数声明
"""

def demo():
    """演示 Python 的函数定义"""
    print("1. 基本函数定义")
    
    # Node.js: function greet(name) { return `Hello, ${name}!`; }
    # Python 的 f"..." 类似 Node.js 的 `...${}...` 模板字符串
    # f 是 "formatted string" 的缩写，可以在字符串中直接嵌入变量
    def greet(name):
        """简单的问候函数"""
        return f"Hello, {name}!"  # f-string: 类似 Node.js 的 `Hello, ${name}!`
    
    print(f"   {greet('Python')}")  # f-string 中也可以调用函数
    print()
    
    print("2. 默认参数")
    # Node.js: function greet(name = "World") { ... }
    def greet_with_default(name="World"):
        return f"Hello, {name}!"
    
    print(f"   {greet_with_default()}")
    print(f"   {greet_with_default('Python')}")
    print()
    
    print("3. 可变参数（类似 arguments）")
    # Node.js: function sum(...args) { return args.reduce((a, b) => a + b, 0); }
    def sum_numbers(*args):
        """计算多个数字的和"""
        return sum(args)
    
    print(f"   sum_numbers(1, 2, 3, 4) = {sum_numbers(1, 2, 3, 4)}")
    print()
    
    print("4. 关键字参数（类似对象参数）")
    # Node.js: function createUser({ name, age, email }) { ... }
    def create_user(name, age, email=None):
        """创建用户信息"""
        user = {"name": name, "age": age}
        if email:
            user["email"] = email
        return user
    
    user1 = create_user("Alice", 25)
    user2 = create_user("Bob", 30, "bob@example.com")
    print(f"   user1: {user1}")
    print(f"   user2: {user2}")
    print()
    
    print("5. Lambda 函数（类似箭头函数）")
    # Node.js: const square = x => x * x
    square = lambda x: x * x
    print(f"   square(5) = {square(5)}")
    
    # 使用 map（类似数组的 map）
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x * x, numbers))
    print(f"   map([1,2,3,4,5], square) = {squared}")
    print()
    
    print("6. 列表推导式（类似 map/filter 的组合）")
    # Node.js: [1,2,3,4,5].map(x => x * x).filter(x => x > 10)
    squared_filtered = [x * x for x in numbers if x * x > 10]
    print(f"   [x*x for x in [1,2,3,4,5] if x*x > 10] = {squared_filtered}")
    print()
    
    print("7. 文档字符串（类似 JSDoc）")
    def calculate_area(length, width):
        """
        计算矩形面积
        
        Args:
            length: 长度
            width: 宽度
        
        Returns:
            面积值
        """
        return length * width
    
    print(f"   calculate_area(5, 3) = {calculate_area(5, 3)}")
    # __doc__ 是 Python 的特殊属性，用于访问函数的文档字符串
    # 类似 Node.js 中通过注释编写的 JSDoc，但 Python 的文档字符串是实际的对象属性
    print(f"   函数文档: {calculate_area.__doc__}")

