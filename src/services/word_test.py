from repository.exercise_repository import exercise_repository
from repository.stats_repository import stats_repository


class WordTestService:
    """Progam logic for word tests.

    Attributes:
        exercise_repo: the repository where exercises are saved.
        stats_repo: the repository where stats are saved.
    """

    def __init__(
        self,
        exercise_repo=exercise_repository,
        stats_repo=stats_repository,
    ):
        self.exercise_repo = exercise_repo
        self.stats_repo = stats_repo

    def get_all_word_tests(self) -> list:
        """Return a list of all word tests. For each word test the list containes a
        dictionary that has id, name, guide and type of the word test."""
        return self.exercise_repo.get_all_exercises("word test")
