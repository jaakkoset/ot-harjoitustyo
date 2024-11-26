from word_test import WordTest


COMMANDS = {
    "q": "q lopeta ohjelma",
    "1": "1 tee sanakoe",
}


class Program:
    """Program loop and its helper methods"""

    def __init__(self, io):
        self._io = io

    def program(self):
        """Program loop"""
        while True:
            self._print_commands()
            command = self._io.read("Anna komento: ")

            if command == "1":
                self._word_test()

            if command == "q":
                break

    def _print_commands(self):
        """Print all commands for the user"""
        self._io.write("\nKomennot:")
        for command in COMMANDS.values():
            self._io.write("  " + command)

    def _word_test(self):
        """Ui for the word test."""
        test = WordTest()
        self._io.write("\nPoistu kirjoittamalla x")

        while True:
            latin_word = test.latin_word()
            self._io.write("\nSuomenna sana: " + latin_word)
            answer = self._io.read()
            if answer == "x":
                break
            check = test.check_answer(answer)
            if check:
                self._io.write("\nVastasit oikein")
                self._io.write("Oikeat vastaukset:")
                self._io.write(test.printable_translations())
                test.next_word()
            else:
                self._io.write("\nVastaus väärin")
