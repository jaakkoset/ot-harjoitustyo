import unittest
from services.word_test import WordTestService
from repository.stats_repository import stats_repository


class TestStatsRepository(unittest.TestCase):
    """Tests to ensure statistics get added correctly"""

    def setUp(self):
        self.stats_repo = stats_repository
        self.test = WordTestService(stats_repo=self.stats_repo)
        self.test.new_exercise(1)

    def test_wrong_answers_get_added(self):
        """Wrong answers are added to statistics"""
        should_be = {
            "correct_word_test_answers": 0,
            "wrong_word_test_answers": 0,
            "word_tests_completed": 0,
        }
        stats = self.stats_repo.get_all_stats()
        self.assertEqual(should_be, stats)
