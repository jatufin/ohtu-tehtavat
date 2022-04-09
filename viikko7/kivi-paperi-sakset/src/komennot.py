from kps import KPS


class Komennot:
    def __init__(self, eka_io, toka_io, tekoaly_io, parempi_tekoaly_io, tuomari):
        self._komennot = {
            "a": Peli(eka_io, toka_io, tuomari),
            "b": Peli(eka_io, tekoaly_io, tuomari),
            "c": Peli(eka_io, parempi_tekoaly_io, tuomari)
        }

    def suorita(self, komento):
        if komento not in self._komennot:
            return False

        self._komennot[komento].aloita()

        return True
    
    def valikko(self, io):
        teksti = """
Valitse pelataanko
(a) Ihmistä vastaan
(b) Tekoälyä vastaan
(c) Parannettua tekoälyä vastaan
Muilla valinnoilla lopetetaan"""
        io.kirjoita(teksti)

        return io.lue()


class Peli:
    def __init__(self, eka_io, toka_io, tuomari):
        self._eka_io = eka_io
        self._toka_io = toka_io
        self._tuomari = tuomari

    def aloita(self):
        KPS.luo_peli(self._eka_io, self._toka_io, self._tuomari).pelaa()


