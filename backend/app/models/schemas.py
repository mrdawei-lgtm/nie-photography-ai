from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from enum import Enum


class CompositionRule(str, Enum):
    """构图规则类型"""
    RULE_OF_THIRDS = "rule_of_thirds"
    CENTERED = "centered"
    LEADING_LINES = "leading_lines"
    SYMMETRY = "symmetry"


class SubjectType(str, Enum):
    """主体类型"""
    PERSON = "person"
    ANIMAL = "animal"
    OBJECT = "object"
    LANDSCAPE = "landscape"
    UNKNOWN = "unknown"


class SubjectInfo(BaseModel):
    """主体信息"""
    type: SubjectType
    bounding_box: Dict[str, float]  # {x, y, width, height} 0-1归一化坐标
    confidence: float
    is_primary: bool = True


class LightingInfo(BaseModel):
    """光线信息"""
    type: str  # backlit, side_lit, front_lit
    brightness: float  # 0-1
    exposure_quality: str  # good, underexposed, overexposed


class CompositionAnalysis(BaseModel):
    """构图分析结果"""
    score: float  # 0-100
    rule_name: Optional[str] = None
    violated_rules: List[str] = []
    suggestions: List[str] = []


class AnalysisResult(BaseModel):
    """完整的分析结果"""
    image_id: str
    overall_score: float
    subjects: List[SubjectInfo]
    lighting: LightingInfo
    composition: CompositionAnalysis
    actionable_suggestions: List[str]  # 可执行的建议


class AnalysisRequest(BaseModel):
    """分析请求"""
    image_data: str  # Base64编码的图片
    include_crop_suggestion: bool = False


class AnalysisResponse(BaseModel):
    """分析响应"""
    success: bool
    data: Optional[AnalysisResult] = None
    error: Optional[str] = None
