import unittest
from services.word_test import WordTestService


class TestWordTestService(unittest.TestCase):
    def setUp(self):
        self.exercise_repository = StubExerciseRepository()
        self.test = WordTestService(self.exercise_repository, StubStatsRepository())
        self.test.new_exercise(1, self.exercise_repository)

    def test_question(self):
        """Method question returns the correct question"""
        question = self.test.question()
        should_be = "puella"
        self.assertEqual(should_be, question)

    def test_check_answer(self):
        """Method check_answer returns True when the answer is true and False otherwise"""
        wrong_answer = self.test.check_answer("tyllerö")
        self.assertFalse(wrong_answer)
        correct_answer = self.test.check_answer("tyttö")
        self.assertTrue(correct_answer)

    def test_change_to_next_question(self):
        """Method change_to_next_word actually changes the word"""
        self.test.change_to_next_question()
        new_word = self.test.question()
        self.assertTrue(new_word, "puer")

    def test_change_to_next_question_returns_false(self):
        """Method change_to_next_question returns False after all questions have been
        iterated"""
        self.assertTrue(self.test.change_to_next_question())
        self.assertTrue(self.test.change_to_next_question())
        self.assertFalse(self.test.change_to_next_question())

    def test_printable_answers(self):
        """printable_translations works correctly"""
        self.test.change_to_next_question()
        actually_is = self.test.printable_answers()
        should_be = "Hyväksytyt vastaukset ovat:\n   poika   lapsi"
        self.assertEqual(should_be, actually_is)

    def test_exercise_name(self):
        """exercise_name returns the correct name"""
        name = self.test.exercise_name()
        self.assertEqual(name, "Helppo sanakoe")

    def test_number_of_questions(self):
        number = self.test.exercise.number_of_questions()
        self.assertEqual(3, number)

    def test_is_word_test_completed_returns_false(self):
        """Method _is_word_test_completed returns False if all questions have not been
        answered correctly"""
        self.assertFalse(self.test._is_word_test_completed())
        self.test.check_answer("tyttö")
        self.assertFalse(self.test._is_word_test_completed())
        self.test.change_to_next_question()
        self.test.check_answer("lapsi")
        self.test.change_to_next_question()
        self.test.check_answer("WRONG ANSWER")
        self.assertFalse(self.test._is_word_test_completed())

    def test_is_word_test_completed_returns_true(self):
        """Method _is_word_test_completed returns True if all questions have been
        answered correctly"""
        self.test.check_answer("tyttö")
        self.test.change_to_next_question()
        self.test.check_answer("poika")
        self.test.change_to_next_question()
        self.test.check_answer("sota")
        self.assertTrue(self.test._is_word_test_completed())


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
            {"question": "bellum", "answers": ("sota",)},
        ]
        self.exercise_info = {
            "name": "Helppo sanakoe",
            "guide": "Suomenna annetut sanat",
            "type": "word test",
        }

    def get_exercise_questions(self, exercise_id):
        return self.all_exercise_questions

    def get_exercise_info(self, exercise_id):
        return self.exercise_info

    def add_correct_word_test_answer_to_stats(self):
        pass

    def add_wrong_word_test_answer_to_stats(self):
        pass

    def add_completed_word_test_to_stats(self):
        pass


class StubStatsRepository:
    def __init__(self):
        pass

    def add_correct_word_test_answer(self):
        pass

    def add_wrong_word_test_answer(self):
        pass

    def add_completed_word_test(self):
        pass
