import unittest
from unittest.mock import Mock
from word_repository import WordRepository


class TestWordTest(unittest.TestCase):
    def setUp(self):
        self.repository = WordRepository(Mock())

    def test_if_id_is_too_big_it_resets(self):
        too_large_id = self.repository.words_with_translations()
        self.assertNotEqual(too_large_id, 0)
        word = self.repository.get_word_and_translations(too_large_id)
        self.assertEqual(int(word["id"]), 0)
