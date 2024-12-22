from repository.exercise_repository import exercise_repository


class ExercisesService:
    """Provides methods to get information of exercises from the database.

    Attributes:
        exercise_repo: the repository where exercises are saved.
    """

    def __init__(
        self,
        exercise_repo=exercise_repository,
    ):
        self.exercise_repo = exercise_repo

    def get_all_word_tests(self) -> list:
        """Return a list of all word tests. For each word test the list containes a
        dictionary that has id, name, guide and type of the word test."""
        return self.exercise_repo.get_all_exercises("word test")
