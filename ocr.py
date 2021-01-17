from PIL import Image
import sys

import pyocr
import pyocr.builders

class Ocr:
    def __init__(self, lang, type):
        self.lang = lang
        self.type = type

    def ocr(self, imagePath="imagePath"):
        langDict = {"1":"jpn", "2":"eng"}
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found")
            sys.exit(1)

        tool = tools[0]
        # print("Will use tool '%s'" % (tool.get_name()))
        txt = tool.image_to_string(
            Image.open(imagePath),
            lang=langDict[self.lang],
            builder=pyocr.builders.TextBuilder(tesseract_layout=self.type)
        )

        return txt