from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # MiniMax配置（主模型）
    minimax_api_key: str
    minimax_group_id: str
    minimax_model: str = "vision-v1"

    # 智谱AI配置（备选模型）
    zhipuai_api_key: Optional[str] = None
    zhipuai_model: str = "glm-4v"

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
