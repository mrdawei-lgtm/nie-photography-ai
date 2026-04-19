# 后端开发环境配置

## Python环境

### 创建虚拟环境

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 或 venv\Scripts\activate  # Windows
```

### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置环境变量

```bash
cp .env.example .env
# 编辑.env文件，填入你的API密钥
```

## 获取智谱AI API密钥

1. 访问 https://open.bigmodel.cn/
2. 注册/登录账号
3. 创建API Key
4. 复制到 `.env` 文件中的 `ZHIPUAI_API_KEY`

## 运行开发服务器

```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API文档

启动服务器后，访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 测试

```bash
pytest
```
