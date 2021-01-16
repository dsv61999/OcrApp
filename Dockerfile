# python3のlatestのDocker imageをベースにする
FROM python:latest

# tesseractと依存ライブラリをaptでインストール
RUN apt-get update
RUN apt-get -y install \
    tesseract-ocr \
    tesseract-ocr-jpn
RUN apt-get clean

# 必要なpythonライブラリをpipでインストール
RUN pip install --upgrade pip; \
    pip install \
    pillow \
    pyocr

# 作業用ディレクトリを設定
WORKDIR /use/share/host/

ENTRYPOINT ["/usr/bin/tail", "-f", "/dev/null"]
