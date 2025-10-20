import pyxel
from player import Player

class Game:
    """
    Class that manages the game in general
    """
    def __init__(self) -> None:
        """
        Initialize the class Player

        takes no arguments and returns None
        """

        self.player = Player()

        self.window_width: int = 1000 # width of the window
        self.window_height: int = 750 # height of the window
        self.window_title: str = "Window-Kill" # title of the window

        pyxel.init(self.window_width, self.window_height, title=self.window_title) # initializes Pyxel and creates the window

        pyxel.run(self.update, self.draw) # call infinitely the update and draw functions
    
    def update(self):
        """
        Function that calls all the update functions of every class and is called infinitely by Pyxel

        takes no arguments and returns None
        """
        self.player.update() # updates the player

    def draw(self):
        """
        Function that calls all the draw functions of every class and is called infinitely by Pyxel

        takes no argyments and returns None
        """
        pyxel.cls(0) # clears the window
        self.player.draw() # draws the player
