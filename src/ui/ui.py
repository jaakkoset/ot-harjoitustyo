from exercises.word_test import WordTest
from repository.stats_repository import stats_repository


COMMANDS = {
    "q": "q lopeta ohjelma",
    "1": "1 sanakoe",
    "2": "2 tunnista sanan taivutusmuoto",
    "3": "3 tunnista lauserakenne",
    "4": "4 näytä tilastot",
}


class Ui:
    """Program loop and its helper methods"""

    def __init__(self, io, stats_repo=stats_repository):
        self._io = io
        self.stats = stats_repo

    def program(self):
        """Program loop"""
        while True:
            self._print_commands()
            command = self._io.read("Anna komento: ")

            if command == "q":
                break

            if command == "1":
                self._word_test()

            if command == "4":
                self._stats()

    def _print_commands(self):
        """Print all commands for the user"""
        self._io.write("\nKomennot:")
        for command in COMMANDS.values():
            self._io.write("  " + command)

    def _word_test(self):
        """Ui for the word test."""
        word_test_id = 1
        test = WordTest(word_test_id)
        self._io.write("\nPoistu kirjoittamalla x")

        while True:
            latin_word = test.latin_word()
            self._io.write("\nSuomenna sana: " + latin_word)
            answer = self._io.read()
            if answer == "x":
                break
            answer_is_correct = test.check_answer(answer)
            if answer_is_correct:
                self._io.write("\nVastasit oikein")
                self._io.write("Oikeat vastaukset:")
                self._io.write(test.printable_translations())
                if not test.change_to_next_word():
                    self._io.write("\nKoe valmis")
                    break

            else:
                self._io.write("\nVastaus väärin")

    def _stats(self):
        """Show statistics about the user"""
        correct_answers = self.stats.get_total_correct_word_test_answers()
        self._io.write(f"\nOlet vastannut oikein {correct_answers} sanaan")
