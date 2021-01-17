import display

#  OCRタイプの入力処理を行う関数
def inputType():
    typeList = (1, 2)   #  存在するOCRタイプのリスト(型はタプル)
    display.showCaption_Em("ＯＣＲのタイプを選んでください")
    print("type1  ・・・日本語")
    print("type2  ・・・英語")
    type = input()
    #  整数が入力されているかのチェック
    try:
        type = int(type)
    except:
        print("入力は「１」か「２」にしてください")
        return inputType()
    #  存在するタイプが入力されているか
    if(type in typeList):
        return str(type)
    else:
        print("入力は「１」か「２」にしてください")
        return inputType()

#  入力の処理を行うクラス
class InputConfig:
    def __init__(self, type):
        self.type = type
    
    def inputImage(self):
        display.showCaption_Em("画像を入力してください")
        imagePath = input()
        self.imagePath = imagePath
