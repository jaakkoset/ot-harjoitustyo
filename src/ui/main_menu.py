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
            command=self._root.destroy,
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

        self._frame.grid_columnconfigure(0, weight=1, minsize=600)
