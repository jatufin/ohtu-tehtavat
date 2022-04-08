class KPS:
    def __init__(self, tuomari):
        self._tuomari = tuomari
        
    def pelaa(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self._tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(self._tuomari)
        
    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmäisen_siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    @staticmethod
    def luo_kaksinpeli(tuomari):
        from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja        
        return KPSPelaajaVsPelaaja(tuomari)
        
    @staticmethod
    def luo_yksinpeli(tuomari, tekoaly):
        from kps_tekoaly import KPSTekoaly
        return KPSTekoaly(tuomari, tekoaly)
