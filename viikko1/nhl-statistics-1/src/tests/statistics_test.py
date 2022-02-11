import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_haku_loytaa_oikean_pelaajan(self):
        self.assertIsNotNone(self.statistics.search("Semenko"))

    def test_haku_ei_loyda_vaaraa_pelaajaa(self):
        self.assertIsNone(self.statistics.search("XSemenko"))

    def test_joukkue_palauttaa_oikean_maaran(self):
        team = self.statistics.team("EDM")

        self.assertEqual(len(team), 3)

    def test_parhaat_palauttaa_oikean_maaran(self):
        top_three = self.statistics.top_scorers(3)

        self.assertEqual(len(top_three), 3)

    def test_parhaat_loytaa_parhaan(self):
        top_three = self.statistics.top_scorers(3)

        self.assertEqual(top_three[0].name, "Gretzky")
