# シンプルなOCRアプリ
## 開発環境
- Docker 20.10.0
- Python 3.9.1
- Pillow     8.1.0
- pyocr      0.8
- tesseract 4.0.0
  
```docker:dockerのビルド
docker build -t [コンテナ名] [Dockerfileがあるパス]
```
```docker:ローカルフォルダとのマウント
docker run -v [ローカルパス]:/usr/share/host --name [コンテナ名] -it python /bin/bash
```