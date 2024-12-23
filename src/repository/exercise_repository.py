"""Class ExerciseRepository provides methods for database queries involving exercises"""

from database_connection import get_database_connection


class ExerciseRepository:
    """Methods for database queries involving exercises.

    Attributes:
        connection: connection for the database.
    """

    def __init__(self, connection):
        self._connection = connection

    def get_exercise_questions(self, exercise_id: str) -> list:
        """Return a list of all questions and answers of the question.

        Args:
            exercise_id: the id number of the exercise.

        Returns:
            A list containing dictionaries in the form of
            {"id": (str), "exercise_id": (str), "question": (str), "answers": (tuple)}.
        """
        exercise_id = int(exercise_id)
        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT id, exercise_id, question 
            FROM Questions
            WHERE exercise_id=?;
        """,
            (exercise_id,),
        )
        questions = cursor.fetchall()

        exercise_questions = []
        for row in questions:
            question = {}
            question["id"] = row["id"]
            question["exercise_id"] = row["exercise_id"]
            question["question"] = row["question"]

            cursor.execute(
                """
                SELECT id, question_id, answer 
                FROM Answers
                WHERE question_id=?;
            """,
                (question["id"],),
            )

            answer_list = [answer["answer"] for answer in cursor]

            question["answers"] = answer_list
            exercise_questions.append(question)

        return exercise_questions

    def get_exercise_info(self, exercise_id: str) -> dict:
        """Get the general information of the exercise.

        Args:
            exercise_id: the id number of the exercise.

        Returns:
            A dictionary contaning the id, name and guide of the exercise.
        """
        exercise_id = int(exercise_id)
        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT id, name, guide 
            FROM Exercises
            WHERE id=?;
        """,
            (exercise_id,),
        )
        exercise = cursor.fetchone()
        exercise = {"id": exercise[0], "name": exercise[1], "guide": exercise[2]}

        return exercise

    def get_all_exercises(self, exercise_type: str) -> list:
        """Return list of all exercises of the give type

        Args:
            exercise_type: e.g. word test"""
        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT id, name, guide, type 
            FROM Exercises
            WHERE type=?;
        """,
            (exercise_type,),
        )

        word_tests = []
        for row in cursor:
            test = {}
            test["id"] = row["id"]
            test["name"] = row["name"]
            test["guide"] = row["guide"]
            test["type"] = row["type"]

            word_tests.append(test)

        return word_tests


exercise_repository = ExerciseRepository(get_database_connection())
