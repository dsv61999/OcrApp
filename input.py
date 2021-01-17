import display

#  OCRタイプの入力処理を行う関数
def inputLang():
    langList = (1, 2)   #  存在する言語のリスト(型はタプル)
    langDict = {"1":"日本語", "2":"英語"}
    display.showCaption_Em("ＯＣＲの言語を選んでください")
    print("1・・・日本語")
    print("2・・・英語")
    print("*----------------------------------------*")
    lang = input()
    #  整数が入力されているかのチェック
    try:
        lang = int(lang)
    except:
        print("入力は「１」か「２」にしてください")
        return inputLang()
    #  存在する言語が入力されているか
    if(lang in langList):
        print("{}で読み込みます".format(langDict[str(lang)]))
        return str(lang)
    else:
        print("入力は「１」か「２」にしてください")
        return inputLang()

def inputType():
    typeList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)   #  存在するOCRタイプのリスト(型はタプル)
    display.showCaption_Em("ＯＣＲのタイプを選んでください")
    print("6・・・単一の均一なテキストブロックを想定します(デフォルト)")
    print("help・・・ＯＣＲのタイプ一覧をみることができます")
    print("*----------------------------------------------*")

    type = input()
    if (type=="help"):
        display.showHelp()
        #  整数が入力されているかのチェック
    try:
        type = int(type)
    except:
        print("入力は「0」〜「10」にしてください")
        return inputType()
    #  存在する言語が入力されているか
    if(type in typeList):
        print("タイプ{}で読み込みます".format(type))
        return type
    else:
        print("入力は「0」〜「10」にしてください")
        return inputType()
    

#  入力の処理を行うクラス
class InputConfig:
    def __init__(self, lang, type):
        self.lang = lang
        self.type = type
    
    def inputImage(self):
        display.showCaption_Em("画像を入力してください")
        imagePath = input()
        self.imagePath = imagePath
