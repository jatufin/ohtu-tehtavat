class KPS:
    def __init__(self, eka_io, toka_io, tuomari):
        self._eka_io = eka_io
        self._toka_io = toka_io
        self._tuomari = tuomari
        
    def pelaa(self):
        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            if self._tuntematon_siirto(ekan_siirto) or self._tuntematon_siirto(tokan_siirto):
                break
            
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self._eka_io.kirjoita(self._tuomari)

        self._eka_io.kirjoita("Kiitos!")
        self._eka_io.kirjoita(self._tuomari)
        
    def _ensimmaisen_siirto(self):
        return self._eka_io.lue("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmäisen_siirto):
        return "k"

    def _tuntematon_siirto(self, siirto):
        if len(siirto) != 1:
            return True
        
        return siirto not in "kps"

    @staticmethod
    def luo_kaksinpeli(eka_io, toka_io, tuomari):
        from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja        
        return KPSPelaajaVsPelaaja(eka_io, toka_io, tuomari)
        
    @staticmethod
    def luo_yksinpeli(io, tuomari, tekoaly):
        from kps_tekoaly import KPSTekoaly
        return KPSTekoaly(io, tuomari, tekoaly)
