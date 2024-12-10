"""
Class StatsRepository provides methods for database queries involving statistics about
the user
"""

from database_connection import get_database_connection


class StatsRepository:
    """Methods for adding and querying statics from the database"""

    def __init__(self, connection):
        self._connection = connection
        # self.stats = {"correct word test answers": 0}

    def add_correct_word_test_answer(self):
        cursor = self._connection.cursor()

        cursor.execute(
            """
                        UPDATE Stats 
                        SET 
                            correct_word_test_answers = 
                            correct_word_test_answers + 1 
                        WHERE id=1"""
        )
        self._connection.commit()
        # self.stats["correct word test answers"] += 1

    def get_all_stats(self) -> dict:
        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT 
                correct_word_test_answers,
                wrong_word_test_answers,
                word_tests_completed

            FROM Stats
            WHERE id=1;
        """
        )
        stats = cursor.fetchone()
        stats = dict(stats)
        return stats
        # return self.stats["correct word test answers"]


stats_repository = StatsRepository(get_database_connection())
