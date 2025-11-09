import pyxel

class ASCII:
    """
    Class that manages the ASCII police
    """

    def __init__(self) -> None:
        """For each character, see ascii.txt"""
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
        Convert each character into a ASCII font

        @param string: the string to convert
        @return: a list with top/mid/bottom of the string for each character 
        """

        string = string.lower()
        liste: list[str] = ["", "", ""]
        for letter in string:
            for i in range(3):
                liste[i] += self.alphabet[letter][i] + " "
        return liste
    
    def text(self, x: float, y: float, text: str, color: int) -> None:
        """
        Display a converted text with pyxel

        @param x: float. The x location of the text
        @param y: float. The y location of the text
        @param text: str. The text
        @param color: int. The color
        @return: None
        """

        converted = self.convert(text)
        SPACE = 7
        for i in range(3):
            pyxel.text(x, y + SPACE * i, converted[i], color)
        return