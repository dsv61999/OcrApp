import input
import display
import ocr

# OcrApp = input.ShowCaption("OcrApp")
# OcrApp.show()
display.showCaption("OcrApp")
config = input.InputConfig("aa")
config.inputImage()

# print(config.imagePath)

ocrInstance = ocr.Ocr("ocrInstance")
ocrInstance.ocr(config.imagePath)
