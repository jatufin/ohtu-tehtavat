from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from tuomari import Tuomari
from komennot import Komennot
from pelaajat import Pelaajatehdas


def main():
    eka = Pelaajatehdas.luo_ihmispelaaja()
    toka = Pelaajatehdas.luo_ihmispelaaja_ilman_tulostusta()

    tekoaly = Pelaajatehdas.luo_konepelaaja(Tekoaly())
    parempi_tekoaly = Pelaajatehdas.luo_konepelaaja(TekoalyParannettu(10))

    tuomari = Tuomari()
    komennot = Komennot(eka, toka, tekoaly, parempi_tekoaly, tuomari)

    while True:
        tuomari.nollaa()

        valinta = komennot.valikko(eka)

        if not komennot.suorita(valinta):
            break


if __name__ == "__main__":
    main()
