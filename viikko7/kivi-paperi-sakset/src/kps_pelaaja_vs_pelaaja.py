from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def __init__(self, io, tuomari):
        super().__init__(io, tuomari)
        
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto
 
