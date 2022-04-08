from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self, tuomari, tekoaly):
        super().__init__(tuomari)
        self._tekoaly = tekoaly
 
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        
        print(f"Tietokone valitsi: {tokan_siirto}")
              
        return tokan_siirto
    
    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
