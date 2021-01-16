#　枠線付きで文字を表示する関数
def showCaption(caption="caption"):
    blankLen = 3    # 余白の長さ
    strLen = len(caption)   # 文字の長さ
    blank = " "*blankLen
    line = "-"* (strLen + 2*blankLen)

    print("*" + line + "*")
    print("|" + blank + caption + blank + "|")
    print("*" + line + "*")

def showCaption_Em(caption="caption"):
    blankLen = 3    # 余白の長さ
    strLen = len(caption)*2   # 文字の長さ
    blank = " "*blankLen
    line = "-"* (strLen + 2*blankLen)

    print("*" + line + "*")
    print("|" + blank + caption + blank + "|")
    print("*" + line + "*")