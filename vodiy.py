class Osoba:
    def __init__(self, imya, vik):
        self.imya = imya
        self.vik = vik

    def pokazaty_vik(self):
        return f"{self.imya} має {self.vik} років"

class Vodiy(Osoba):
    def __init__(self, imya, vik, nomer_posvidchennya):
        super().__init__(imya, vik)
        self.nomer_posvidchennya = nomer_posvidchennya

    def informatsiya(self):
        return f"{self.imya}, {self.vik} років, посвідчення №{self.nomer_posvidchennya}"
