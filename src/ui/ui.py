import sys
from exercises.exercise import Exercise
from repository.stats_repository import stats_repository


COMMANDS = {
    "q": "q lopeta ohjelma",
    "1": "1 sanakoe",
    "4": "4 näytä tilastot",
}


class Ui:
    def __init__(self, io, stats_repo=stats_repository):
        self.io = io
        self.stats = stats_repo

        self.command_handler = CommandHandler(io)

    def program(self):
        """The program loop"""
        while True:
            self._print_commands()
            command = self.io.read("Anna komento: ")
            self.command_handler.get(command).run()

    def _print_commands(self):
        """Print all commands for the user"""
        self.io.write("\nKomennot:")
        for command in COMMANDS.values():
            self.io.write("  " + command)


class CommandHandler:
    def __init__(self, io):
        self.io = io

        self.COMMANDS = {
            "q": Quit(self.io),
            "1": WordTest(self.io),
            "4": Stats(self.io),
        }

    def get(self, command):
        if command in self.COMMANDS:
            return self.COMMANDS[command]

        return InvalidCommand(self.io)


class WordTest:
    def __init__(self, io):
        self.io = io

    def run(self):
        word_test_id = 1
        test = Exercise(word_test_id)
        self.io.write("\nPoistu kirjoittamalla x")

        while True:
            latin_word = test.latin_word()
            self.io.write("\nSuomenna sana: " + latin_word)
            answer = self.io.read()
            if answer == "x":
                self.io.write("\nLopetit kokeen")
                break
            answer_is_correct = test.check_answer(answer)
            if answer_is_correct:
                self.io.write("\nVastasit oikein")
                self.io.write("Oikeat vastaukset:")
                self.io.write(test.printable_answers())
                if not test.change_to_next_word():
                    self.io.write("\nKoe valmis")
                    break

            else:
                self.io.write("\nVastaus väärin, yritä uudelleen.")


class Stats:
    def __init__(self, io):
        self.io = io
        self.stats = stats_repository

    def run(self):
        """Show statistics about the user"""
        correct_answers = self.stats.get_total_correct_word_test_answers()
        self.io.write(f"\nOlet vastannut oikein {correct_answers} sanaan")


class InvalidCommand:
    def __init__(self, io):
        self.io = io

    def run(self):
        self.io.write("\nVäärä komento")


class Quit:
    def __init__(self, io):
        self.io = io

    def run(self):
        self.io.write("\nNäkemiin")
        sys.exit(0)
