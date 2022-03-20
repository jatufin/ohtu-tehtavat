class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    class Plus:
        def __init__(self, sovellus):
            self._sovellus = sovellus

        def suorita(self, arvo):
            self._sovellus.plus(arvo)

    class Miinus:
        def __init__(self, sovellus):
            self._sovellus = sovellus

        def suorita(self, arvo):
            self._sovellus.miinus(arvo)

    class Nollaus:
        def __init__(self, sovellus):
            self._sovellus = sovellus

        def suorita(self, arvo):
            self._sovellus.nollaa()

    class Kumoa:
        def __init__(self, sovellus):
            self._sovellus = sovellus

        def suorita(self, arvo):
            pass
