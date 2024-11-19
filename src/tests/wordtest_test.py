import unittest
from word_test import WordTest


class TestWordTest(unittest.TestCase):
    def setUp(self):
        self.test = WordTest()

    def test_new_word(self):
        """new_word actually changes the word"""
        old_word = self.test.latin_word()
        self.test.new_word()
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
