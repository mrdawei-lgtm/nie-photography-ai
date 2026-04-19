from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # 智谱AI配置
    zhipuai_api_key: str
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
