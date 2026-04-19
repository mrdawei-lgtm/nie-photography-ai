### 移动端
```bash
cd mobile
# 创建iOS项目
xcodebuild -list
# 或者使用Xcode创建新项目
```

## 依赖安装（Swift Package Manager）

### 主依赖
- Alamofire - HTTP网络请求
- Kingfisher - 图片加载和缓存
- SwiftUI

### 项目结构

```
mobile/
├── Nie/
│   ├── App/
│   │   ├── NieApp.swift
│   │   └── ContentView.swift
│   ├── Models/          # 数据模型
│   ├── Services/        # API服务
│   ├── Views/           # 页面视图
│   │   ├── CameraView.swift
│   │   ├── ResultView.swift
│   │   └── ...
│   └── Resources/       # 资源文件
└── Nie.xcodeproj
```

## 配置Info.plist

添加相机和相册权限：
```xml
<key>NSCameraUsageDescription</key>
<string>需要使用相机拍摄照片</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>需要访问相册选择照片</string>
```
