class KonsoliIO:
    def __init__(self, null_output=False):
        self._null_output = null_output

    def lue(self, teksti=""):
        return input(teksti)

    def kirjoita(self, teksti):
        if not self._null_output:
            print(teksti)


class TekoalyIO():
    def __init__(self, tekoaly):
        self._tekoaly = tekoaly

    def lue(self, teksti=""):
        return self._tekoaly.anna_siirto()

    def kirjoita(self, teksti):
        if self._on_siirto(teksti):
            self._tekoaly.aseta_siirto(teksti)

    def _on_siirto(self, siirto):
        return len(siirto) == 1 and siirto in "kps"
