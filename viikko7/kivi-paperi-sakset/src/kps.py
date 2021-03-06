class KPS:
    def __init__(self, eka_pelaaja, toka_pelaaja, tuomari):
        self._eka_pelaaja = eka_pelaaja
        self._toka_pelaaja = toka_pelaaja
        self._tuomari = tuomari

    def pelaa(self):
        self._eka_pelaaja.kirjoita("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            if (self._tuntematon_siirto(ekan_siirto) or
                self._tuntematon_siirto(tokan_siirto)):
                break

            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self._eka_pelaaja.kirjoita(self._tuomari)

        self._eka_pelaaja.kirjoita("Kiitos!")
        self._eka_pelaaja.kirjoita(self._tuomari)

    def _ensimmaisen_siirto(self):
        return self._eka_pelaaja.lue("Ensimmäisen pelaajan siirto: ")

    # _toisen_siirto() was originally only a template
    # method to be implemented in inherited classes. But
    # as child classes turned out to be redundant and were
    # abandoned altogether, the method is fully implemented
    # in the sole KPS class.
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._toka_pelaaja.lue("Toisen pelaajan siirto: ")
        self._toka_pelaaja.kirjoita(ensimmaisen_siirto)

        # This is the only place where the KPS object changes
        # behaviour in the case the other player is not human
        if self._toka_pelaaja.tyyppi == "tietokone":
            self._eka_pelaaja.kirjoita(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto

    def _tuntematon_siirto(self, siirto):
        if len(siirto) != 1:
            return True

        return siirto not in "kps"

    # Originally we had two separate methods for creating
    # objects of the inherited classes.
    @staticmethod
    def luo_peli(eka_pelaaja, toka_pelaaja, tuomari):
        return KPS(eka_pelaaja, toka_pelaaja, tuomari)
