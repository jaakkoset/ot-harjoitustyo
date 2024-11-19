"""Class IOConsole provides methods for interacting with user"""


class IOConsole:
    """Methods for interacting with the user"""

    def read(self, text: str = "") -> str:
        """Show the argument text to user and return the user input"""
        return input(text)

    def write(self, text: str):
        """Show the argument text to user"""
        print(text)
