# import sys
# from tkinter import Tk, ttk, constants
from ui.main_menu import MainMenu
from ui.exercise import Exercise
from ui.select_exercise import SelectExercise

# from exercises.exercise import Exercise
# from repository.stats_repository import stats_repository
# from services.word_test import WordTestService


class UI:
    """This class is responsible for the user interface"""

    def __init__(self, root):
        self._root = root
        root.geometry("800x800")
        self._current_view = None

    def start(self):
        """Starts the program by opening the main menu"""
        self._show_main_menu()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_main_menu(self):
        self._show_main_menu()

    def _handle_word_test(self):
        """Opens an exercise as a word test"""
        self._show_exercise("Sanakoe")

    def _handle_select_word_test(self):
        """Opens a list of all word tests"""
        self._show_select_exercise("word test")

    def _show_main_menu(self):
        """Opens the main menu"""
        self._hide_current_view()
        self._current_view = MainMenu(self._root, self._handle_select_word_test)

        self._current_view.pack()

    def _show_exercise(self, title):
        """Opens the the window for any exercise. Only the title and some texts differ
        between exercises, but otherwise the logic is the same."""
        self._hide_current_view()
        self._current_view = Exercise(self._root, self._handle_main_menu, title)

        self._current_view.pack()

    def _show_select_exercise(self, exercise_type):
        """Opens the window where the user can select an exercise"""
        self._hide_current_view()
        if exercise_type == "word test":
            open_exercise = self._handle_word_test
        else:
            raise TypeError("Ei ollut sanakoe")

        windows = {"main menu": self._handle_main_menu, "open exercise": open_exercise}
        self._current_view = SelectExercise(self._root, windows, exercise_type)

        self._current_view.pack()

# class WordTest:
#     """Contains the program loop of word tests"""

#     def __init__(self, io):
#         self.io = io

#     def run(self):
#         word_test_id = self.choose_word_test()
#         test = Exercise(word_test_id)
#         self.io.write(
#             "\nVoit poistua kokeesta missä vaiheessa tahansa kirjoittamalla x"
#         )

#         while True:
#             question = test.question()
#             self.io.write("\nSuomenna sana: " + question)
#             answer = self.io.read()
#             if answer == "x":
#                 self.io.write("\nLopetit kokeen")
#                 break
#             answer_is_correct = test.check_answer(answer)
#             if answer_is_correct:
#                 self.io.write("\nVastasit oikein")
#                 self.io.write("Oikeat vastaukset:")
#                 self.io.write(test.printable_answers())
#                 WordTestService().add_correct_word_test_answer_to_stats()
#                 if not test.change_to_next_question():
#                     WordTestService().add_completed_word_test_to_stats()
#                     self.io.write("\nKoe valmis")
#                     break

#             else:
#                 self.io.write("\nVastaus väärin, yritä uudelleen.")
#                 WordTestService().add_wrong_word_test_answer_to_stats()

#     def choose_word_test(self):
#         """Allows user to choose the word test"""
#         word_tests = WordTestService().get_all_word_tests()
#         while True:
#             self.print_all_word_tests(word_tests)
#             test_id = self.io.read("\nAnna testin numero: ")
#             for test in word_tests:
#                 if str(test["id"]) == test_id:
#                     return test_id

#     def print_all_word_tests(self, word_tests):
#         """Print all choosable word tests for the user to see"""
#         self.io.write("\nValitse testi")
#         for test in word_tests:
#             self.io.write(f"  {test['id']} {test['name']}")


# class Stats:
#     def __init__(self, io):
#         self.io = io
#         self.stats = stats_repository

#     def run(self):
#         """Show statistics about the user"""
#         stats = self.stats.get_all_stats()
#         self.io.write("\nSanakokeiden tilastot")
#         self.io.write(
#             f"  Olet kääntänyt oikein {stats['correct_word_test_answers']} sanaa"
#         )
#         self.io.write(
#             f"  Olet antanut {stats['wrong_word_test_answers']} väärää käännöstä"
#         )
#         self.io.write(f"  Olet suorittanut {stats['word_tests_completed']} sanakoetta")
