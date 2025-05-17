class Tvaryna:
    def __init__(self, imya):
        self.imya = imya

    def zvuk(self):
        return "Тварина видає звук"

class Sobaka(Tvaryna):
    def __init__(self, imya, poroda):
        super().__init__(imya)
        self.poroda = poroda

    def zvuk(self):
        return f"{self.imya} гавкає"

class Kit(Tvaryna):
    def __init__(self, imya, kolir):
        super().__init__(imya)
        self.kolir = kolir

    def zvuk(self):
        return f"{self.imya} нявкає"
