import unittest
from repository.exercise_repository import exercise_repository


class TestExerciseRepository(unittest.TestCase):
    def setUp(self):
        self.repository = exercise_repository

    def test_get_exercise_questions(self):
        """get_exercise_questions returns a list"""
        words = self.repository.get_exercise_questions(1)
        self.assertIsInstance(words, list)
