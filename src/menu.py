import pyxel
from ascii import ASCII
from control import Control

class Menu:
    """
    Class that displays the menu.
    """

    def __init__(self) -> None:
        """
        Create the menu.
        """

        self.items: dict[str, str] = {
            "play": "Play",
            "controls": "Controls",
            "restart": "Restart",
            "quit": "Quit"
        }
        self.ascii: ASCII = ASCII()
        self.x: int = 25
        self.y: int = 25
        self.color: int = pyxel.COLOR_GREEN
        self.selected_index: int = 0
        self.items_names: list = list(self.items.keys())
        self.in_menu: bool = True

    def toggle_menu(self) -> None:
        """
        A function to toggle on/off the menu
        """

        self.in_menu = not self.in_menu

    def update(self, controls: Control, game) -> None:
        """
        Handle user input to navigate.

        Args:
            controls (Control): The controls menu.
            game (Game): The main game instance.
        """

        # Navigate the upgrade menu
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            self.selected_index = (self.selected_index + 1) % len(self.items)
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_Z):
            self.selected_index = (self.selected_index - 1) % len(self.items)

        # Purchase the selected upgrade
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_F):
            selected_skill = self.items_names[self.selected_index]
            match selected_skill:
                case "play":
                    self.toggle_menu()
                case "controls":
                    controls.toggle_menu()
                    self.toggle_menu()
                case "restart":
                    game.restart_game()
                case "quit":
                    pyxel.quit()

    def draw(self, game) -> None:
        """
        Draw the menu.
        """

        pyxel.cls(0)
        self.y = 25
        self.ascii.text(self.x, self.y, "--- Menu ---", pyxel.COLOR_YELLOW)
        self.y += 60

        # Display each item
        for i, item in enumerate(self.items):
            item = self.items[item]
            color = pyxel.COLOR_LIME if i == self.selected_index else pyxel.COLOR_WHITE
            self.ascii.text(20, self.y, f"{item}"
, color)
            self.y += 30

        self.y += 30
        self.ascii.text(self.x, self.y, "Press ENTER to select", pyxel.COLOR_DARK_BLUE)
        self.y += 30
        self.ascii.text(self.x, self.y, "Press ZQSD or the arrow keys to switch buttons", pyxel.COLOR_DARK_BLUE)
        self.y += 60

        minutes = game.best_time // 3600
        seconds = (game.best_time // 60) % 60
        self.ascii.text(self.x, self.y, f"Best time: {minutes:02}:{seconds:02}", pyxel.COLOR_LIGHT_BLUE)