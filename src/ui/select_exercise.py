from tkinter import ttk, constants
from services.word_test import WordTestService


class SelectExercise:
    """UI for selecting the exercise."""

    def __init__(
        self, root, handle_main_menu, handle_open_exercise
    ):
        self._root = root
        self._handle_main_menu = handle_main_menu
        self._open_exercise = handle_open_exercise
        self._frame = None
        self._entry = None

        self._initialize()

    def _get_exercises(self) -> list:
        """Get a list of all exercises"""
        return WordTestService().get_all_word_tests()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._set_heading_label()
        self._set_main_menu_button()
        self._set_exercise_list()
        self._frame.grid_columnconfigure(0, weight=1, minsize=600)

    def _set_heading_label(self):
        heading_label = ttk.Label(master=self._frame, text="Valitse koe")
        heading_label.grid(row=0, padx=10, pady=10)

    def _set_main_menu_button(self):
        """Set the main menu button"""
        main_menu_button = ttk.Button(
            master=self._frame,
            text="Takaisin päävalikkoon",
            command=self._handle_main_menu,
        )
        main_menu_button.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=(constants.W),
            padx=10,
            pady=5,
        )

    def _set_exercise_list(self):
        """List all exercises and give each one a button"""
        exercises = self._get_exercises()

        for exercise in exercises:
            exercise_button = ttk.Button(
                master=self._frame,
                text=exercise["name"],
                command=lambda id=exercise["id"]: self._open_exercise(id),
            )
            exercise_button.grid(
                column=0,
                columnspan=2,
                sticky=(constants.E, constants.W),
                padx=10,
                pady=5,
            )
