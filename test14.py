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


'''cat = Animal()
cat.is_mammals()
cat.is_domestic()'''


class Dogs(Animal):
    def __init__(self, legs=4, tale=True, domestic=True, mammals=True):
        super().__init__(legs, tale, domestic, mammals)

    def is_mammals(self):
        super().is_mammals()


sharik = Dogs()
sharik.is_mammals()


class Horse(Animal):
    def __init__(self, legs=4, tale=True):
        super().__init__(legs, tale)

    def legs_and_tale(self):
        if self.legs == 4 and self.tale == True:
            print("4 ноги и хвост")


horse = Horse()
horse.legs_and_tale()
