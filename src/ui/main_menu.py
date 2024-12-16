from tkinter import ttk, constants


class MainMenu:
    def __init__(self, root, handle_word_test):
        self._root = root
        self._handle_word_test = handle_word_test
        self._frame = None
        self._entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Päävalikko")

        word_test_button = ttk.Button(
            master=self._frame,
            text="Tee sanakoe",
            command=self._handle_word_test,
        )
        quit_button = ttk.Button(
            master=self._frame,
            text="Lopeta ohjelma",
            command=lambda: self._handle_quit_button("quit button"),
        )

        self._entry = ttk.Entry(master=self._frame)

        heading_label.grid(padx=10, pady=10)
        word_test_button.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=10,
            pady=5,
        )
        quit_button.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=10,
            pady=5,
        )

        self._entry.grid(row=4, column=0, padx=10, pady=10)

        self._frame.grid_columnconfigure(0, weight=1, minsize=600)

    def _handle_quit_button(self, x):
        entry_value = self._entry.get()
        print(f"Value of entry is: {entry_value} + {x}")
