from fastapi import APIRouter, HTTPException
from app.models.schemas import AnalysisRequest, AnalysisResponse
from app.services.analysis_service import AnalysisService
import base64

router = APIRouter()
analysis_service = AnalysisService()


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_photo(request: AnalysisRequest):
    """
    分析照片，提供构图和拍摄建议

    - **image_data**: Base64编码的图片数据
    - **include_crop_suggestion**: 是否包含裁切建议（MVP阶段暂不实现）
    """
    try:
        # 直接使用Base64数据
        # 假设前端已经去掉了data:image/xxx;base64,前缀
        image_data = request.image_data

        # 执行分析（异步）
        result = await analysis_service.analyze_photo(image_data)

        return AnalysisResponse(
            success=True,
            data=result
        )

    except Exception as e:
        return AnalysisResponse(
            success=False,
            error=str(e)
        )


@router.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "ok", "service": "analysis"}
