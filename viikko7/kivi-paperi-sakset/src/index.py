from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from tuomari import Tuomari
from komennot import Komennot
from kpsio import IOTehdas

def main():
    eka_io = IOTehdas.luo_ihmis_io()
    toka_io = IOTehdas.luo_ihmis_io_ilman_tulostusta()

    tekoaly_io = IOTehdas.luo_tekoaly_io(Tekoaly())
    parempi_tekoaly_io = IOTehdas.luo_tekoaly_io(TekoalyParannettu(10))

    tuomari = Tuomari()
    komennot = Komennot(eka_io, toka_io, tekoaly_io, parempi_tekoaly_io, tuomari)

    while True:
        tuomari.nollaa()

        valinta = komennot.valikko(eka_io)

        if not komennot.suorita(valinta):
            break


if __name__ == "__main__":
    main()
