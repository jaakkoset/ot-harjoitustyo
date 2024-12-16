from tkinter import ttk, constants


class Exercise:
    def __init__(self, root, handle_main_menu, title):
        self._root = root
        self._handle_main_menu = handle_main_menu
        self.title = title
        self._frame = None
        self._entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        main_menu_button = ttk.Button(
            master=self._frame,
            text="Takaisin päävalikkoon",
            command=self._handle_main_menu,
        )
        heading_label = ttk.Label(master=self._frame, text=self.title)
        question_label = ttk.Label(master=self._frame, text="Anna vastaus")

        answer_button = ttk.Button(
            master=self._frame,
            text="Vastaa",
            command=self._handle_answer,
        )

        self._entry = ttk.Entry(master=self._frame)

        heading_label.grid(padx=10, pady=10)
        main_menu_button.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=(constants.W),
            padx=10,
            pady=5,
        )
        question_label.grid(padx=10, pady=10)
        self._entry.grid(row=3, column=0, padx=10, pady=10)
        answer_button.grid(
            row=4,
            column=0,
            columnspan=2,

            padx=10,
            pady=5,
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=600)

    def _handle_answer(self):
        entry_value = self._entry.get()
        print(f"Value of entry is: {entry_value}")
