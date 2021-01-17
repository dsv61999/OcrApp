import input
import display
import ocr

display.showCaption("OcrApp")
display.showAA("こんにちは")
lang = input.inputLang()
type = input.inputType()
config = input.InputConfig(lang, type)
config.inputImage()

# print(config.imagePath)

ocrInstance = ocr.Ocr(lang, type)
ocrInstance.ocr(config.imagePath)
