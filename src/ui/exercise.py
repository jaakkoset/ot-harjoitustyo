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
        self._was_answer_correct_label = None
        self._next_question_button = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy_frame(self):
        if self._frame is not None:
            self._frame.destroy()

    def initialize_frame(self):
        self.destroy_frame()
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(0, weight=1, minsize=600)
        self.pack()

    def destroy_widget(self, widget):
        """Destroys a given ttk widget (e.g. Label, Button) if it exists"""
        if widget is not None:
            widget.destroy()

    def _initialize(self):
        self.initialize_frame()
        self._set_title()
        self._set_main_menu_button()
        self._set_question()
        self._set_answer_field()
        self._set_answer_button()
        # self._frame.grid_columnconfigure(0, weight=1, minsize=600)

    def _set_title(self):
        """Set the title"""
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

    def _set_next_question_button(self):
        """Set the button that changes the question"""
        self._next_question_button = ttk.Button(
            master=self._frame,
            text="Seuraava kysymys",
            command=self._handle_next_question,
        )
        self._next_question_button.grid(
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
        )

    def _display_correct_answer_view(self):
        """Display the view the user gets after answering correctly"""
        self.initialize_frame()
        self._set_title()
        self._set_main_menu_button()
        self._set_question()
        self._set_answer_label("Oikein")

    def _display_wrong_answer_view(self):
        """Display the view the user gets after answering incorrectly"""
        self._set_answer_label("Vastaus on väärin")

    def _set_answer_label(self, label_text: str):
        """Display the label that tells whether the answer was correct or not

        Args:
            label_text: the text to be displayed"""
        self.destroy_widget(self._was_answer_correct_label)
        self._was_answer_correct_label = ttk.Label(master=self._frame, text=label_text)
        self._was_answer_correct_label.grid(padx=10, pady=10)

    def _handle_answer(self):
        """Handles the anser given by the user"""
        entry_value = self._entry.get()
        answer_is_correct = self.exercise.check_answer(entry_value)
        if answer_is_correct:
            self._display_correct_answer_view()
        else:
            self._display_wrong_answer_view()

        self.destroy_widget(self._next_question_button)
        self._set_next_question_button()

    def _handle_next_question(self):
        pass
