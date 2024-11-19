"""class WordRepository provides methods for database queries involving words"""


class WordRepository:
    """Methods for database queries involving words"""

    def __init__(self):
        self.words = [
            ("puella", ("tyttö",)),
            ("colōnus", ("maanviljelijä",)),
            (
                "puer",
                (
                    "poika",
                    "lapsi",
                ),
            ),
        ]
        self.words2 = [
            ("puella", ("tyttö")),
            ("colōnus", ("maanviljelijä")),
            ("puer", ("poika", "lapsi")),
            ("bellum", ("sota")),
            ("rēx", ("kuningas")),
            ("lītus", ("ranta")),
            ("nāvis", ("laiva")),
            ("mare", ("meri")),
            ("bonus", ("hyvä")),
            ("pauper", ("köyhä")),
            ("omnis", ("jokainen")),
            ("parō", ("valmistaa", "valmistautua")),
            ("moneō", ("varoittaa")),
            ("regō", ("hallita")),
            ("audiō", ("kuulla")),
            ("capiō", ("ottaa")),
        ]

    def word_and_translations(self, ordinal: int) -> dict:
        """
        Return a Latin word and its Finnish translations in a tuple.

        Args:
            ordinal: the ordinal number of the Latin word in the database."""
        word = {"word": self.words[ordinal][0], "translations": self.words[ordinal][1]}
        return word

    def words_with_translations(self):
        """Return the number of latin words that have a translation in the database.
        Only words with translations are suitable for word tests."""
        return len(self.words)
