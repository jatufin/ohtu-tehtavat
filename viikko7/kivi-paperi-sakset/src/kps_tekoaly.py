from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self, io, tuomari, tekoaly):
        super().__init__(io, tuomari)
        self._tekoaly = tekoaly
 
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        
        self._io.kirjoita(f"Tietokone valitsi: {tokan_siirto}")
              
        return tokan_siirto
    
    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
