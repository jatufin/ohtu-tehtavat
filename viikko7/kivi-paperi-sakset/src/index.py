from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from tuomari import Tuomari
from komennot import Komennot
from pelaajat import Pelaajatehdas


def main():
    eka = Pelaajatehdas.luo_ihminen()
    toka = Pelaajatehdas.luo_ihminen_ilman_tulostusta()

    tekoaly = Pelaajatehdas.luo_tekoaly(Tekoaly())
    parempi_tekoaly = Pelaajatehdas.luo_tekoaly(TekoalyParannettu(10))

    tuomari = Tuomari()
    komennot = Komennot(eka, toka, tekoaly, parempi_tekoaly, tuomari)

    while True:
        tuomari.nollaa()

        valinta = komennot.valikko(eka)

        if not komennot.suorita(valinta):
            break


if __name__ == "__main__":
    main()
