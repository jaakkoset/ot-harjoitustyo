import unittest
from exercises.exercise import Exercise


class TestExercise(unittest.TestCase):
    def setUp(self):
        self.test = Exercise(1, StubExerciseRepository())

    def test_new_word(self):
        """change_to_next_word actually changes the word"""
        old_word = self.test.question()
        self.test.change_to_next_word()
        new_word = self.test.question()
        self.assertFalse(old_word == new_word)

    def test_question(self):
        """Method question returns the correct question"""
        question = self.test.question()
        should_be = "puella"
        self.assertEqual(should_be, question)

    def test_answers(self):
        """Method answers returns the answers"""
        answers = self.test.answers()
        should_be = ("tyttö",)
        self.assertEqual(should_be, answers)

    def test_printable_answers(self):
        """printable_translations works correctly"""
        self.test.change_to_next_word()
        next_word = self.test.printable_answers()
        should_be = "  poika  lapsi"
        self.assertEqual(should_be, next_word)


class StubExerciseRepository:
    def __init__(self):
        self.all_exercise_questions = [
            {
                "id": "-1",
                "exercise_id": "-1",
                "question": "puella",
                "answers": ("tyttö",),
            },
            {
                "id": "-2",
                "exercise_id": "-1",
                "question": "puer",
                "answers": ("poika", "lapsi"),
            },
        ]

    def get_exercise_questions(self, word_id):
        return self.all_exercise_questions
