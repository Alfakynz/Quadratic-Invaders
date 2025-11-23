import pyxel

class ASCII:
    """
    Class that manages the ASCII font.
    """

    def __init__(self) -> None:
        """
        For each character, see ascii.txt (not included into the documentation, see the repo on [GitHub](https://github.com/Alfakynz/Quadratic-Invaders)).
        Each character is represented by an array of 3 strings (top, middle, bottom).
        """

        self.alphabet: dict[str, list[str]] = {
            "a": ["  /\\  ", " /--\\ ", "/    \\"],
            "b": ["|--\\", "| -<", "|__/"],
            "c": [" /--", "|   ", " \\__"],
            "d": ["|--\\ ", "|   |", "|__/ "],
            "e": ["|---", "|-- ", "|___"],
            "f": ["|---", "|-- ", "|   "],
            "g": [" /-- ", "|  __", " \\__/"],
            "h": ["|   |", "|---|", "|   |"],
            "i": ["|", "|", "|"],
            "j": ["|   ", "|   ", "\\__/"],
            "k": ["| /", "|| ", "| \\"],
            "l": ["|   ", "|   ", "|___"],
            "m": ["|\\ /|", "| v |", "|   |"],
            "n": ["|\\  |", "| \\ |", "|  \\|"],
            "o": ["/---\\", "|   |", "\\___/"],
            "p": ["|-\\", "|_/", "|  "],
            "q": ["/---\\", "|   |", "\\__\\_"],
            "r": ["|-\\", "|_/", "| \\"],
            "s": ["/-\\", " \\ ", "\\_/"],
            "t": ["-----", "  |  ", "  |  "],
            "u": ["|  |", "|  |", "\\__/"],
            "v": ["\\    /", " \\  / ", "  \\/  "],
            "w": ["\\        /", " \\  /\\  / ", "  \\/  \\/  "],
            "x": ["\\ /", " X ", "/ \\"],
            "y": ["\\ /", " V ", " | "],
            "z": ["--/", " / ", "/__"],
            " ": ["   ", "   ", "   "],
            ".": [" ", " ", "O"],
            ":": ["O", " ", "O"],
            "(": ["/", "|", "\\"],
            ")": ["\\", "|", "/"],
            "_": ["   ", "   ", "==="],
            "-": ["   ", "===", "   "],
            "+": [" | ", "=|=", " | "],
            "0": ["/--\\", "|  |", "\\__/"],
            "1": ["/| ", " | ", "_|_"],
            "2": ["/-\\", "  /", "/__"],
            "3": ["--\\", " < ", "__/"],
            "4": [" /| ", "/_|_", "  | "],
            "5": ["|--", " -\\", "__/"],
            "6": ["/-- ", "|--\\", "\\__/"],
            "7": ["---/", "  / ", " /  "],
            "8": ["/--\\", "|--|", "\\__/"],
            "9": ["/--\\", "\\--|", " __/"]
        }

    def convert(self, string: str) -> list[str]:
        """
        Convert each character into an ASCII font. For each character, get the top/mid/bottom part of letters from self.alphabet.

        Args:
            string (str): The string to convert.
        
        Returns:
            list[str]: An array with top/mid/bottom of the string for each character.
        """

        string = string.lower()
        array: list[str] = ["", "", ""]
        for letter in string:
            for i in range(3):
                array[i] += self.alphabet[letter][i] + " "
        return array
    
    def text(self, x: float, y: float, text: str, color: int) -> None:
        """
        Display a converted text with pyxel. Display the top/mid/bottom parts of the ASCII font one below the other.

        Args:
            x (float): The x location of the text.
            y (float): The y location of the text.
            text (str): The text to convert.
            color (int): The color to use.
        """

        converted = self.convert(text)
        SPACE = 7
        for i in range(3):
            pyxel.text(x, y + SPACE * i, converted[i], color)
        return