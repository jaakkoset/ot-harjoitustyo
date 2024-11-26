"Class WordTest provides methods for word tests"
from word_repository import WordRepository
from database_connection import get_database_connection


class WordTest:
    """Methods for word tests"""

    def __init__(self, repository=WordRepository(get_database_connection())):
        self.db = repository
        self.word = {
            "id": -1,
            "word": None,
            "translations": None,
        }
        self.next_word()

    def next_word(self):
        """Fetch the next word and its translations from the database and save them"""
        next_id = int(self.word_id()) + 1
        self.word = self.db.get_word_and_translations(next_id)

    def word_id(self) -> str:
        """Return the id number of the word"""
        return self.word["id"]

    def latin_word(self) -> str:
        """Return the Latin word"""
        return self.word["word"]

    def translations(self) -> tuple:
        """Return the Finnish translations in a tuple"""
        return self.word["translations"]

    def printable_translations(self) -> str:
        """Return the translations in one string"""
        text = ""
        for t in self.word["translations"]:
            text += "  " + t
        return text

    def check_answer(self, answer) -> bool:
        """Check the answer given by the user"""
        if answer in self.word["translations"]:
            return True
        return False
