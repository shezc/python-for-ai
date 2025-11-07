"""
文档字符串（Docstring）详解
对比 Node.js 的 JSDoc 注释
"""

def demo():
    """详细解释 Python 的文档字符串和 __doc__ 属性"""
    print("=" * 60)
    print("Python 文档字符串（Docstring）详解")
    print("=" * 60)
    print()
    
    print("1. 什么是 __doc__？")
    print("-" * 60)
    print("   __doc__ 是 Python 的一个特殊属性（special attribute）")
    print("   用于访问函数、类、模块的文档字符串（docstring）")
    print("   类似 Node.js 中通过注释编写的 JSDoc")
    print()
    
    print("2. 什么是文档字符串（Docstring）？")
    print("-" * 60)
    print("   文档字符串是函数、类或模块的第一行字符串")
    print("   用三引号 '''...''' 或 \"\"\"...\"\"\" 包裹")
    print("   用于描述函数的功能、参数、返回值等")
    print()
    
    print("3. 基本用法示例")
    print("-" * 60)
    
    def greet(name):
        """简单的问候函数"""
        return f"Hello, {name}!"
    
    print("   函数定义:")
    print("   def greet(name):")
    print('       """简单的问候函数"""')
    print("       return f'Hello, {name}!'")
    print()
    print(f"   访问文档: greet.__doc__")
    print(f"   结果: {greet.__doc__}")
    print()
    
    print("4. 详细文档字符串（类似 JSDoc）")
    print("-" * 60)
    
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
    
    print("   函数定义:")
    print("   def calculate_area(length, width):")
    print('       """')
    print("       计算矩形面积")
    print("       ...")
    print('       """')
    print()
    print(f"   访问文档: calculate_area.__doc__")
    print("   结果:")
    print(calculate_area.__doc__)
    print()
    
    print("5. 文档字符串的格式规范")
    print("-" * 60)
    print("   Python 官方推荐使用 Google 风格或 NumPy 风格")
    print()
    print("   Google 风格示例:")
    print('   """')
    print("   函数简短描述")
    print()
    print("   详细描述（可选）")
    print()
    print("   Args:")
    print("       参数名: 参数说明")
    print()
    print("   Returns:")
    print("       返回值说明")
    print('   """')
    print()
    
    print("6. 与 Node.js JSDoc 对比")
    print("-" * 60)
    print("   Python:")
    print('   def calculate_area(length, width):')
    print('       """')
    print("       计算矩形面积")
    print("       ...")
    print('       """')
    print()
    print("   Node.js:")
    print("   /**")
    print("    * 计算矩形面积")
    print("    * @param {number} length - 长度")
    print("    * @param {number} width - 宽度")
    print("    * @returns {number} 面积值")
    print("    */")
    print("   function calculateArea(length, width) { ... }")
    print()
    
    print("7. 访问文档字符串的方法")
    print("-" * 60)
    
    def example_function():
        """这是一个示例函数"""
        pass
    
    # 方法1: 使用 __doc__ 属性
    print("   方法1: 使用 __doc__ 属性")
    print(f"   example_function.__doc__ = {example_function.__doc__}")
    print()
    
    # 方法2: 使用 help() 函数（更详细）
    print("   方法2: 使用 help() 函数（显示更详细的信息）")
    print("   help(example_function)")
    print("   （运行 help() 会显示更完整的文档）")
    print()
    
    # 方法3: 使用 inspect 模块
    import inspect
    print("   方法3: 使用 inspect 模块")
    doc = inspect.getdoc(example_function)
    print(f"   inspect.getdoc(example_function) = {doc}")
    print()
    
    print("8. 类的文档字符串")
    print("-" * 60)
    
    class Person:
        """人员类
        
        用于表示一个人的基本信息
        """
        
        def __init__(self, name):
            """初始化人员
            
            Args:
                name: 姓名
            """
            self.name = name
    
    print("   类的文档字符串:")
    print(f"   Person.__doc__ = {Person.__doc__}")
    print()
    print("   方法的文档字符串:")
    print(f"   Person.__init__.__doc__ = {Person.__init__.__doc__}")
    print()
    
    print("9. 模块的文档字符串")
    print("-" * 60)
    print("   文件顶部的三引号字符串就是模块的文档字符串")
    print("   例如这个文件开头的:")
    print('   """')
    print("   文档字符串（Docstring）详解")
    print("   ...")
    print('   """')
    print()
    print(f"   访问方式: __doc__ = {__doc__}")
    print()
    
    print("10. 实际应用场景")
    print("-" * 60)
    print("   ✅ 代码文档：帮助理解函数功能")
    print("   ✅ IDE 提示：编辑器会显示文档字符串")
    print("   ✅ 自动生成文档：工具可以提取文档字符串生成文档")
    print("   ✅ 交互式帮助：在 Python 交互环境中使用 help()")
    print()
    
    print("11. 最佳实践")
    print("-" * 60)
    print("   ✅ 为所有公共函数、类、模块编写文档字符串")
    print("   ✅ 使用三引号包裹多行文档")
    print("   ✅ 第一行写简短描述，空一行后写详细说明")
    print("   ✅ 说明参数类型和返回值")
    print("   ✅ 保持文档与代码同步更新")
    print()
    
    print("=" * 60)
    print("总结：__doc__ 是访问文档字符串的特殊属性")
    print("     类似 Node.js 中通过注释编写的 JSDoc")
    print("=" * 60)

if __name__ == "__main__":
    demo()

