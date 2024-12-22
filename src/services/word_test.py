from repository.exercise_repository import exercise_repository
from repository.stats_repository import stats_repository
from entities.exercise import Exercise


class WordTestService:
    """Program logic for word tests.

    Attributes:
        exercise_repo: the repository where exercises are saved.
        stats_repo: the repository where stats are saved.
        exercise: an Exercise type object that as all questions and answers of an
        exercise.
        question_index: an integer count of the questions that have been answered.
    """

    def __init__(
        self,
        exercise_repo=exercise_repository,
        stats_repo=stats_repository,
    ):
        self.exercise_repo = exercise_repo
        self.stats_repo = stats_repo

        self.exercise = None
        self.question_index = 0

    def new_exercise(self, exercise_id) -> None:
        """Create a new exercise.

        Args:
            exercise_id: the id of the exercise in the database"""
        self.exercise = Exercise(exercise_id)

    def question(self):
        """Return the current question"""
        return self.exercise.question(self.question_index)

    def check_answer(self, answer) -> bool:
        """Check the answer given by the user. Return True when the answer is correct
        and False otherwise."""
        if answer in self.exercise.answers(self.question_index):
            return True
        return False

    def change_to_next_question(self) -> bool:
        """
        Change the current question. Return True if question is changed and False if
        there are no questions left."""
        self.question_index += 1
        no_questions_left = self.question_index >= self.exercise.number_of_questions()
        if no_questions_left:
            return False
        return True

    def printable_answers(self) -> str:
        """Return the answers of the current question in one string"""
        text = ""
        for answer in self.exercise.answers(self.question_index):
            text += "  " + answer
        return text

    def exercise_name(self) -> str:
        """Return the name of the current exercise"""
        return self.exercise.name()

    def get_all_word_tests(self) -> list:
        """Return a list of all word tests. For each word test the list containes a
        dictionary that has id, name, guide and type of the word test."""
        return self.exercise_repo.get_all_exercises("word test")

    def add_correct_word_test_answer_to_stats(self):
        self.stats_repo.add_correct_word_test_answer()

    def add_wrong_word_test_answer_to_stats(self):
        self.stats_repo.add_wrong_word_test_answer()

    def add_completed_word_test_to_stats(self):
        self.stats_repo.add_completed_word_test()
