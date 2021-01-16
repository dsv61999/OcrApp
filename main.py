from PIL import Image
import sys

import pyocr
import pyocr.builders

import input

# OcrApp = input.ShowCaption("OcrApp")
# OcrApp.show()

input.showCaption()
# tools = pyocr.get_available_tools()
# if len(tools) == 0:
#     print("No OCR tool found")
#     sys.exit(1)

# tool = tools[0]
# print("Will use tool '%s'" % (tool.get_name()))

# txt = tool.image_to_string(
#     Image.open("./sample_data/wiki.png"),
#     lang="jpn",
#     builder=pyocr.builders.TextBuilder(tesseract_layout=6)
# )
# print( txt )