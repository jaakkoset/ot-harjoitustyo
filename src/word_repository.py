"""Class WordRepository provides methods for database queries involving words"""


class WordRepository:
    """Methods for database queries involving words"""

    def __init__(self, connection):
        self._connection = connection

        self.words = [
            ("0", "puella", ("tyttö",)),
            ("1", "colōnus", ("maanviljelijä",)),
            (
                "2",
                "puer",
                (
                    "poika",
                    "lapsi",
                ),
            ),
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

    def get_word_and_translations(self, word_id: str) -> dict:
        """
        Return a Latin word and its Finnish translations in a tuple.

        Args:
            word_id: the id number of the Latin word in the database.
        """
        word_id = int(word_id)
        if word_id >= self.words_with_translations():
            word_id = 0

        word = {
            "id": self.words[word_id][0],
            "word": self.words[word_id][1],
            "translations": self.words[word_id][2],
        }
        return word

    def words_with_translations(self):
        """Return the number of latin words that have a translation in the database.
        Only words with translations are suitable for word tests."""
        return len(self.words)
