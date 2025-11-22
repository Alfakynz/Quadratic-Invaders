import pyxel
from PIL import Image as PILImage
from pathlib import Path
from player import Player
from enemies import Enemies
from upgrades import Upgrade
from menu import Menu
from control import Control

class Game:
    """
    Class that manages the game in general.
    """

    def __init__(self) -> None:
        """
        Initialize the class Player.
        """

        self.player: Player = Player() # creates the object Player
        self.enemies: Enemies = Enemies(self.player) # creates the object Enemies
        self.upgrade: Upgrade = Upgrade(self.player) # creates the object Upgrade
        self.menu: Menu = Menu() # creates the object Menu
        self.control: Control = Control() # creatse the object Control

        self.window_width: int = 1250 # width of the window
        self.window_height: int = 800 # height of the window

        self.window_title: str = "Window-Kill" # title of the window

        self.in_upgrade_menu: bool = False

        # Matches the paths with the files (made by ChatGPT)
        BASE_DIR: Path = Path(__file__).resolve().parent
        ASSETS_DIR: Path = BASE_DIR.parent / "assets"
        SRC: Path = ASSETS_DIR / "GameOver.png"
        DST: Path = ASSETS_DIR / "_GameOver_256.png"

        # Resizes the GameOver image into a 256x256 format (made by ChatGPT)
        im = PILImage.open(SRC).convert("RGBA")
        # Uses the newer Resampling enum if available, otherwise falls back to legacy constants
        resampling = getattr(PILImage, "Resampling", None)
        if resampling is not None:
            resample_method = resampling.BICUBIC
        else:
            resample_method = getattr(PILImage, "BICUBIC", getattr(PILImage, "NEAREST"))
        im.thumbnail((256, 256), resample_method)
        im.save(DST)

        pyxel.init(self.window_width, self.window_height, title = self.window_title, fps = 60, quit_key = False) # initializes Pyxel and creates the window
        pyxel.images[0].load(0, 0, str(DST)) #puts the game over image in Pyxel's image bank 0 at the coordinates (0, 0)

        self.game_over_w, self.game_over_h = im.size #gets the size of the image

        #tests if the width and the height of the image is between 1 and 256 (inclusive) since Pyxel has difficulties with invalid surfaces (zero, negative, higher than 256, etc...)
        assert 1 <= self.game_over_w <= 256
        assert 1 <= self.game_over_h <= 256

        self.cursor_path: Path = ASSETS_DIR / "cursor.png"
        self.cursor_pixels = self.load_image_as_array(str(self.cursor_path))

        pyxel.run(self.update, self.draw) # calls infinitely the update and draw methods

    def update(self) -> None:
        """
        Method that calls all the update methods of every class and is called infinitely by Pyxel.
        """

        # Temporary quit the game with 0
        if pyxel.btnp(pyxel.KEY_0):
            pyxel.quit()
        
        if self.player.skills["hp"] > 0:
            if pyxel.btnp(pyxel.KEY_ESCAPE):
                if not self.in_upgrade_menu and not self.control.in_control:
                    self.menu.toggle_menu()
                else:
                    self.in_upgrade_menu = False

            if pyxel.btnp(pyxel.KEY_E) and not self.menu.in_menu:
                self.upgrade.message = ""  # Clear previous messages when toggling menu
                self.in_upgrade_menu = not self.in_upgrade_menu

            if self.control.in_control:
                self.control.update(self.menu) # updates the control menu
                return # skips the rest of the update method

            if self.menu.in_menu:
                self.menu.update(self.control) # updates the menu
                return # skips the rest of the update method

            if self.in_upgrade_menu:
                self.upgrade.update() # updates the upgrade menu
                return # skips the rest of the update method

            self.player.update(self.enemies.enemies_array, 
                               self.enemies.size, 
                               self.enemies.attack,
                               self.window_width,
                               self.window_height) # updates the player and gives some attributes of the Enemies class to the Player Class

            self.enemies.update(self.player.player_x,
                                self.player.player_y,
                                self.player.r,
                                self.player.skills["attack"],
                                self.player.bullets.bullets_array,
                                self.player.bullets.size,
                                self.window_width,
                                self.window_height) # updates the enemies and gives some attributes of the Player class and the Bullets to the Enemies Class
            return

    def draw(self) -> None:
        """
        Method that calls all the draw methods of every class and is called infinitely by Pyxel.
        """

        pyxel.cls(0) # clears the window
        pyxel.mouse(False) # displays the mouse on the window

        if self.control.in_control:
            self.control.draw() # draws the controls menu
        elif self.menu.in_menu:
            self.menu.draw() # draws the menu
        elif self.player.skills["hp"] > 0:
            if self.in_upgrade_menu:
                self.upgrade.draw() # draws the upgrade menu
            else:
                self.player.draw() # draws the player
                self.enemies.draw() # draws the enemies
                self.draw_cursor(pyxel.mouse_x - 16, pyxel.mouse_y - 16) # draws a custom cursor (centered)
        else:
            #centers the image
            x = (self.window_width  - self.game_over_w) // 2
            y = (self.window_height - self.game_over_h) // 2

            pyxel.blt(x, y, 0, 0, 0, self.game_over_w, self.game_over_h) #displays the game over image when the player dies

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
            x (int): the x-coordinate to draw the cursor.
            y (int): the y-coordinate to draw the cursor.
        """

        for j, row in enumerate(self.cursor_pixels):
            for i, color in enumerate(row):
                if color != 0:
                    pyxel.pset(x + i, y + j, color)