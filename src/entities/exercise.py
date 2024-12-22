from repository.exercise_repository import exercise_repository


class Exercise:
    """
    An Exercise object includes all the questions and answers of a given exercise and it
    also has methods for handling them and checking answers given by the user. 

    Attributes:
        exercise_id: id number of the exercise.
        exercise_repo: the repository where exercises are saved.
        questions: a list of all questions.
        number_of_question: the number of questions.
        question_index: an integer count of the questions that have been answered.
    """

    def __init__(
        self,
        exercise_id,
        exercise_repo=exercise_repository,
    ):
        self.exercise_id = exercise_id
        self.exercise_repo = exercise_repo

        self.__questions = self.exercise_repo.get_exercise_questions(exercise_id)
        self.__exercise_info = self.exercise_repo.get_exercise_info(exercise_id)
        self.__number_of_question = len(self.__questions)
        self.__question_index = 0

    def change_to_next_question(self) -> bool:
        """
        Change the current question. Return True if question is changed and False if
        there are no questions left."""
        self.__question_index += 1
        no_questions_left = self.__question_index >= self.__number_of_question
        if no_questions_left:
            return False
        return True

    def question(self) -> str:
        """Return the current question"""
        return self.__questions[self.__question_index]["question"]

    def answers(self) -> tuple:
        """Return the answers in a tuple"""
        return self.__questions[self.__question_index]["answers"]

    def printable_answers(self) -> str:
        """Return the answers in one string"""
        text = ""
        for t in self.__questions[self.__question_index]["answers"]:
            text += "  " + t
        return text

    def check_answer(self, answer) -> bool:
        """Check the answer given by the user. Return True when the answer is correct
        and False otherwise."""
        if answer in self.__questions[self.__question_index]["answers"]:
            return True
        return False
