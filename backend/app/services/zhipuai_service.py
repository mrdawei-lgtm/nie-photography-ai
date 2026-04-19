from app.core.config import settings
from typing import Dict, Any
import base64
import json
import httpx


class ZhipuAIService:
    """智谱AI服务（主模型：GLM-4.6V）- 使用HTTP API调用"""

    def __init__(self):
        self.api_key = settings.zhipuai_api_key
        self.model = settings.zhipuai_model
        self.base_url = "https://open.bigmodel.cn/api/paas/v4"

    async def analyze_image(self, image_base64: str) -> Dict[str, Any]:
        """
        使用智谱AI GLM-4.6V分析图片

        Args:
            image_base64: Base64编码的图片

        Returns:
            分析结果
        """
        # 构建提示词
        prompt = self._build_analysis_prompt()

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": self.model,
                        "messages": [
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": image_base64
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": prompt
                                    }
                                ]
                            }
                        ],
                        "temperature": 0.7,
                        "max_tokens": 1000
                    }
                )

                if response.status_code == 200:
                    result = response.json()
                    result_text = result["choices"][0]["message"]["content"]
                    return self._parse_result(result_text)
                else:
                    return {
                        "error": f"智谱AI API调用失败: {response.status_code}",
                        "details": response.text
                    }

        except Exception as e:
            print(f"智谱AI调用失败: {e}")
            return {"error": str(e)}

    def _build_analysis_prompt(self) -> str:
        """构建分析提示词"""
        return """你是一个专业的摄影助手。请分析这张照片，提供以下信息：

1. 主体识别：照片中的主要拍摄对象是什么（人物、动物、物体、风景）？
2. 主体位置：主体在画面中的位置（左侧、右侧、中心、上侧、下侧）？
3. 构图评估：
   - 主体是否突出？
   - 画面是否平衡？
   - 是否符合三分法？
   - 构图存在什么问题？
4. 光线评估：
   - 光线类型（顺光、侧光、逆光）？
   - 曝光是否合适？
5. 改进建议：
   - 给出2-3条具体的、可执行的建议
   - 建议要简洁明了，例如"向左移动一点"、"把主体放到右侧三分之一"、"靠近一点"

请以JSON格式返回结果，格式如下：
{
  "subject_type": "person|animal|object|landscape",
  "subject_position": "left|right|center|top|bottom",
  "composition_score": 85,
  "composition_issues": ["主体太靠边", "画面不平衡"],
  "lighting_type": "backlit|side_lit|front_lit",
  "exposure_quality": "good|underexposed|overexposed",
  "actionable_suggestions": ["向左移动一点", "把主体放到右侧三分之一"],
  "confidence": 0.9
}

只返回JSON，不要有其他文字。"""

    def _parse_result(self, result_text: str) -> Dict[str, Any]:
        """解析AI返回的结果"""
        try:
            # 尝试提取JSON
            start_idx = result_text.find('{')
            end_idx = result_text.rfind('}') + 1
            if start_idx >= 0 and end_idx > start_idx:
                json_str = result_text[start_idx:end_idx]
                return json.loads(json_str)
            else:
                return {"error": "无法解析AI返回结果", "raw": result_text}
        except json.JSONDecodeError as e:
            return {"error": f"JSON解析失败: {e}", "raw": result_text}
