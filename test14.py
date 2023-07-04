class Animal:
    def __init__(self, legs=4, tale=True, domestic=True, mammals=True):
        self.legs = legs
        self.tale = tale
        self.domestic = domestic
        self.mammals = mammals

    def is_mammals(self):
        if self.mammals == True:
            print("mammals")

    def is_domestic(self):
        if self.domestic == True:
            print("domestic")


cat = Animal(4, True, True, True)
cat.is_mammals()
cat.is_domestic()
