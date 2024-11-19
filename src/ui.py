"""
User interface

Class:
    Program"""

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
        """Print all commands for the user"""
        self._io.write("Komennot:")
        for command in COMMANDS.values():
            self._io.write("  " + command)
