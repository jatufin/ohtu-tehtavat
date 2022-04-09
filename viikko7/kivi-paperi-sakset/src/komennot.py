from kps import KPS


class Komennot:
    def __init__(self, eka, toka, tekoaly, parempi_tekoaly, tuomari):
        self._komennot = {
            "a": Peli(eka, toka, tuomari),
            "b": Peli(eka, tekoaly, tuomari),
            "c": Peli(eka, parempi_tekoaly, tuomari)
        }

    def suorita(self, komento):
        if komento not in self._komennot:
            return False

        self._komennot[komento].aloita()

        return True

    def valikko(self, pelaaja):
        teksti = """
Valitse pelataanko
(a) Ihmistä vastaan
(b) Tekoälyä vastaan
(c) Parannettua tekoälyä vastaan
Muilla valinnoilla lopetetaan"""
        pelaaja.kirjoita(teksti)

        return pelaaja.lue()


class Peli:
    def __init__(self, eka, toka, tuomari):
        self._eka = eka
        self._toka = toka
        self._tuomari = tuomari

    def aloita(self):
        KPS.luo_peli(self._eka, self._toka, self._tuomari).pelaa()
