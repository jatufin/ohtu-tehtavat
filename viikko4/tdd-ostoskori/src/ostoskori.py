from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def tavaroita_korissa(self):
        # Palauttaa tavaroiden kokonaismäärän
        yhteensa = 0

        for ostos in self._ostokset:
            yhteensa += ostos.lukumaara()

        return yhteensa

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        yhteishinta = 0

        for tuote in self._ostokset:
            yhteishinta += tuote.hinta()

        return yhteishinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        for ostos in self._ostokset:
            if(ostos.tuote == lisattava):
                ostos.muuta_lukumaaraa(1)
                return

        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa yhden kappaleen tuotetta ostoskorista
        for ostos in self._ostokset:
            if(ostos.tuote == poistettava):
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() < 1:
                    self._ostokset.remove(ostos)

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._ostokset = []

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse
        # JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostokset
