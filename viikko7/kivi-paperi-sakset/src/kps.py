class KPS:
    def __init__(self, eka, toka, tuomari):
        self._eka = eka
        self._toka = toka
        self._tuomari = tuomari

    def pelaa(self):
        self._eka.kirjoita("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            if (self._tuntematon_siirto(ekan_siirto) or
                self._tuntematon_siirto(tokan_siirto)):
                break

            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self._eka.kirjoita(self._tuomari)

        self._eka.kirjoita("Kiitos!")
        self._eka.kirjoita(self._tuomari)

    def _ensimmaisen_siirto(self):
        return self._eka.lue("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._toka.lue("Toisen pelaajan siirto: ")
        self._toka.kirjoita(ensimmaisen_siirto)

        if self._toka.tyyppi == "tietokone":
            self._eka.kirjoita(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto

    def _tuntematon_siirto(self, siirto):
        if len(siirto) != 1:
            return True

        return siirto not in "kps"

    @staticmethod
    def luo_peli(eka, toka, tuomari):
        return KPS(eka, toka, tuomari)
