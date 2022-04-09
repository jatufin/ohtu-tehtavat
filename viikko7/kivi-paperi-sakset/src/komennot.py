from kps import KPS


class Komennot:
    def __init__(self, eka_ihminen, toka_ihminen, tietokone, parempi_tietokone, tuomari):
        self._komennot = {
            "a": Peli(eka_ihminen, toka_ihminen, tuomari),
            "b": Peli(eka_ihminen, tietokone, tuomari),
            "c": Peli(eka_ihminen, parempi_tietokone, tuomari)
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
    def __init__(self, eka_pelaaja, toka_pelaaja, tuomari):
        self._eka_pelaaja = eka_pelaaja
        self._toka_pelaaja = toka_pelaaja
        self._tuomari = tuomari

    def aloita(self):
        KPS.luo_peli(self._eka_pelaaja, self._toka_pelaaja, self._tuomari).pelaa()
