class Pristriy:
    def uvimknyty(self):
        return "Пристрій увімкнено"

    def vymknyty(self):
        return "Пристрій вимкнено"

class Televizor(Pristriy):
    def uvimknyty(self):
        return "Телевізор увімкнено"

class Noutbuk(Pristriy):
    def uvimknyty(self):
        return "Ноутбук увімкнено"

class Kholodylnyk(Pristriy):
    def uvimknyty(self):
        return "Холодильник працює"
