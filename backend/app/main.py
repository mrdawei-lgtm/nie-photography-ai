from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import analysis
from app.core.config import settings

app = FastAPI(
    title="Nie Photography AI",
    description="AI辅助摄影API服务",
    version="0.1.0"
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境需要限制
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(analysis.router, prefix="/api/v1", tags=["analysis"])


@app.get("/")
async def root():
    return {"message": "Nie Photography AI API", "version": "0.1.0"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
