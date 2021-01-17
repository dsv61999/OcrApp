#　枠線付きで文字を表示する関数
def showCaption(caption="caption"):
    blankLen = 3    # 余白の長さ
    strLen = len(caption)   # 文字の長さ
    blank = " "*blankLen
    line = "-"* (strLen + 2*blankLen)

    print("*" + line + "*")
    print("|" + blank + caption + blank + "|")
    print("*" + line + "*")

#  枠線付きで文字を表示する関数(全角用)
def showCaption_Em(caption="caption"):
    blankLen = 3    # 余白の長さ
    strLen = len(caption)*2   # 文字の長さ
    blank = " "*blankLen
    line = "-"* (strLen + 2*blankLen)

    print("*" + line + "*")
    print("|" + blank + caption + blank + "|")
    print("*" + line + "*")

#  アスキーアートを表示する関数
def showAA(word="Hello"):
    print("　　{}".format(word))
    print("  ／ーーー＼")
    print(" /・　 ・　 ＼/|")
    print("／ーーー＼　　 |")
    print("｜ ――― ｜　　｜|")
    print("＼＿＿＿／　　 |")
    print("　　＼　　　　／")
    print("　　　ーーーー)")

#  ＯＣＲのタイプ一覧を表示する関数
def showHelp():
    print("0・・・方向とスクリプト検出(OSD)のみ")
    print("1・・・OSDによる自動ページセグメンテーション")
    print("2・・・自動ページセグメンテーション。OSDまたはOCRなし")
    print("3・・・完全自動のページセグメンテーション。OSDなし")
    print("4・・・可変サイズのテキストの単一列を想定します")
    print("5・・・垂直に配置されたテキストの単一の均一なブロックを想定します")
    print("6・・・単一の均一なテキストブロックを想定します")
    print("7・・・画像を単一のテキスト行として扱います")
    print("8・・・画像を1つの単語として扱います")
    print("9・・・画像を円の中の1つの単語として扱います")
    print("10・・・画像を単一の文字として扱います")

#  テキスト(実行結果)を表示する関数
def showTxt(txt):
    showCaption_Em("実行結果")
    print( txt )