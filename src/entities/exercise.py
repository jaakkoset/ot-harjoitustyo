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

    def question(self, index: int) -> str:
        """Return a question

        Args:
            index: the index number of the question"""
        return self.__questions[index]["question"]

    def answers(self, index) -> tuple:
        """Return the answers of a question in a tuple

        Args:
            index: the index number of the question"""
        return self.__questions[index]["answers"]

    def number_of_questions(self):
        return self.__number_of_question

    def name(self):
        return self.__exercise_info["name"]
