import pyxel
from PIL import Image as PILImage
from pathlib import Path
from player import Player
from enemies import Enemies
from upgrades import Upgrade

# Matches the paths with the files (made by ChatGPT)
BASE_DIR = Path(__file__).resolve().parent           
ASSETS_DIR = BASE_DIR.parent / "assets"              
SRC = ASSETS_DIR / "GameOver.png"
DST = ASSETS_DIR / "_GameOver_256.png"               

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
        self.enemies = Enemies(self.player) # creates the object Enemies
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

        pyxel.init(self.window_width, self.window_height, title = self.window_title, fps = 60) # initializes Pyxel and creates the window
        pyxel.image(0).load(0, 0, str(DST))

        # Resizes the GameOver image into a 256x256 format (made by ChatGPT)
        im = PILImage.open(SRC).convert("RGBA")
        im.thumbnail((256, 256), PILImage.BICUBIC)
        im.save(DST)
        self.game_over_w, self.game_over_h = im.size
        self.game_over_w = max(1, min(self.game_over_w, 256))
        self.game_over_h = max(1, min(self.game_over_h, 256))
        self.cursor_path = ASSETS_DIR / "cursor.png"
        self.cursor_pixels = self.load_image_as_array(str(self.cursor_path))

        pyxel.run(self.update, self.draw) # call infinitely the update and draw functions

    def variables_update(self):

        self.player.enemies_list = self.enemies.enemies_list
        self.player.enemy_size = self.enemies.size
        self.player.enemies_damage = self.enemies.damage

        self.player.bullets.enemies_list = self.enemies.enemies_list
        self.player.bullets.enemy_size = self.enemies.size

        # gives the player's position to the enemies
        self.enemies.player_x = self.player.player_x
        self.enemies.player_y = self.player.player_y

        self.enemies.player_size = self.player.r
        self.enemies.player_attack = self.player.skills["attack"]

        self.enemies.bullets_list = self.player.bullets.bullets_list
        self.enemies.bullet_size = self.player.bullets.size

    def update(self) -> None:
        """
        Function that calls all the update functions of every class and is called infinitely by Pyxel

        takes no arguments -> None
        """
        if self.player.skills["hp"] > 0:
            if pyxel.btnp(pyxel.KEY_E):
                self.upgrade.message = ""  # Clear previous messages when toggling menu
                self.in_upgrade_menu = not self.in_upgrade_menu

            if self.in_upgrade_menu:
                self.upgrade.update() # updates the upgrade menu
                return # skips the rest of the update function

            self.variables_update()

            self.player.update() # updates the player

            self.enemies.update() # updates the enemies

            return

    def draw(self) -> None:
        """
        Function that calls all the draw functions of every class and is called infinitely by Pyxel

        takes no arguments -> None
        """

        pyxel.cls(0) # clears the window
        pyxel.mouse(False) # displays the mouse on the window

        if self.player.skills["hp"] > 0:
            if self.in_upgrade_menu:
                self.upgrade.draw() # draws the upgrade menu
            else:
                self.player.draw() # draws the player
                self.enemies.draw() # draws the enemies
                self.draw_cursor(pyxel.mouse_x - 16, pyxel.mouse_y - 16) # draws a custom cursor (centered)

            return
        
        else:
            x = (self.window_width  - self.game_over_w) // 2
            y = (self.window_height - self.game_over_h) // 2
            pyxel.blt(x, y, 0, 0, 0, self.game_over_w, self.game_over_h)


    def load_image_as_array(self, path: str, color: int = 12) -> list[list[int]]:
        """
        Load an image and convert it to a 2D array of pixel colors based on transparency.
        Args:
            path (str): The file path to the image.
            color (int): The color to use for non-transparent pixels.
        Returns:
            list[list[int]]: A 2D array representing the image pixels.
        """
        img = PILImage.open(path).convert("RGBA")
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