"Class WordTest provides methods for word tests"
from word_repository import word_repository
from stats_repository import stats_repository


class WordTest:
    """Methods for word tests"""

    def __init__(
        self,
        word_repo=word_repository,
        stats_repo=stats_repository,
    ):
        self.word_repo = word_repo
        self.stats_repo = stats_repo
        self.word = {
            "id": -1,
            "word": None,
            "translations": None,
        }
        self.next_word()

    def next_word(self):
        """Fetch the next word and its translations from the database and save them"""
        next_id = int(self.word_id()) + 1
        self.word = self.word_repo.get_word_and_translations(next_id)

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
            self.add_correct_word_test_answer_to_stats()
            return True
        return False

    def add_correct_word_test_answer_to_stats(self):
        self.stats_repo.add_correct_word_test_answer()
