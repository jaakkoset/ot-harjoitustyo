import unittest
from exercises.word_test import Exercise


class TestExercise(unittest.TestCase):
    def setUp(self):
        self.test = Exercise(1)

    def test_new_word(self):
        """new_word actually changes the word"""
        old_word = self.test.latin_word()
        self.test.change_to_next_word()
        new_word = self.test.latin_word()
        self.assertFalse(old_word == new_word)

    def test_latin_word(self):
        """latin_word returns a string"""
        latin_word = self.test.latin_word()
        self.assertIsInstance(latin_word, str)

    def test_answers(self):
        """Answers returns a list"""
        translation = self.test.answers()
        self.assertIsInstance(translation, list)

    def test_printable_answers(self):
        """printable_translations works correctly"""
        word_test = Exercise(1, exercise_repo=StubExerciseRepository())
        word_test.change_to_next_word()
        should_be = "  poika  lapsi"
        self.assertEqual(word_test.printable_answers(), should_be)


class StubExerciseRepository:
    def __init__(self):
        self.all_exercise_questions = [
            {"id": "-1", "exercise_id": "-1", "question": "puella", "answers": ("tyttö",)},
            {"id": "-2", "exercise_id": "-1", "question": "puer", "answers": ("poika", "lapsi")},
        ]
        self.exercise = None

    def get_exercise_data(self, word_id):
        return self.exercise, self.all_exercise_questions
