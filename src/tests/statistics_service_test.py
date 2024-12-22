import unittest
from services.statistics import StatisticsService


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.statistics = StatisticsService(StubStatsRepository())

    def test_printable_statistics(self):
        """Method printable_statistics returns the statistics in the correct format"""
        should_be = "Sanakokeiden tilastot\n"
        should_be += "  Olet kääntänyt oikein 1 sanaa\n"
        should_be += "  Olet vastannut väärin 2 kertaa\n"
        should_be += "  Olet suorittanut 3 sanakoetta kokonaisuudessaan"
        acutally_is = self.statistics.printable_statistics()
        self.assertEqual(should_be, acutally_is)


class StubStatsRepository:
    def __init__(self):
        self.stats = {
            "correct_word_test_answers": 1,
            "wrong_word_test_answers": 2,
            "word_tests_completed": 3,
        }

    def get_all_stats(self):
        return self.stats
