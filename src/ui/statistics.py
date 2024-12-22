from tkinter import ttk, constants
from services.statistics import StatisticsService


class StatisticsUI:
    def __init__(self, root, handle_main_menu):
        self._root = root
        self._handle_main_menu = handle_main_menu
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        if self._frame is not None:
            self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._set_title()
        self._set_main_menu_button()
        self._display_statistics()
        self._frame.grid_columnconfigure(0, weight=1, minsize=600)

    def _set_title(self):
        """Set the title"""
        heading_label = ttk.Label(master=self._frame, text="Tilastot")
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

    def _display_statistics(self):
        """Display all statistics"""
        stats = StatisticsService().printable_statistics()
        stats_label = ttk.Label(master=self._frame, text=stats)
        stats_label.grid(padx=10, pady=10)
