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
        if self.kuuluu(n):
            return False
        
        self.lukujono[self.alkioiden_lukumaara] = n
        self.alkioiden_lukumaara += 1
        
        if self.alkioiden_lukumaara == len(self.lukujono):
            self.lukujono += [0] * self.kasvatuskoko

        return True


    def poista(self, n):
        if not self.kuuluu(n):
            return False

        self.lukujono.remove(n)
        self.lukujono.append(0)
        self.alkioiden_lukumaara -= 1

        return True

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lukumaara]
    
    @staticmethod
    def yhdiste(a, b):
        uusi_joukko, a_taulu, b_taulu = IntJoukko.parametrit(a, b)

        for n in (a_taulu + b_taulu):
            uusi_joukko.lisaa(n)

        return uusi_joukko

    @staticmethod
    def leikkaus(a, b):
        uusi_joukko, a_taulu, b_taulu = IntJoukko.parametrit(a, b)        

        for n in a_taulu:
            if n in b_taulu:
                uusi_joukko.lisaa(n)

        return uusi_joukko

    @staticmethod
    def erotus(a, b):
        uusi_joukko, a_taulu, b_taulu = IntJoukko.parametrit(a, b)

        for n in a_taulu:
            if n not in b_taulu:
                uusi_joukko.lisaa(n)

        return uusi_joukko

    @staticmethod
    def parametrit(a, b):
        uusi_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        return uusi_joukko, a_taulu, b_taulu
    
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
