"""Class WordRepository provides methods for database queries involving words"""

from database_connection import get_database_connection


class WordRepository:
    """Methods for database queries involving words"""

    def __init__(self, connection):
        self._connection = connection

        self.words = [
            {"id": "0", "latin": "puella", "translations": ("tyttö",)},
            {
                "id": "1",
                "latin": "puer",
                "translations": (
                    "poika",
                    "lapsi",
                ),
            },
            {"id": "2", "latin": "bellum", "translations": ("sota",)},
            {"id": "3", "latin": "rēx", "translations": ("kuningas",)},
        ]

        # self.words2 = [
        #     ("puella", ("tyttö")),
        #     ("colōnus", ("maanviljelijä")),
        #     ("puer", ("poika", "lapsi")),
        #     ("bellum", ("sota")),
        #     ("rēx", ("kuningas")),
        #     ("lītus", ("ranta")),
        #     ("nāvis", ("laiva")),
        #     ("mare", ("meri")),
        #     ("bonus", ("hyvä")),
        #     ("pauper", ("köyhä")),
        #     ("omnis", ("jokainen")),
        #     ("parō", ("valmistaa", "valmistautua")),
        #     ("moneō", ("varoittaa")),
        #     ("regō", ("hallita")),
        #     ("audiō", ("kuulla")),
        #     ("capiō", ("ottaa")),
        # ]

    def get_word_test_words(self, word_test_id: str) -> list[dict]:
        """
        Return the Latin words and their Finnish translations in dictionaries in a list.

        Args:
            word_test_id: the id number of the word test in the database.
        """
        word_test_id = int(word_test_id)

        return self.words

    def words_with_translations(self):
        """Return the number of latin words that have a translation in the database.
        Only words with translations are suitable for word tests."""
        return len(self.words)


word_repository = WordRepository(get_database_connection)
