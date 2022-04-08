class KonsoliIO:
    def lue(self, teksti=""):
        return input(teksti)

    def kirjoita(self, *teksti):
        for rivi in teksti:
            print(rivi)
