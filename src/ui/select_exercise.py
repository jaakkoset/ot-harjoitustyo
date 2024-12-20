from tkinter import ttk, constants
from services.word_test import WordTestService

WORD_TEST_LABELS = {"heading": "Valitse sanakoe"}
OTHER_LABELS = {"heading": "Valitse OTHER"}


class SelectExercise:
    def __init__(self, root, windows: dict, exercise_type: str):
        self._root = root
        self._handle_main_menu = windows["main menu"]
        self._open_exercise = windows["open exercise"]
        self._exercise_type = exercise_type
        self.labels = self._set_labels()
        self._frame = None
        self._entry = None

        self._initialize()

    def _set_labels(self):
        """Set the correct labels for an exercise"""
        if self._exercise_type == "word test":
            labels = WORD_TEST_LABELS
        else:
            labels = OTHER_LABELS
        return labels

    def _get_exercises(self) -> list:
        return WordTestService().get_all_word_tests()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text=self.labels["heading"])

        self._entry = ttk.Entry(master=self._frame)
        heading_label.grid(padx=10, pady=10)

        exercises = self._get_exercises()

        for exercise in exercises:
            exercise_button = ttk.Button(
                master=self._frame,
                text=exercise["name"],
                command=self._open_exercise,
            )
            exercise_button.grid(
                column=0,
                columnspan=2,
                sticky=(constants.E, constants.W),
                padx=10,
                pady=5,
            )

        self._frame.grid_columnconfigure(0, weight=1, minsize=600)
