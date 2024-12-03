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

        self.exercise, self.questions = self.word_repo.get_word_test_words(word_test_id)
        self.number_of_words = len(self.questions)
        self.word_index = 0

    def word_id(self) -> str:
        """Return the id number of the word"""
        return self.questions[self.word_index]["id"]

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
        return self.questions[self.word_index]["question"]

    def translations(self) -> tuple:
        """Return the Finnish translations in a tuple"""
        return self.questions[self.word_index]["answers"]

    def printable_translations(self) -> str:
        """Return the translations in one string"""
        text = ""
        for t in self.questions[self.word_index]["answers"]:
            text += "  " + t
        return text

    def check_answer(self, answer) -> bool:
        """Check the answer given by the user"""
        if answer in self.questions[self.word_index]["answers"]:
            self.add_correct_word_test_answer_to_stats()
            return True
        return False

    def add_correct_word_test_answer_to_stats(self):
        self.stats_repo.add_correct_word_test_answer()
