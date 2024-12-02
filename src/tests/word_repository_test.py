import unittest
from unittest.mock import Mock
from repository.word_repository import WordRepository


class TestWordTest(unittest.TestCase):
    def setUp(self):
        self.repository = WordRepository(Mock())

    def test_get_word_test_words(self):
        """get_word_test_words returns a dictionary"""
        words = self.repository.get_word_test_words(1)
        self.assertIsInstance(words, list)
