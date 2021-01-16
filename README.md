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
<!-- ```docker:ローカルフォルダとのマウント
docker run -v [ローカルパス]:/usr/share/host --name [コンテナ名] -it [イメージ名] /bin/bash
``` 
マウントがうまくいかなかった
pythonイメージでマウントするとうまくいったので、pythonイメージからDockerfile通りにインストールした
-->

### 参考
- [tesseract+pytesseractのdockerコンテナ](https://qiita.com/cranpun/items/704a32f0def141ea1da4)