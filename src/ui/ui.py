import sys
from exercises.exercise import Exercise
from repository.stats_repository import stats_repository
from services.word_test import WordTestService


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
        """The loop for the main menu"""
        while True:
            self._print_commands()
            command = self.io.read("Anna komento: ")
            self.command_handler.get(command).run()

    def _print_commands(self):
        """Print all commands for the user in the main menu"""
        self.io.write("\nKomennot:")
        for command in COMMANDS.values():
            self.io.write("  " + command)


class CommandHandler:
    def __init__(self, io):
        self.io = io

        self.commands = {
            "q": Quit(self.io),
            "1": WordTest(self.io),
            "4": Stats(self.io),
        }

    def get(self, command):
        if command in self.commands:
            return self.commands[command]

        return InvalidCommand(self.io)


class WordTest:
    """Contains the program loop of word tests"""

    def __init__(self, io):
        self.io = io

    def run(self):
        word_test_id = self.choose_word_test()
        test = Exercise(word_test_id)
        self.io.write(
            "\nVoit poistua kokeesta missä vaiheessa tahansa kirjoittamalla x"
        )

        while True:
            question = test.question()
            self.io.write("\nSuomenna sana: " + question)
            answer = self.io.read()
            if answer == "x":
                self.io.write("\nLopetit kokeen")
                break
            answer_is_correct = test.check_answer(answer)
            if answer_is_correct:
                self.io.write("\nVastasit oikein")
                self.io.write("Oikeat vastaukset:")
                self.io.write(test.printable_answers())
                WordTestService().add_correct_word_test_answer_to_stats()
                if not test.change_to_next_word():
                    WordTestService().add_completed_word_test_to_stats()
                    self.io.write("\nKoe valmis")
                    break

            else:
                self.io.write("\nVastaus väärin, yritä uudelleen.")
                WordTestService().add_wrong_word_test_answer_to_stats()

    def choose_word_test(self):
        """Allows user to choose the word test"""
        word_tests = WordTestService().get_all_word_tests()
        while True:
            self.print_all_word_tests(word_tests)
            test_id = self.io.read("\nAnna testin numero: ")
            for test in word_tests:
                if str(test["id"]) == test_id:
                    return test_id

    def print_all_word_tests(self, word_tests):
        """Print all choosable word tests for the user to see"""
        self.io.write("\nValitse testi")
        for test in word_tests:
            self.io.write(f"  {test['id']} {test['name']}")


class Stats:
    def __init__(self, io):
        self.io = io
        self.stats = stats_repository

    def run(self):
        """Show statistics about the user"""
        stats = self.stats.get_all_stats()
        self.io.write("\nSanakokeiden tilastot")
        self.io.write(
            f"  Olet kääntänyt oikein {stats['correct_word_test_answers']} sanaa"
        )
        self.io.write(
            f"  Olet antanut {stats['wrong_word_test_answers']} väärää käännöstä"
        )
        self.io.write(f"  Olet suorittanut {stats['word_tests_completed']} sanakoetta")


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
