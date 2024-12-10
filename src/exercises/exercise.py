from repository.exercise_repository import exercise_repository


class Exercise:
    """Methods for handling questions and checking answers.

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

        self.questions = self.exercise_repo.get_exercise_questions(exercise_id)
        self.number_of_question = len(self.questions)
        self.question_index = 0

    def change_to_next_word(self) -> bool:
        """Change the current word. Return True if word is changed and False if there
        are no words left."""
        self.question_index += 1
        no_questions_left = self.question_index >= self.number_of_question
        if no_questions_left:
            return False
        return True

    def question(self) -> str:
        """Return the current question"""
        return self.questions[self.question_index]["question"]

    def answers(self) -> tuple:
        """Return the answers in a tuple"""
        return self.questions[self.question_index]["answers"]

    def printable_answers(self) -> str:
        """Return the answers in one string"""
        text = ""
        for t in self.questions[self.question_index]["answers"]:
            text += "  " + t
        return text

    def check_answer(self, answer) -> bool:
        """Check the answer given by the user. Return True when the answer is correct
        and False otherwise."""
        if answer in self.questions[self.question_index]["answers"]:
            return True
        return False
