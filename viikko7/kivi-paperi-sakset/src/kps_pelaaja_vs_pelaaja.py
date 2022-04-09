from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def __init__(self, eka_io, toka_io, tuomari):
        super().__init__(eka_io, toka_io, tuomari)
        
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._toka_io.lue("Toisen pelaajan siirto: ")

        return tokan_siirto
 
