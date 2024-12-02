"""
Class StatsRepository provides methods for database queries involving statistics about
the user
"""

from database_connection import get_database_connection


class StatsRepository:
    def __init__(self, connection):
        self._connection = connection
        self._stats = {"correct word test answers": 0}

    def add_correct_word_test_answer(self):
        self._stats["correct word test answers"] += 1

    def get_total_correct_word_test_answers(self):
        return self._stats["correct word test answers"]


stats_repository = StatsRepository(get_database_connection)
