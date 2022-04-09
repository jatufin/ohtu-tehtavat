from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from tuomari import Tuomari
from komennot import Komennot
from kpsio import KonsoliIO, TekoalyIO

def main():
    eka_io = KonsoliIO()
    toka_io = KonsoliIO(null_output=True)
    tuomari = Tuomari()
    tekoaly_io = TekoalyIO(Tekoaly())
    parempi_tekoaly_io = TekoalyIO(TekoalyParannettu(10))
    komennot = Komennot(eka_io, toka_io, tekoaly_io, parempi_tekoaly_io, tuomari)

    while True:
        tuomari.nollaa()

        valinta = komennot.valikko(eka_io)

        if not komennot.suorita(valinta):
            break


if __name__ == "__main__":
    main()
