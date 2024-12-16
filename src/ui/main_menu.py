from tkinter import ttk, constants


class MainMenu:
    def __init__(self, root):
        self._root = root
        root.geometry("800x1000")
        self._entry = None

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Päävalikko")

        word_test_button = ttk.Button(master=self._root, text="Tee sanakoe")
        quit_button = ttk.Button(
            master=self._root,
            text="Lopeta ohjelma",
            command=lambda: self._handle_button_click("button a"),
        )

        self._entry = ttk.Entry(master=self._root)

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

        self._root.grid_columnconfigure(0, weight=1, minsize=600)

    def _handle_button_click(self, x):
        entry_value = self._entry.get()
        print(f"Value of entry is: {entry_value} + {x}")
