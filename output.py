import display

# 入力画像の名前(拡張子を除いた)を取得する関数
def get_image_name(imageName="sample.png"):
    extension = imageName.rfind(".")  #  後ろから"."を探して、そのインデックスをextensionに代入
    imageName = imageName[0:extension]
    return imageName

#  OCR出力を保存する関数
def saveOutput(save, txt, imageName):
    if (save):
        with open("./output/" + imageName + ".txt", "w") as f:  #  outputフォルダに保存する
            print(txt, file=f)
        print("./output/" + imageName + ".txt を保存しました" )
    else:
        print("出力結果を保存しませんでした")