"Class WordTest provides methods for word tests"
from repository.word_repository import word_repository
from repository.stats_repository import stats_repository


class WordTest:
    """Methods for word tests"""

    def __init__(
        self,
        word_test_id,
        word_repo=word_repository,
        stats_repo=stats_repository,
    ):
        self.word_test_id = word_test_id
        self.word_repo = word_repo
        self.stats_repo = stats_repo

        self.words = self.word_repo.get_word_test_words(word_test_id)
        self.number_of_words = len(self.words)
        self.word_index = 0

    def word_id(self) -> str:
        """Return the id number of the word"""
        return self.words[self.word_index]["id"]

    def change_to_next_word(self) -> bool:
        """Change the current word. Return True if word is changed and False if there
        are no words left."""
        self.word_index += 1
        no_words_left = self.word_index >= self.number_of_words
        if no_words_left:
            return False
        return True

    def latin_word(self) -> str:
        """Return the Latin word"""
        return self.words[self.word_index]["latin"]

    def translations(self) -> tuple:
        """Return the Finnish translations in a tuple"""
        return self.words[self.word_index]["translations"]

    def printable_translations(self) -> str:
        """Return the translations in one string"""
        text = ""
        for t in self.words[self.word_index]["translations"]:
            text += "  " + t
        return text

    def check_answer(self, answer) -> bool:
        """Check the answer given by the user"""
        if answer in self.words[self.word_index]["translations"]:
            self.add_correct_word_test_answer_to_stats()
            return True
        return False

    def add_correct_word_test_answer_to_stats(self):
        self.stats_repo.add_correct_word_test_answer()
