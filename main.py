import input
import display
import ocr

display.showCaption("OcrApp")
display.showAA("こんにちは")
type = input.inputType()
config = input.InputConfig(type)
config.inputImage()

# print(config.imagePath)

ocrInstance = ocr.Ocr(type)
ocrInstance.ocr(config.imagePath)
