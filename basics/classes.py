"""
类和对象示例
对比 Node.js 的类定义
"""

def demo():
    """演示 Python 的类和对象"""
    print("1. 基本类定义")
    
    # Node.js:
    # class Person {
    #   constructor(name, age) {
    #     this.name = name;
    #     this.age = age;
    #   }
    #   greet() {
    #     return `Hello, I'm ${this.name}`;
    #   }
    # }
    
    class Person:
        """人员类"""
        
        def __init__(self, name, age):
            """构造函数（类似 constructor）"""
            self.name = name
            self.age = age
        
        def greet(self):
            """问候方法"""
            return f"Hello, I'm {self.name}, {self.age} years old"
        
        def __str__(self):
            """字符串表示（类似 toString）"""
            return f"Person(name={self.name}, age={self.age})"
    
    person = Person("Alice", 25)
    print(f"   {person.greet()}")
    print(f"   {person}")
    print()
    
    print("2. 类属性（类似静态属性）")
    class Counter:
        """计数器类"""
        count = 0  # 类属性
        
        def __init__(self):
            Counter.count += 1
            self.id = Counter.count
    
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    print(f"   创建了 {Counter.count} 个 Counter 实例")
    print(f"   c1.id = {c1.id}, c2.id = {c2.id}, c3.id = {c3.id}")
    print()
    
    print("3. 继承")
    # Node.js: class Student extends Person { ... }
    class Student(Person):
        """学生类（继承自 Person）"""
        
        def __init__(self, name, age, student_id):
            super().__init__(name, age)  # 调用父类构造函数
            self.student_id = student_id
        
        def study(self, subject):
            """学习方法"""
            return f"{self.name} is studying {subject}"
    
    student = Student("Bob", 20, "S12345")
    print(f"   {student.greet()}")
    print(f"   {student.study('Python')}")
    print()
    
    print("4. 属性装饰器（类似 getter/setter）")
    class Circle:
        """圆形类"""
        
        def __init__(self, radius):
            self._radius = radius  # 私有属性（约定用 _ 开头）
        
        @property
        def radius(self):
            """半径属性（getter）"""
            return self._radius
        
        @radius.setter
        def radius(self, value):
            """半径属性（setter）"""
            if value < 0:
                raise ValueError("半径不能为负数")
            self._radius = value
        
        @property
        def area(self):
            """面积属性（只读）"""
            return 3.14159 * self._radius ** 2
    
    circle = Circle(5)
    print(f"   圆的半径: {circle.radius}")
    print(f"   圆的面积: {circle.area:.2f}")
    circle.radius = 10
    print(f"   修改后半径: {circle.radius}, 面积: {circle.area:.2f}")

