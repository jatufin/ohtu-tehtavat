from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def __init__(self, tuomari):
        super().__init__(tuomari)
        
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto
    
    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
