import unittest
from repository.exercise_repository import exercise_repository


class TestExerciseRepository(unittest.TestCase):
    def setUp(self):
        self.repository = exercise_repository

    def test_get_exercise_questions(self):
        """get_exercise_questions returns a list"""
        words = self.repository.get_exercise_questions(1)
        self.assertIsInstance(words, list)

    def test_get_exercise_info(self):
        """Method get_exercise_info returns the correct info in a diciotnary"""
        exercise = self.repository.get_exercise_info(1)
        should_be = "Helppo sanakoe"
        self.assertEqual(should_be, exercise["name"])
        should_be = "Suomenna annetut sanat"
        self.assertEqual(should_be, exercise["guide"])
