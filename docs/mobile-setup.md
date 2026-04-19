# 移动端开发环境配置

## Flutter安装

### macOS

1. 下载Flutter SDK:
   ```bash
   cd ~/development
   unzip ~/Downloads/flutter_macos_arm64_3.24.5-stable.zip
   export PATH="$PATH:`pwd`/flutter/bin"
   ```

2. 验证安装:
   ```bash
   flutter doctor
   ```

3. 安装依赖:
   ```bash
   flutter precache
   ```

### 初始化项目

```bash
cd mobile
flutter create --org com.nie --platforms ios .
```

## 依赖安装

```bash
cd mobile
flutter pub add camera image_picker http dio
flutter pub add provider
```

## 项目结构

```
mobile/
├── lib/
│   ├── main.dart
│   ├── models/          # 数据模型
│   ├── services/        # API服务
│   ├── screens/         # 页面
│   └── widgets/         # 组件
├── ios/                 # iOS原生配置
└── pubspec.yaml
```
