import pyxel
from player import Player
from enemies import Enemies
from upgrades import Upgrade

class Game:
    """
    Class that manages the game in general
    """
    def __init__(self) -> None:
        """
        Initialize the class Player

        takes no arguments and returns None
        """

        self.player = Player() # creates the object Player
        self.enemies = Enemies() # creates the object Enemies
        self.upgrade = Upgrade(self.player) # creates the object Upgrade

        self.window_width: int = 1000 # width of the window
        self.window_height: int = 750 # height of the window

        # gives the width and height of the window to the different classes
        self.player.window_width = self.window_width
        self.player.window_height = self.window_height
        self.enemies.window_width = self.window_width
        self.enemies.window_height = self.window_height
        self.player.bullets.window_width = self.window_width
        self.player.bullets.window_height = self.window_height

        self.window_title: str = "Window-Kill" # title of the window

        self.in_upgrade_menu: bool = False

        pyxel.init(self.window_width, self.window_height, title=self.window_title, fps=60) # initializes Pyxel and creates the window

        pyxel.run(self.update, self.draw) # call infinitely the update and draw functions

    def update(self) -> None:
        """
        Function that calls all the update functions of every class and is called infinitely by Pyxel

        takes no arguments -> None
        """

        if pyxel.btnp(pyxel.KEY_E):
            self.in_upgrade_menu = not self.in_upgrade_menu

        if self.in_upgrade_menu:
            self.upgrade.update() # updates the upgrade menu
            return # skips the rest of the update function

        self.player.update() # updates the player

        # gives the player's position to the enemies
        self.enemies.player_x = self.player.player_x
        self.enemies.player_y = self.player.player_y

        self.enemies.update() # updates the enemies

        return

    def draw(self) -> None:
        """
        Function that calls all the draw functions of every class and is called infinitely by Pyxel

        takes no arguments -> None
        """

        pyxel.cls(0) # clears the window
        pyxel.mouse(True) # displays the mouse on the window

        if self.in_upgrade_menu:
            self.upgrade.draw() # draws the upgrade menu
        else:
            self.player.draw() # draws the player
            self.enemies.draw() # draws the enemies

        return

