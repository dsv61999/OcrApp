import display

class InputConfig:
    def __init__(self, name):
        self.name = name
    def inputImage(self):
        display.showCaption_Em("画像を入力してください")
        imagePath = input()
        self.imagePath = imagePath
