from ui.main_menu import MainMenu
from ui.exercise import ExerciseUI
from ui.select_exercise import SelectExercise
from ui.statistics import StatisticsUI


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

    def _handle_word_test(self, exercise_id):
        """Opens an exercise as a word test"""
        self._show_exercise(exercise_id)

    def _handle_select_word_test(self):
        """Opens a list of all word tests"""
        self._show_select_exercise("word test")

    def _handle_statistics(self):
        self._show_statistics()

    def _show_main_menu(self):
        """Opens the main menu"""
        self._hide_current_view()
        self._current_view = MainMenu(
            self._root, self._handle_select_word_test, self._handle_statistics
        )

        self._current_view.pack()

    def _show_exercise(self, exercise_id):
        """Opens the the window for any exercise. Only the title and some texts differ
        between exercises, but otherwise the logic is the same."""
        self._hide_current_view()
        self._current_view = ExerciseUI(self._root, self._handle_main_menu, exercise_id)

        self._current_view.pack()

    def _show_select_exercise(self, exercise_type):
        """Opens the window where the user can select an exercise"""
        self._hide_current_view()
        if exercise_type == "word test":
            handle_open_exercise = self._handle_word_test
        else:
            raise TypeError("Ei ollut sanakoe")

        self._current_view = SelectExercise(
            self._root, exercise_type, self._handle_main_menu, handle_open_exercise
        )

        self._current_view.pack()

    def _show_statistics(self):
        """Show all statistics"""
        self._hide_current_view()
        self._current_view = StatisticsUI(self._root, self._handle_main_menu)
        self._current_view.pack()
