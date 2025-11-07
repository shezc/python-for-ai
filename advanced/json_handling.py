"""
JSON 处理示例
对比 Node.js 的 JSON 对象
"""

import json

def demo():
    """演示 Python 的 JSON 处理"""
    print("1. JSON 序列化（类似 JSON.stringify）")
    
    # Node.js: JSON.stringify({ name: "Python", version: "3.11" })
    data = {
        "name": "Python",
        "version": "3.11",
        "features": ["简单", "强大", "易学"],
        "is_awesome": True,
        "null_value": None
    }
    
    json_string = json.dumps(data, ensure_ascii=False, indent=2)
    print("   JSON 字符串:")
    print(json_string)
    print()
    
    print("2. JSON 反序列化（类似 JSON.parse）")
    # Node.js: JSON.parse('{"name": "Python"}')
    json_str = '{"name": "Python", "age": 30, "active": true}'
    parsed_data = json.loads(json_str)
    print(f"   解析结果: {parsed_data}")
    print(f"   类型: {type(parsed_data).__name__}")
    print()
    
    print("3. 处理嵌套 JSON")
    complex_data = {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ],
        "metadata": {
            "total": 2,
            "page": 1
        }
    }
    
    json_output = json.dumps(complex_data, ensure_ascii=False, indent=2)
    print("   复杂 JSON 结构:")
    print(json_output)
    print()
    
    print("4. 从文件读取 JSON（类似 fs.readFileSync + JSON.parse）")
    # 先创建一个 JSON 文件
    sample_data = {
        "project": "Python 学习",
        "status": "进行中",
        "progress": 75
    }
    
    with open("sample.json", "w", encoding="utf-8") as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)
    
    # 读取 JSON 文件
    with open("sample.json", "r", encoding="utf-8") as f:
        loaded = json.load(f)
    
    print(f"   从文件读取: {loaded}")
    print()
    
    print("5. 处理 JSON 数组")
    items = [
        {"id": 1, "name": "项目 A"},
        {"id": 2, "name": "项目 B"},
        {"id": 3, "name": "项目 C"}
    ]
    
    items_json = json.dumps(items, ensure_ascii=False, indent=2)
    print("   JSON 数组:")
    print(items_json)
    print()
    
    print("6. 错误处理")
    try:
        invalid_json = "{'name': 'Python'}"  # 单引号不是有效的 JSON
        json.loads(invalid_json)
    except json.JSONDecodeError as e:
        print(f"   ❌ JSON 解析错误: {e}")
    print()
    
    print("💡 提示:")
    print("   - json.dumps() 类似 JSON.stringify()")
    print("   - json.loads() 类似 JSON.parse()")
    print("   - json.dump() / json.load() 用于文件操作")

