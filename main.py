import input
import display
import ocr
import output

#  見出し
display.showCaption("OcrApp")
display.showAA("こんにちは")

#  使用する言語の取得
lang = input.inputLang()
#  使用するタイプの取得
type = input.inputType()
#  入力画像のパスと名前の取得
imagePath, imageName = input.inputImage()
#  OCRの実行
ocrInstance = ocr.Ocr(lang, type)
txt = ocrInstance.ocr(imagePath)
#  結果の表示
display.showTxt(txt)
#  保存するかどうかの情報の取得
save = input.inputSave()
#  出力の保存
output.saveOutput(save, txt, imageName)

