from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self):
        super().__init__()
        self._tekoaly = Tekoaly()
 
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        
        return tokan_siirto
    
    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
