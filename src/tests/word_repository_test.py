import unittest
from repository.word_repository import exercise_repository


class TestExerciseRepository(unittest.TestCase):
    def setUp(self):
        self.repository = exercise_repository

    def test_get_get_exercise_data(self):
        """get_word_test_words returns a tuple"""
        words = self.repository.get_exercise_data(1)
        self.assertIsInstance(words, tuple)
