KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(
            self,
            kapasiteetti: int = KAPASITEETTI,
            kasvatuskoko: int = OLETUSKASVATUS):
        if kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lukumaara = 0

    def kuuluu(self, n):
        return n in self.lukujono
    
    def lisaa(self, n):
        if self.alkioiden_lukumaara == 0:
            self.lukujono[0] = n
            self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1
            return True
        else:
            pass

        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lukumaara] = n
            self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1

            if self.alkioiden_lukumaara % len(self.lukujono) == 0:
                taulukko_old = self.lukujono
                self.kopioi_taulukko(self.lukujono, taulukko_old)
                self.lukujono = [0] * (self.alkioiden_lukumaara + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.lukujono)

            return True

        return False

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lukumaara):
            if n == self.lukujono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lukumaara - 1):
                apu = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = apu

            self.alkioiden_lukumaara = self.alkioiden_lukumaara - 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lukumaara

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x, a_taulu, b_taulu = IntJoukko.parametrit(a, b)                

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y, a_taulu, b_taulu = IntJoukko.parametrit(a, b)        

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z, a_taulu, b_taulu = IntJoukko.parametrit(a, b)
        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    @staticmethod
    def parametrit(a,b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        return x, a_taulu, b_taulu
    
    def __str__(self):
        if self.alkioiden_lukumaara == 0:
            return "{}"
        elif self.alkioiden_lukumaara == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lukumaara - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lukumaara - 1])
            tuotos = tuotos + "}"
            return tuotos
