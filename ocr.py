from PIL import Image
import sys

import pyocr
import pyocr.builders

import display

class Ocr:
    def __init__(self, type):
        self.type = type

    def ocr(self, imagePath="imagePath"):
        lang = {"1":"jpn", "2":"eng"}
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found")
            sys.exit(1)

        tool = tools[0]
        print("タイプ{}で読み込みました".format(self.type))
        # print("Will use tool '%s'" % (tool.get_name()))
        txt = tool.image_to_string(
            Image.open(imagePath),
            lang=lang[self.type],
            builder=pyocr.builders.TextBuilder(tesseract_layout=6)
        )
        display.showCaption_Em("実行結果")

        print( txt )