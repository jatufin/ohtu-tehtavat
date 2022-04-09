# Instead of creating different KPS main game classes based on
# different type of players, the separation between human and UI
# players is done in an upper level: The game itself should not
# be deeply aware if one (or indeed all) of the players are computers
# or not.
#
class Pelaajatehdas:
    @staticmethod
    def luo_ihmispelaaja():
        return Ihminen()

    @staticmethod
    def luo_ihmispelaaja_ilman_tulostusta():
        return Ihminen(null_output=True)

    @staticmethod
    def luo_konepelaaja(tekoaly):
        return Tekoaly(tekoaly)


class Pelaaja:
    def __init__(self, tyyppi="tuntematon"):
        self._tyyppi = tyyppi

    @property
    def tyyppi(self):
        return self._tyyppi


class Ihminen(Pelaaja):
    # Possibility to suppress the output is to avoid duplicate
    # printouts in the (usual) case both human players are on
    # the same console
    def __init__(self, null_output=False):
        super().__init__(tyyppi="ihminen")
        self._null_output = null_output

    def lue(self, teksti=""):
        return input(teksti)

    def kirjoita(self, teksti):
        if not self._null_output:
            print(teksti)


class Tekoaly(Pelaaja):
    def __init__(self, tekoaly):
        super().__init__(tyyppi="tietokone")
        self._tekoaly = tekoaly

    def lue(self, teksti=""):
        return self._tekoaly.anna_siirto()

    def kirjoita(self, teksti):
        if self._on_siirto(teksti):
            self._tekoaly.aseta_siirto(teksti)

    def _on_siirto(self, siirto):
        return len(siirto) == 1 and siirto in "kps"
