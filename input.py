class ShowCaption:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("*------------*")
        print("|    {}    |".format(self.name))
        print("*------------*")

def showCaption():
    print("*------------*")
    print("|   OcrApp   |")
    print("*------------*")