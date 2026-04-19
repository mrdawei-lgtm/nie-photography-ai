from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # 智谱AI配置（主模型：GLM-4.6V）
    zhipuai_api_key: str
    zhipuai_model: str = "glm-4.6v"

    # MiniMax配置（对比模型：MiniMax-VL）
    minimax_api_key: Optional[str] = None
    minimax_group_id: Optional[str] = None
    minimax_model: str = "minimax-vl"

    # API配置
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # 文件上传配置
    max_upload_size: int = 10485760  # 10MB
    allowed_extensions: str = "jpg,jpeg,png,heic"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
