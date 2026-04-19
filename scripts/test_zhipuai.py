#!/usr/bin/env python3
"""
测试智谱AI集成
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.services.zhipuai_service import ZhipuAIService
import base64


def test_zhipuai():
    """测试智谱AI"""
    print("测试智谱AI集成...")

    # 读取测试图片
    # 这里需要你提供一个测试图片的路径
    test_image_path = "test_photo.jpg"

    if not os.path.exists(test_image_path):
        print(f"错误：找不到测试图片 {test_image_path}")
        print("请在该目录下放置一张测试照片，命名为 test_photo.jpg")
        return

    # 读取并编码图片
    with open(test_image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')

    # 调用服务
    service = ZhipuAIService()
    result = service.analyze_image(image_data)

    print("\n分析结果：")
    print("-" * 50)
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("-" * 50)


if __name__ == "__main__":
    test_zhipuai()
