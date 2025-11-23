import pyxel
from ascii import ASCII

class Control:
    """
    Class that manages the control screen
    """

    def __init__(self) -> None:
        """
        Create the control informations
        """

        self.items: list[str] = [
            "Press ENTER or F to select",
            "Use ZQSD or the arrow keys to move",
            "Press ESCAPE to close the window or open the menu",
            "Press E or RSHIFT to open the upgrade menu",
            "Hold left click to shoot enemies"
        ]
        self.ascii: ASCII = ASCII()
        self.x: int = 25
        self.y: int = 25
        self.in_control: bool = False

    def toggle_menu(self):
        self.in_control = not self.in_control

    def update(self, menu) -> None:
        """
        Handle user input to quit the controls.

        Args:
            menu (Menu): The main menu to return to.
        """

        # Navigate the upgrade menu
        if pyxel.btnp(pyxel.KEY_ESCAPE) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_F):
            menu.toggle_menu()
            self.toggle_menu()

    def draw(self) -> None:
        """
        Draw the controls.
        """

        pyxel.cls(0)
        self.y = 25
        self.ascii.text(self.x, self.y, "--- Controls ---", pyxel.COLOR_YELLOW)
        self.y += 60
        self.ascii.text(self.x, self.y, "Back", pyxel.COLOR_LIME)
        self.y += 60

        # Display each item
        for item in self.items:
            self.ascii.text(self.x, self.y, item, pyxel.COLOR_DARK_BLUE)
            self.y += 30