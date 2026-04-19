from app.models.schemas import (
    AnalysisResult,
    SubjectInfo,
    LightingInfo,
    CompositionAnalysis,
    SubjectType
)
from app.services.zhipuai_service import ZhipuAIService
import uuid


class AnalysisService:
    """图片分析服务"""

    def __init__(self):
        self.ai_service = ZhipuAIService()

    def analyze_photo(self, image_base64: str) -> AnalysisResult:
        """
        分析照片

        Args:
            image_base64: Base64编码的图片

        Returns:
            分析结果
        """
        # 调用AI分析
        ai_result = self.ai_service.analyze_image(image_base64)

        if "error" in ai_result:
            raise Exception(f"AI分析失败: {ai_result['error']}")

        # 转换为我们的数据模型
        subject = self._parse_subject(ai_result)
        lighting = self._parse_lighting(ai_result)
        composition = self._parse_composition(ai_result)

        return AnalysisResult(
            image_id=str(uuid.uuid4()),
            overall_score=ai_result.get("composition_score", 70),
            subjects=[subject],
            lighting=lighting,
            composition=composition,
            actionable_suggestions=ai_result.get("actionable_suggestions", [])
        )

    def _parse_subject(self, ai_result: dict) -> SubjectInfo:
        """解析主体信息"""
        position_map = {
            "left": 0.2,
            "right": 0.8,
            "center": 0.5,
            "top": 0.5,
            "bottom": 0.5
        }

        subject_type = ai_result.get("subject_type", "unknown")
        try:
            type_enum = SubjectType(subject_type)
        except ValueError:
            type_enum = SubjectType.UNKNOWN

        position = ai_result.get("subject_position", "center")
        x = position_map.get(position, 0.5)
        y = 0.5  # 默认垂直居中

        return SubjectInfo(
            type=type_enum,
            bounding_box={
                "x": x - 0.1,  # 简化处理，假设主体占20%
                "y": y - 0.15,
                "width": 0.2,
                "height": 0.3
            },
            confidence=ai_result.get("confidence", 0.8),
            is_primary=True
        )

    def _parse_lighting(self, ai_result: dict) -> LightingInfo:
        """解析光线信息"""
        lighting_type = ai_result.get("lighting_type", "front_lit")
        exposure = ai_result.get("exposure_quality", "good")

        brightness = 0.5  # 默认值
        if exposure == "underexposed":
            brightness = 0.3
        elif exposure == "overexposed":
            brightness = 0.8

        return LightingInfo(
            type=lighting_type,
            brightness=brightness,
            exposure_quality=exposure
        )

    def _parse_composition(self, ai_result: dict) -> CompositionAnalysis:
        """解析构图分析"""
        return CompositionAnalysis(
            score=ai_result.get("composition_score", 70),
            rule_name="rule_of_thirds",  # MVP默认
            violated_rules=ai_result.get("composition_issues", []),
            suggestions=ai_result.get("actionable_suggestions", [])
        )
