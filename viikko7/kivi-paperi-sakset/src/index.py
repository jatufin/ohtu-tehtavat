from kps import KPS
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from tuomari import Tuomari

from kpsio import KonsoliIO, TekoalyIO


class Komennot:
    def __init__(self, io, tuomari, tekoaly, parempi_tekoaly):
        self._komennot = {
            "a": Kaksinpeli(io, tuomari),
            "b": Yksinpeli(io, tuomari, tekoaly),
            "c": Yksinpeli(io, tuomari, parempi_tekoaly),
        }

        
class Kaksinpeli:
    def __init__(self, io, tuomari):
        self._io = io
        self._tuomari = tuomari

    def aloita(self):
        KPS.luo_kaksinpeli(self._io, self._tuomari).pelaa()


class Yksinpeli:
    def __init__(self, io, tuomari, tekoaly):
        self._io = io
        self._tuomari = tuomari
        self._tekoaly = Tekoaly

    def aloita(self):
        KPS.luo_kaksinpeli(self._io, self._tuomari).pelaa()


def main():
    eka_io = KonsoliIO()
    toka_io = KonsoliIO(null_output=True)
    tuomari = Tuomari()
    tekoaly_io = TekoalyIO(Tekoaly())
    parempi_tekoaly_io = TekoalyIO(TekoalyParannettu(10))

    while True:
        tuomari.nollaa()

        valinta = valikko(eka_io)

        if valinta == "a":
            aloita(KPS.luo_peli(eka_io, toka_io, tuomari), eka_io)

        elif valinta == "b":
            aloita(KPS.luo_peli(eka_io, tekoaly_io, tuomari), eka_io)

        elif valinta == "c":
            aloita(KPS.luo_peli(eka_io, parempi_tekoaly_io, tuomari), eka_io)

        else:
            break

        
def aloita(peli, io):
    io.kirjoita("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
    peli.pelaa()


def valikko(io):
    teksti = """
Valitse pelataanko
(a) Ihmistä vastaan
(b) Tekoälyä vastaan
(c) Parannettua tekoälyä vastaan
Muilla valinnoilla lopetetaan"""
    io.kirjoita(teksti)

    return io.lue()


if __name__ == "__main__":
    main()
