import unittest
from repository.word_repository import word_repository


class TestWordTest(unittest.TestCase):
    def setUp(self):
        self.repository = word_repository

    def test_get_word_test_words(self):
        """get_word_test_words returns a tuple"""
        words = self.repository.get_word_test_words(1)
        self.assertIsInstance(words, tuple)
