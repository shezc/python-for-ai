"""
Transformers 情感分析示例
使用 Hugging Face Transformers 进行文本情感分析

模型已下载到本地，从本地路径加载使用，无需网络连接
"""

import os
from pathlib import Path

# 配置本地模型存储目录 - C盘根目录下的models文件夹
MODELS_DIR = Path("C:/models")
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# 模型配置
MODEL_CONFIGS = {
    "chinese": {
        "name": "uer/roberta-base-finetuned-chinanews-chinese",
        "local_path": MODELS_DIR / "chinese-sentiment",
        "display_name": "中文情感分析模型"
    },
    "english": {
        "name": "distilbert-base-uncased-finetuned-sst-2-english",
        "local_path": MODELS_DIR / "english-sentiment",
        "display_name": "英文情感分析模型"
    }
}

# 自动配置镜像站（如果未设置环境变量）
MIRROR_ENDPOINT = 'https://hf-mirror.com'
if 'HF_ENDPOINT' not in os.environ:
    os.environ['HF_ENDPOINT'] = MIRROR_ENDPOINT

# 设置下载超时（可选，单位：秒）
# 如果网络较慢，可以增加这个值
if 'HF_HUB_DOWNLOAD_TIMEOUT' not in os.environ:
    os.environ['HF_HUB_DOWNLOAD_TIMEOUT'] = '300'  # 5分钟超时

from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch


def download_model(model_key="chinese", force_download=False):
    """
    下载模型到本地
    
    Args:
        model_key: 模型键名 ("chinese" 或 "english")
        force_download: 是否强制重新下载
    """
    if model_key not in MODEL_CONFIGS:
        raise ValueError(f"未知的模型键: {model_key}")
    
    config = MODEL_CONFIGS[model_key]
    local_path = config["local_path"]
    model_name = config["name"]
    
    # 检查模型是否已存在
    if local_path.exists() and not force_download:
        print(f"✅ {config['display_name']} 已存在于本地: {local_path}")
        return str(local_path)
    
    print(f"\n📥 正在下载 {config['display_name']}...")
    print(f"   模型: {model_name}")
    print(f"   保存到: {local_path}")
    print("   这可能需要几分钟时间，请耐心等待...\n")
    
    try:
        # 确保目录存在
        local_path.mkdir(parents=True, exist_ok=True)
        
        # 下载模型和分词器（先下载到临时位置，然后保存到指定路径）
        print("   正在下载模型文件...")
        # 注意: from_pretrained 不支持 timeout 参数
        # 超时设置需要通过环境变量 HF_HUB_DOWNLOAD_TIMEOUT 或 requests 库配置
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        
        # 保存到指定路径
        print("   正在保存到本地...")
        tokenizer.save_pretrained(str(local_path))
        model.save_pretrained(str(local_path))
        
        print(f"✅ {config['display_name']} 下载完成！")
        print(f"   保存位置: {local_path}\n")
        
        return str(local_path)
        
    except Exception as e:
        print(f"❌ 下载失败: {e}")
        print("\n提示:")
        print("1. 检查网络连接")
        print("2. 如果使用镜像，确保 HF_ENDPOINT 环境变量已设置")
        print("3. 可以手动设置镜像: os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'")
        raise


def get_model_path(model_key="chinese", auto_download=True):
    """
    获取模型本地路径，如果不存在则自动下载
    
    Args:
        model_key: 模型键名
        auto_download: 如果模型不存在是否自动下载
    """
    config = MODEL_CONFIGS[model_key]
    local_path = config["local_path"]
    
    if local_path.exists():
        return str(local_path)
    elif auto_download:
        return download_model(model_key)
    else:
        raise FileNotFoundError(
            f"模型不存在于 {local_path}，请先运行 download_model('{model_key}') 下载模型"
        )


def basic_sentiment_analysis():
    """基本情感分析示例（使用本地模型）"""
    print("=" * 60)
    print("1. 基本情感分析（使用本地模型）")
    print("=" * 60)
    
    try:
        # 获取本地模型路径（如果不存在会自动下载）
        model_path = get_model_path("chinese", auto_download=True)
        
        # 从本地路径加载模型
        classifier = pipeline("sentiment-analysis", model=model_path)
        
        print(f"classifier.model.config.id2label: {classifier.model.config.id2label}")

        # 测试文本
        texts = [
            "今天天气真好，心情很愉快！",
            "这部电影太糟糕了，完全不值得看。",
            "产品还不错，但价格有点贵。",
            "服务态度很好，推荐大家来试试。",
            "中国足球战胜了巴西男足"
        ]
        
        print("\n分析结果：")
        for text in texts:
            result = classifier(text)
            label = result[0]['label']
            score = result[0]['score']
            
            # 转换标签为中文
            print(f"result: {result[0]}")
            label_cn = "正面" if label == "POSITIVE" else "负面"
            
            print(f"\n文本: {text}")
            print(f"  情感: {label_cn}")
            print(f"  置信度: {score:.4f}")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    print("\n" + "=" * 60 + "\n")


def batch_sentiment_analysis():
    """批量情感分析示例（使用本地模型）"""
    print("=" * 60)
    print("3. 批量情感分析（使用本地模型）")
    print("=" * 60)
    
    try:
        # 获取本地模型路径
        model_path = get_model_path("chinese", auto_download=True)
        
        # 从本地路径加载模型
        classifier = pipeline("sentiment-analysis", model=model_path)
        
        # 批量文本
        texts = [
            "这个餐厅的菜品非常美味，环境也很优雅。",
            "快递太慢了，等了整整一周才收到。",
            "客服回复很快，问题解决得很及时。",
            "产品质量一般，性价比不高。",
            "非常满意，会再次购买！"
        ]
        
        print("\n批量分析结果：")
        # 批量处理（更高效）
        results = classifier(texts)
        
        for text, result in zip(texts, results):
            label = result['label']
            score = result['score']
            label_cn = "正面" if label == "POSITIVE" else "负面"
            
            print(f"\n文本: {text}")
            print(f"  情感: {label_cn} (置信度: {score:.4f})")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    print("\n" + "=" * 60 + "\n")


def detailed_sentiment_analysis():
    """详细的情感分析（使用本地模型）"""
    print("=" * 60)
    print("4. 详细情感分析（使用本地模型，获取原始分数）")
    print("=" * 60)
    
    try:
        # 获取本地模型路径
        model_path = get_model_path("chinese", auto_download=True)
        
        # 从本地路径加载模型
        classifier = pipeline("sentiment-analysis", 
                             model=model_path,
                             top_k=None)  # 返回所有类别的分数
        
        texts = [
            "这个电影太精彩了！",
            "服务态度很差，不推荐。"
        ]
        
        print("\n详细分析结果：")
        for text in texts:
            try:
                results = classifier(text)
                print(f"\n文本: {text}")
                
                # 处理返回结果：top_k=None 时返回格式为 [[{...}, {...}]]
                # 单个文本时，results 是 [[{label: 'POSITIVE', score: 0.9}, {label: 'NEGATIVE', score: 0.1}]]
                if isinstance(results, list):
                    # 获取第一个（也是唯一一个）文本的所有结果
                    if len(results) > 0 and isinstance(results[0], list):
                        text_results = results[0]
                    else:
                        text_results = results
                    
                    # 显示所有类别的分数
                    for result in text_results:
                        if isinstance(result, dict):
                            label = result.get('label', 'UNKNOWN')
                            score = result.get('score', 0.0)
                            label_cn = "正面" if label == "POSITIVE" else "负面"
                            print(f"  {label_cn}: {score:.4f}")
                        else:
                            print(f"  结果格式异常: {result}")
                else:
                    print(f"  无法解析结果类型: {type(results)}")
            except Exception as e:
                print(f"\n文本: {text}")
                print(f"  ❌ 处理出错: {e}")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        import traceback
        print("\n详细错误信息:")
        traceback.print_exc()
    
    print("\n" + "=" * 60 + "\n")


def download_all_models():
    """下载所有模型到本地"""
    print("\n" + "=" * 60)
    print("下载所有模型到本地")
    print("=" * 60)
    print(f"\n模型保存目录: {MODELS_DIR}\n")
    
    for model_key in MODEL_CONFIGS.keys():
        try:
            download_model(model_key, force_download=False)
        except Exception as e:
            print(f"❌ 下载 {model_key} 模型失败: {e}\n")
    
    print("=" * 60)
    print("所有模型下载完成！")
    print("=" * 60 + "\n")


def demo():
    """运行所有示例"""
    print("\n" + "=" * 60)
    print("Transformers 情感分析示例（本地模型）")
    print("=" * 60)
    
    # 显示模型目录
    print(f"\n📁 本地模型目录: {MODELS_DIR}")
    
    # 检查模型是否存在
    chinese_exists = MODEL_CONFIGS["chinese"]["local_path"].exists()
    english_exists = MODEL_CONFIGS["english"]["local_path"].exists()
    
    print(f"\n模型状态:{'✅ 已下载' if chinese_exists else '❌ 未下载'}")
    
    if not chinese_exists or not english_exists:
        print("\n💡 提示: 首次运行会自动下载缺失的模型")
        print("   也可以手动运行 download_all_models() 预先下载所有模型\n")
    
    try:
        # 基本情感分析
        basic_sentiment_analysis()
        
        # 批量分析
        # batch_sentiment_analysis()
        
        # 详细分析
        # detailed_sentiment_analysis()
        
        print("\n✅ 所有示例运行完成！")
    except Exception as e:
        print(f"\n❌ 运行出错: {e}")
        print("\n可能的解决方案:")
        print("1. 检查网络连接（首次下载需要网络）")
        print("2. 安装必要的依赖: pip install transformers torch")
        print("3. 如果网络问题，可以手动下载模型")
        print("4. 检查磁盘空间是否充足")


if __name__ == "__main__":
    import sys
    
    # 支持命令行参数
    if len(sys.argv) > 1 and sys.argv[1] == "download":
        # 下载所有模型
        download_all_models()
    else:
        # 运行示例
        demo()

