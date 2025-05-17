class MovaProgramuvannya:
    def __init__(self, imya):
        self.imya = imya

    def vyvesty_pryvitannya(self):
        return f"Привіт! Це мова програмування {self.imya}."

class Python(MovaProgramuvannya):
    def __init__(self):
        super().__init__("Python")

class JavaScript(MovaProgramuvannya):
    def __init__(self):
        super().__init__("JavaScript")

class Java(MovaProgramuvannya):
    def __init__(self):
        super().__init__("Java")
