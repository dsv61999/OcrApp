import display

#  OCR言語の入力処理を行う関数
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

#  OCRタイプの入力処理を行う関数
def inputType():
    typeList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)   #  存在するOCRタイプのリスト(型はタプル)
    display.showCaption_Em("ＯＣＲのタイプを選んでください")
    print("6・・・単一の均一なテキストブロックを想定します(デフォルト)")
    print("help・・・ＯＣＲのタイプ一覧をみることができます")
    print("*--------------------------------------------------------------*")

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

#  画像の入力を処理する関数
def inputImage():
    display.showCaption_Em("画像を入力してください")
    imageName = input()
    imagePath = "./input/" + imageName  #  入力画像はinputフォルダ内に保存しておく
    print("{}の画像を読み込みます".format(imagePath))
    return imagePath, imageName

#  出力を保存するかの入力を処理する関数
def inputSave():
    display.showCaption_Em("出力結果を保存しますか？")
    print("y or yes・・・保存する")
    print("n or no・・・保存しない")
    print("*----------------------------------------*")
    save = input()
    if (save == "y" or save == "yes"):
        return True
    elif (save == "n" or save == "no"):
        return False
    else:
        print("入力は「y」か 「yes」か「n」か「no」にしてください")
        return inputSave()

