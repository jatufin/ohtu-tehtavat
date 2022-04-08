from kps import KPS


from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from tuomari import Tuomari


def main():
    tuomari = Tuomari()
    tekoaly = Tekoaly()
    parempi_tekoaly = TekoalyParannettu(10)

    while True:
        tuomari.nollaa()

        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            aloita(KPS.luo_kaksinpeli(tuomari))

        elif vastaus.endswith("b"):
            aloita(KPS.luo_yksinpeli(tuomari, tekoaly))

        elif vastaus.endswith("c"):
            aloita(KPS.luo_yksinpeli(tuomari, parempi_tekoaly))

        else:
            break

def aloita(peli):
    print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
    peli.pelaa()


if __name__ == "__main__":
    main()
