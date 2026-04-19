# Nie - AI辅助摄影App

> 相机里的AI拍摄助手

## 项目简介

Nie（读音：捏）是一个AI辅助摄影App，帮助用户在拍摄当下快速得到更好的照片。核心不是教学，而是直接告诉用户"现在该怎么拍更好"。

## 核心功能

- 📸 **拍后分析**：照片评分、构图问题识别、改进建议
- 🎯 **构图建议**：主体位置优化、画面平衡、留白建议
- ✂️ **智能裁切**：自动生成更优构图版本
- 🔍 **主体识别**：自动识别拍摄主体

## 技术栈

### 移动端
- **Flutter** - 跨平台移动应用框架
- **Swift + SwiftUI** - iOS原生特性集成（需要时）

### 后端
- **Python + FastAPI** - 轻量级API服务
- **智谱AI GLM-4V** - 视觉分析大模型
- **Google Vision API** - 物体检测（备选）

## 项目结构

```
nie-photography-ai/
├── backend/          # 后端API服务
│   ├── app/         # FastAPI应用
│   ├── models/      # 数据模型
│   ├── services/    # 业务逻辑
│   └── tests/       # 测试
├── mobile/          # Flutter移动端
│   ├── lib/        # Dart代码
│   └── ios/        # iOS原生配置
├── docs/            # 项目文档
└── scripts/         # 脚本工具
```

## 开发优先级

1. 构图分析
2. 构图建议
3. 照片评分
4. 智能裁切
5. 主体识别

## 非目标

- ❌ 修图/滤镜
- ❌ 社交系统
- ❌ 内容社区
- ❌ 自研大模型

## 快速开始

### 后端
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 移动端
```bash
cd mobile
flutter run
```

## 许可证

MIT License
