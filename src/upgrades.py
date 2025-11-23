import pyxel
from player import Player
from skill import Skill
from ascii import ASCII

class Upgrade:
    """
    Class that displays the upgrade menu.
    """

    def __init__(self, player: Player) -> None:
        """
        Create the upgrade menu to buy skills upgrades.

        Args:
            player (Player): The Player.
        """

        self.player: Player = player
        self.upgrades: dict[str, Skill] = {
            "hp": Skill("hp", "Increase your health by 1", 25, 1),
            "attack": Skill("attack", "Increase your attack by 1", 10, 1),
            "shield": Skill("shield", "Increase your shield by 5", 50, 5),
            "speed": Skill("speed", "Increase your speed by 1", 5, 1),
            "fire_rate": Skill("fire rate", "Increase your fire rate by 2", 10, -2),
        }
        self.ascii: ASCII = ASCII()
        self.x: int = 25
        self.y: int = 25
        self.color: int = pyxel.COLOR_GREEN
        self.selected_index: int = 0
        self.skill_names: list = list(self.upgrades.keys())

    def increase(self, skill: str) -> None:
        """
        Increase the selected skill of the player if he has enough XP.
        
        Args:
            skill (str): The skill to improve
        """

        # Skill not found
        if skill not in self.upgrades:
            self.message = "Skill not found"
            self.color = pyxel.COLOR_RED
            return
        
        upgrade = self.upgrades[skill]

        # Insufficient XP
        if self.player.xp < upgrade.price:
            self.message = "Insufficient XP"
            self.color = pyxel.COLOR_RED
            return
        
        #speed maxed out (lower than 15)
        if skill == "speed" and upgrade.level == 11:
            self.message = "Skill maxed out"
            return
        
        #shield maxed out (lower than 95)
        if skill == "shield" and upgrade.level == 19:
            self.message = "Skill maxed out"
            return
        
        #fire rate maxed out (higher than 10)
        if skill == "fire rate" and upgrade.level == 25:
            self.message = "Skill maxed out"
            return
        
        self.player.xp -= upgrade.price
        self.player.skills[skill] += upgrade.amount

        upgrade.price = int(upgrade.price * 1.5)
        upgrade.level += 1

        self.message = f"{skill.capitalize()} upgraded to level {upgrade.level}"
        self.color = pyxel.COLOR_LIGHT_BLUE
        return

    def update(self) -> None:
        """
        Handle user input to navigate and purchase upgrades.
        """

        # Navigate the upgrade menu
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            self.selected_index = (self.selected_index + 1) % len(self.skill_names)
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_Z):
            self.selected_index = (self.selected_index - 1) % len(self.skill_names)

        # Purchase the selected upgrade
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_F):
            selected_skill = self.skill_names[self.selected_index]
            self.increase(selected_skill)
    
    def draw(self) -> None:
        """
        Draw the upgrade menu.
        """

        pyxel.cls(0)
        self.y = 25
        self.ascii.text(self.x, self.y, "--- Upgrade Menu ---", pyxel.COLOR_YELLOW)
        self.y += 60
        self.draw_hp(self.x, self.y)
        self.y += 30
        self.ascii.text(self.x, self.y, f"XP: {self.player.xp}", pyxel.COLOR_YELLOW)

        self.y += 60

        # Display each upgrade option
        for i, skill_name in enumerate(self.skill_names):
            upgrade = self.upgrades[skill_name]
            color = pyxel.COLOR_LIME if i == self.selected_index else pyxel.COLOR_WHITE
            self.ascii.text(20, self.y, f"{upgrade.name} Lv.{upgrade.level}: {upgrade.description} ({upgrade.price})"
, color)
            self.y += 30

        self.y += 30
        self.ascii.text(self.x, self.y, "Press ENTER to buy", pyxel.COLOR_DARK_BLUE)
        self.y += 30
        self.ascii.text(self.x, self.y, "Use ZQSD or the arrow keys to select something else", pyxel.COLOR_DARK_BLUE)
        self.y += 30
        self.ascii.text(self.x, self.y, "Press E or ESCAPE to close", pyxel.COLOR_DARK_BLUE)

        # Display a message if necessary
        if hasattr(self, "message"):
            self.y += 60
            self.ascii.text(self.x, self.y, self.message, self.color)

    def draw_hp(self, x, y) -> None:
        """
        Method that draws the hp on the window.
        """

        color = pyxel.COLOR_GREEN

        hp = self.player.skills["hp"]

        if hp > 7:
            color = pyxel.COLOR_GREEN
        elif hp > 5:
            color = pyxel.COLOR_YELLOW
        elif hp > 3:
            color = pyxel.COLOR_ORANGE
        else:
            color = pyxel.COLOR_RED

        self.ascii.text(x, y, f"HP: {hp}", color)