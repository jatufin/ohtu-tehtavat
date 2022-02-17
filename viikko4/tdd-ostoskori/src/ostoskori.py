from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
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
        for ostos in self._ostokset:
            if(ostos.tuote == lisattava):
                ostos.muuta_lukumaaraa(1)
                return
            
        self._ostokset.append(Ostos(lisattava))
        # lisää tuotteen


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
