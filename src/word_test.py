"Class WordTest provides methods for word tests"

from word_repository import WordRepository


class WordTest:
    """Methods for the word test"""

    def __init__(self):
        self.db = WordRepository()
        self.counter = 0
        self.new_word()

    def new_word(self):
        """Fetch the next word and its translations from the database and save them"""
        self.word = self.db.word_and_translations(self.counter)

        if self.counter < self.db.words_with_translations() - 1:
            self.counter += 1
        else:
            self.counter = 0

    def latin_word(self) -> str:
        """Return the Latin word"""
        return self.word["word"]

    def translations(self) -> tuple:
        """Return the translations in a tuple"""
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
