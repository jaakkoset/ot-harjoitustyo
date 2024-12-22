import unittest
from services.word_test import WordTestService
from repository.stats_repository import stats_repository


class TestStatsRepository(unittest.TestCase):
    """Tests to ensure statistics get added correctly. These tests are sensitive to the
    order in which they are executed."""

    def setUp(self):
        self.stats_repo = stats_repository
        self.test = WordTestService(stats_repo=self.stats_repo)
        self.test.new_exercise(1)

        self.stats_dictionary = {
            "correct_word_test_answers": 0,
            "wrong_word_test_answers": 0,
            "word_tests_completed": 0,
        }

    def test_a_all_zeroes_at_the_beginning(self):
        should_be = self.stats_dictionary
        stats = self.stats_repo.get_all_stats()
        self.assertEqual(should_be, stats)

    def test_b_wrong_answers_get_added(self):
        """Wrong answers get added to the stats"""
        self.test.check_answer("WRONG ANSWER")
        should_be = 1
        stats = self.stats_repo.get_all_stats()
        self.assertEqual(should_be, stats["wrong_word_test_answers"])

    def test_c_correct_answers_get_added(self):
        """Correct answers get added to the stats"""
        self.test.check_answer("tyttö")
        should_be = 1
        stats = self.stats_repo.get_all_stats()
        self.assertEqual(should_be, stats["correct_word_test_answers"])

    def test_d_completed_exercises_get_added(self):
        """When the user has answered all questions correctly, a completed wordtest is
        added to the statistcs"""
        self.test.check_answer("tyttö")
        self.test.change_to_next_question()
        self.test.check_answer("lapsi")
        self.test.change_to_next_question()
        self.test.check_answer("sota")
        self.test.change_to_next_question()
        self.test.check_answer("kuningas")
        should_be = 1
        stats = self.stats_repo.get_all_stats()
        self.assertEqual(should_be, stats["word_tests_completed"])
