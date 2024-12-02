import unittest
from exercises.word_test import WordTest


class TestWordTest(unittest.TestCase):
    def setUp(self):
        self.test = WordTest(1)

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

    def test_translations(self):
        """translations returns a tuple"""
        translation = self.test.translations()
        self.assertIsInstance(translation, tuple)

    def test_printable_translations(self):
        """printable_translations works correctly"""
        word_test = WordTest(1, word_repo=StubWordRepository())
        word_test.change_to_next_word()
        should_be = "  poika  lapsi"
        self.assertEqual(word_test.printable_translations(), should_be)


class StubWordRepository:
    def __init__(self):
        self.words = [
            {"id": "0", "latin": "puella", "translations": ("tyttö",)},
            {
                "id": "1",
                "latin": "puer",
                "translations": (
                    "poika",
                    "lapsi",
                ),
            },
            {"id": "2", "latin": "bellum", "translations": ("sota",)},
            {"id": "3", "latin": "rēx", "translations": ("kuningas",)},
        ]

    def get_word_test_words(self, word_id):
        return self.words
