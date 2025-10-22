from PIL import Image
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
        self.cursor_pixels = self.load_image_as_array("assets/cursor.png")

        self.in_upgrade_menu: bool = False

        pyxel.init(self.window_width, self.window_height, title = self.window_title, fps = 60) # initializes Pyxel and creates the window

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
        pyxel.mouse(False) # displays the mouse on the window

        if self.in_upgrade_menu:
            self.upgrade.draw() # draws the upgrade menu
        else:
            self.player.draw() # draws the player
            self.enemies.draw() # draws the enemies
            self.draw_cursor(pyxel.mouse_x - 16, pyxel.mouse_y - 16) # draws a custom cursor (centered)

        return

    def load_image_as_array(self, path: str, color: int = 12) -> list[list[int]]:
        """
        Load an image and convert it to a 2D array of pixel colors based on transparency.
        Args:
            path (str): The file path to the image.
            color (int): The color to use for non-transparent pixels.
        Returns:
            list[list[int]]: A 2D array representing the image pixels.
        """
        img = Image.open(path).convert("RGBA")
        w, h = img.size
        data = []

        for y in range(h):
            row = []
            for x in range(w):
                pixel = img.getpixel((x, y))
                if isinstance(pixel, tuple) and len(pixel) == 4:
                    a = pixel[3]
                elif isinstance(pixel, (int, float)):
                    a = pixel
                else:
                    a = 0
                row.append(color if a > 10 else 0)
            data.append(row)

        return data
    
    def draw_cursor(self, x, y) -> None:
        """
        Draw a custom cursor at the specified position.
        Args:
            x (int): The x-coordinate to draw the cursor.
            y (int): The y-coordinate to draw the cursor.
        
        Returns:
            None
        """
        for j, row in enumerate(self.cursor_pixels):
            for i, color in enumerate(row):
                if color != 0:
                    pyxel.pset(x + i, y + j, color)