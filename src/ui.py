"""User interface"""

from io_console import IOConsole

COMMANDS = {
    "q": "q lopeta ohjelma",
    "1": "1 tee sanakoe",
}


class Program:
    """Program loop and its helper methods"""

    def __init__(self, io):
        self._io = io

    def program(self):
        """Program loop"""
        while True:
            self.print_commands()
            command = self._io.read("Anna komento: ")

            if command == "1":
                self._io.write("valitsit 1")

            if command == "q":
                break

    def print_commands(self):
        self._io.write("Komennot:")
        for command in COMMANDS:
            self._io.write("" + command)


if __name__ == "__main__":
    Program(IOConsole()).program()
