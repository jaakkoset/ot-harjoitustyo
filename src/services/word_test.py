from repository.exercise_repository import exercise_repository
from repository.stats_repository import stats_repository
from entities.exercise import Exercise


class WordTestService:
    """Program logic for word tests.

    Attributes:
        exercise_repo: the repository where exercises are saved.
        stats_repo: the repository where statistics are saved.
        exercise: an Exercise type object that as all questions and answers of an
        exercise.
        question_index: an integer count of the questions that have been answered.
        correct_answers: an integer count of the correct answers given by the user.
        wordtest_completion_added_to_stats: True if user has answered all questions
        correctly and this has been updated to statistcs, and False otherwise.
    """

    def __init__(
        self,
        exercise_id,
        exercise_repo=exercise_repository,
        stats_repo=stats_repository,
    ):
        self.exercise_repo = exercise_repo
        self.stats_repo = stats_repo

        self.exercise = Exercise(exercise_id, exercise_repo)
        self.question_index = 0
        self.correct_answers = 0
        self.__wordtest_completion_added_to_stats = False

    def question(self):
        """Return the current question"""
        return self.exercise.question(self.question_index)

    def check_answer(self, answer) -> bool:
        """Check the answer given by the user and add this information to statistics.
        Return True when the answer is correct and False otherwise."""
        answer_is_correct = answer in self.exercise.answers(self.question_index)
        if answer_is_correct:
            self.correct_answers += 1
            self.word_test_completed()
            self.__add_correct_word_test_answer_to_stats()
            return True
        self.__add_wrong_word_test_answer_to_stats()
        return False

    def word_test_completed(self):
        """If all questions have been answered correctly, add one completed wordtest to
        statistics."""
        if not self.__wordtest_completion_added_to_stats:
            if self._is_word_test_completed():
                self.__wordtest_completion_added_to_stats = True
                self.__add_completed_word_test_to_stats()

    def _is_word_test_completed(self) -> bool:
        """Check whether the user has answered all questions correctly. If so, return
        True and False otherwise"""
        all_questions_have_been_answered_correctly = (
            self.correct_answers >= self.exercise.number_of_questions()
        )
        if all_questions_have_been_answered_correctly:
            return True
        return False

    def change_to_next_question(self) -> bool:
        """
        Change the current question. Return True if question is changed and False if
        there are no questions left."""
        no_questions_left = (
            self.question_index + 1 >= self.exercise.number_of_questions()
        )
        if no_questions_left:
            return False
        self.question_index += 1
        return True

    def printable_answers(self) -> str:
        """Return the answers of the current question in one string"""
        text = "Hyväksytyt vastaukset ovat:\n"
        for answer in self.exercise.answers(self.question_index):
            text += "   " + answer
        return text

    def exercise_name(self) -> str:
        """Return the name of the current exercise"""
        return self.exercise.name()

    def __add_correct_word_test_answer_to_stats(self):
        self.stats_repo.add_correct_word_test_answer()

    def __add_wrong_word_test_answer_to_stats(self):
        self.stats_repo.add_wrong_word_test_answer()

    def __add_completed_word_test_to_stats(self):
        self.stats_repo.add_completed_word_test()
