from tkinter import ttk, constants
from entities.exercise import Exercise


class ExerciseUI:
    def __init__(self, root, handle_main_menu, title, exercise_id):
        self._root = root
        self._handle_main_menu = handle_main_menu
        self.title = title
        self.exercise_id = exercise_id
        self.exercise = Exercise(self.exercise_id)

        self._frame = None
        self._entry = None
        self._question_label = None
        self._answer_button = None
        self._check_answer_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def destroy_widget(self, widget):
        """Destroys a given ttk widget (e.g. Label, Button) if it exists"""
        if widget is not None:
            widget.destroy()

    def _initialize(self):
        self._set_title()
        self._set_main_menu_button()
        self._set_question()
        self._set_answer_field()
        self._set_answer_button()
        self._frame.grid_columnconfigure(0, weight=1, minsize=600)

    def _set_title(self):
        """Set the title"""
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Sanakoe")
        heading_label.grid(padx=10, pady=10)

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

    def _set_question(self):
        """Set the question"""
        question_label = ttk.Label(
            master=self._frame, text=f"Suomenna sana: {self.exercise.question()}"
        )
        question_label.grid(row=2, padx=10, pady=10)

    def _set_answer_field(self):
        """Set the answer field"""
        self._entry = ttk.Entry(master=self._frame)
        self._entry.grid(row=3, column=0, padx=10, pady=10)

    def _set_answer_button(self):
        """Set the answer button"""
        self._answer_button = ttk.Button(
            master=self._frame,
            text="Vastaa",
            command=self._handle_answer,
        )
        self._answer_button.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
        )

    def _set_correct_answer_view(self):
        """Set the view the user gets after answering correctly"""
        self.destroy_widget(self._answer_button)
        self.destroy_widget(self._entry)

    def _handle_answer(self):
        if self._check_answer_label is not None:
            self._check_answer_label.destroy()
        entry_value = self._entry.get()
        answer_is_correct = self.exercise.check_answer(entry_value)
        if answer_is_correct:
            text = "oikein"
            self._set_correct_answer_view()
        else:
            text = "väärin"
        self._check_answer_label = ttk.Label(
            master=self._frame, text=f"Vastaus on {text}"
        )
        self._check_answer_label.grid(padx=10, pady=10)
