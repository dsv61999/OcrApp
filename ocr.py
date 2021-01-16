from PIL import Image
import sys

import pyocr
import pyocr.builders

import display

class Ocr:
    def __init__(self, name):
        self.name = name

    def ocr(self, imagePath="imagePath"):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found")
            sys.exit(1)

        tool = tools[0]
        print("Will use tool '%s'" % (tool.get_name()))

        txt = tool.image_to_string(
            Image.open(imagePath),
            lang="jpn",
            builder=pyocr.builders.TextBuilder(tesseract_layout=6)
        )
        display.showCaption_Em("実行結果")

        print( txt )