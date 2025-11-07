"""
文件操作示例
对比 Node.js 的 fs 模块
"""

import os

def demo():
    """演示 Python 的文件操作"""
    print("1. 写入文件（类似 fs.writeFileSync）")
    
    # Node.js: fs.writeFileSync('test.txt', 'Hello Python')
    content = "Hello Python!\n这是第二行\n这是第三行"
    
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write(content)
    
    print("   ✅ 已创建 test.txt")
    print()
    
    print("2. 读取文件（类似 fs.readFileSync）")
    # Node.js: const content = fs.readFileSync('test.txt', 'utf-8')
    with open("test.txt", "r", encoding="utf-8") as f:
        file_content = f.read()
    
    print(f"   文件内容:\n{file_content}")
    print()
    
    print("3. 逐行读取（类似 readline）")
    with open("test.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    print("   逐行内容:")
    for i, line in enumerate(lines, 1):
        print(f"   第 {i} 行: {line.strip()}")
    print()
    
    print("4. 追加内容（类似 fs.appendFileSync）")
    # Node.js: fs.appendFileSync('test.txt', '\n追加的内容')
    with open("test.txt", "a", encoding="utf-8") as f:
        f.write("\n这是追加的内容")
    
    print("   ✅ 已追加内容到 test.txt")
    print()
    
    print("5. 检查文件是否存在（类似 fs.existsSync）")
    # Node.js: fs.existsSync('test.txt')
    file_exists = os.path.exists("test.txt")
    print(f"   test.txt 存在: {file_exists}")
    print()
    
    print("6. 获取文件信息（类似 fs.statSync）")
    if file_exists:
        file_size = os.path.getsize("test.txt")
        print(f"   文件大小: {file_size} 字节")
    print()
    
    print("7. 读取 JSON 文件")
    import json
    
    # 创建示例 JSON 数据
    data = {
        "name": "Python 学习项目",
        "version": "1.0.0",
        "author": "你",
        "languages": ["Python", "JavaScript"]
    }
    
    # 写入 JSON
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("   ✅ 已创建 data.json")
    
    # 读取 JSON
    with open("data.json", "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    
    print(f"   读取的 JSON 数据: {loaded_data}")
    print()
    
    print("💡 提示: Python 的 'with' 语句会自动关闭文件")
    print("   类似 Node.js 的 try-finally 或使用 fs.promises")

