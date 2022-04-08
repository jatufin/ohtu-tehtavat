from kps import KPS
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from tuomari import Tuomari

from kpsio import KonsoliIO

        
def main():
    io = KonsoliIO()
    tuomari = Tuomari()
    tekoaly = Tekoaly()
    parempi_tekoaly = TekoalyParannettu(10)

    while True:
        tuomari.nollaa()

        valinta = valikko(io)

        if valinta == "a":
            aloita(KPS.luo_kaksinpeli(io, tuomari), io)

        elif valinta == "b":
            aloita(KPS.luo_yksinpeli(io, tuomari, tekoaly), io)

        elif valinta == "c":
            aloita(KPS.luo_yksinpeli(io, tuomari, parempi_tekoaly), io)

        else:
            break

        
def aloita(peli, io):
    io.kirjoita("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
    peli.pelaa()


def valikko(io):
    io.kirjoita("Valitse pelataanko",
                "(a) Ihmistä vastaan",
                "(b) Tekoälyä vastaan",
                "(c) Parannettua tekoälyä vastaan",
                "Muilla valinnoilla lopetetaan")

    return io.lue()


if __name__ == "__main__":
    main()
