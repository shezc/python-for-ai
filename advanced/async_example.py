"""
异步编程示例
对比 Node.js 的 async/await
"""

import asyncio
import time

async def demo():
    """演示 Python 的异步编程"""
    print("1. 基本异步函数（类似 async function）")
    
    # Node.js: async function fetchData() { ... }
    async def fetch_data(delay, name):
        """模拟异步数据获取"""
        print(f"   开始获取 {name}...")
        await asyncio.sleep(delay)  # 类似 await new Promise(resolve => setTimeout(resolve, delay))
        print(f"   ✅ {name} 获取完成")
        return f"{name} 的数据"
    
    # 运行单个异步函数
    result = await fetch_data(1, "用户信息")
    print(f"   结果: {result}")
    print()
    
    print("2. 并发执行（类似 Promise.all）")
    # Node.js: await Promise.all([fetchData(1), fetchData(2), fetchData(3)])
    start_time = time.time()
    
    results = await asyncio.gather(
        fetch_data(1, "数据A"),
        fetch_data(1, "数据B"),
        fetch_data(1, "数据C")
    )
    
    elapsed = time.time() - start_time
    print(f"   所有任务完成，耗时: {elapsed:.2f}秒")
    print(f"   结果: {results}")
    print()
    
    print("3. 异步循环（类似 for await）")
    async def process_items(items):
        """处理多个项目"""
        results = []
        for item in items:
            data = await fetch_data(0.5, f"项目{item}")
            results.append(data)
        return results
    
    items = [1, 2, 3, 4]
    processed = await process_items(items)
    print(f"   处理结果: {processed}")
    print()
    
    print("4. 异步生成器（类似 async generator）")
    async def async_generator(n):
        """异步生成器"""
        for i in range(n):
            await asyncio.sleep(0.1)
            yield i
    
    print("   异步生成器输出:")
    async for value in async_generator(5):
        print(f"     生成值: {value}")
    print()
    
    print("5. 超时处理（类似 Promise.race）")
    async def slow_task():
        """慢任务"""
        await asyncio.sleep(5)
        return "完成"
    
    try:
        # 设置超时
        result = await asyncio.wait_for(slow_task(), timeout=2.0)
        print(f"   结果: {result}")
    except asyncio.TimeoutError:
        print("   ⏰ 任务超时")
    print()
    
    print("6. 异步上下文管理器（类似 async with）")
    class AsyncResource:
        """异步资源管理器"""
        async def __aenter__(self):
            print("   打开资源...")
            await asyncio.sleep(0.1)
            return self
        
        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print("   关闭资源...")
            await asyncio.sleep(0.1)
    
    async with AsyncResource() as resource:
        print("   使用资源...")
        await asyncio.sleep(0.1)
    print()
    
    print("💡 提示:")
    print("   - async def 类似 async function")
    print("   - await 类似 await")
    print("   - asyncio.gather() 类似 Promise.all()")
    print("   - asyncio.wait_for() 类似 Promise.race()")

def run_demo():
    """运行异步示例"""
    # Python 3.7+ 可以使用 asyncio.run()
    asyncio.run(demo())

