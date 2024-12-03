"""Class WordRepository provides methods for database queries involving words"""

from database_connection import get_database_connection


class WordRepository:
    """Methods for database queries involving words"""

    def __init__(self, connection):
        self._connection = connection

    def get_word_test_words(self, word_test_id: str) -> tuple[dict, list[dict]]:
        """
        Return the exercise info, questions and correct answers.

        Args:
            word_test_id: the id number of the word test in the database.

        Returns:
            tuple: (exercise, all_exercise_questions) where exercise is a dictionary
            {"id": (str), "name": (str), "guide": (str)}
            and all_exercise_questions is a list containing dictionaries in the form of
            {"id": (str), "exercise_id": (str), "question": (str), "answers": (tuple)}
        """
        word_test_id = int(word_test_id)
        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT id, name, guide 
            FROM Exercises
            WHERE id=?;
        """,
            (word_test_id,),
        )
        exercise = cursor.fetchone()
        exercise = {"id": exercise[0], "name": exercise[1], "guide": exercise[2]}

        cursor.execute(
            """
            SELECT id, exercise_id, question 
            FROM Questions
            WHERE exercise_id=?;
        """,
            (exercise["id"],),
        )
        questions = cursor.fetchall()

        all_exercise_questions = []
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
            all_exercise_questions.append(question)

        return exercise, all_exercise_questions


word_repository = WordRepository(get_database_connection())
