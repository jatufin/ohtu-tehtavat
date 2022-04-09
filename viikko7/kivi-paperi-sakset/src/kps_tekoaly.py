from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self, io, tekoaly_io, tuomari):
        super().__init__(io, tekoaly_io, tuomari)
 
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._toka_io.lue()
        self._toka_io.kirjoita(ensimmaisen_siirto)
        
        self._eka_io.kirjoita(f"Tietokone valitsi: {tokan_siirto}")
              
        return tokan_siirto
