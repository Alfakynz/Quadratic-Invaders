import pyxel
from player import Player
from skills import Skill
from ascii import ASCII

class Upgrade:
    """
    Class that displays the menu
    """
    def __init__(self, player: Player) -> None:
        self.player = player
        self.upgrades = {
            "hp": Skill("hp", "Increase your health by 1", 25, 1),
            "attack": Skill("attack", "Increase your attack by 1", 10, 1),
            "shield": Skill("shield", "Increase your shield by 5", 50, 5),
            "speed": Skill("speed", "Increase your speed by 1", 5, 1),
            "fire_rate": Skill("fire rate", "Increase your bulleting speed by 2", 10, 2),
        }
        self.ascii: ASCII = ASCII()
        self.x: int = 25
        self.y: int = 25
        self.color: int = pyxel.COLOR_GREEN
        self.selected_index: int = 0
        self.skill_names: list = list(self.upgrades.keys())

    def increase(self, skill: str, player: Player) -> None:
        """
        Increase the selected skill of the player if he has enough XP
        
        skill: str
        player: Player
        -> None
        """
        # Skill not found
        if skill not in self.upgrades:
            self.message = "Skill not found"
            self.color = pyxel.COLOR_RED
            return
        
        upgrade = self.upgrades[skill]

        # Insufficient XP
        if player.xp < upgrade.price:
            self.message = "Insufficient XP"
            self.color = pyxel.COLOR_RED
            return
        
        player.xp -= upgrade.price
        player.skills[skill] += upgrade.amount

        upgrade.price = int(upgrade.price * 1.5)
        upgrade.level += 1

        self.message = f"{skill.capitalize()} upgraded to level {upgrade.level}"
        self.color = pyxel.COLOR_LIGHT_BLUE
        return

    def update(self) -> bool:
        """
        Handle user input to navigate and purchase upgrades

        takes no arguments -> bool
        """

        # Navigate the upgrade menu
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            self.selected_index = (self.selected_index + 1) % len(self.skill_names)
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_Z):
            self.selected_index = (self.selected_index - 1) % len(self.skill_names)

        # Purchase the selected upgrade
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_KP_ENTER):
            selected_skill = self.skill_names[self.selected_index]
            self.increase(selected_skill, self.player)

        return True
    
    def draw(self) -> None:
        """
        Draw the upgrade menu

        takes no arguments -> None
        """
        pyxel.cls(0)
        self.y = 25
        self.ascii.text(self.x, self.y, "--- Upgrade Menu ---", pyxel.COLOR_YELLOW)
        self.y += 30
        self.ascii.text(self.x, self.y, f"XP: {self.player.xp}", pyxel.COLOR_WHITE)

        self.y += 60

        # Display each upgrade option
        for i, skill_name in enumerate(self.skill_names):
            upgrade = self.upgrades[skill_name]
            color = pyxel.COLOR_LIME if i == self.selected_index else pyxel.COLOR_WHITE
            self.ascii.text(20, self.y, f"{upgrade.name} Lv.{upgrade.level}: {upgrade.description} ({upgrade.price})"
, color)
            self.y += 30

        self.y += 30
        self.ascii.text(self.x, self.y, "Press ENTER to buy or press E to close", pyxel.COLOR_DARK_BLUE)

        # Display a message if necessary
        if hasattr(self, "message"):
            self.y += 60
            self.ascii.text(self.x, self.y, self.message, self.color)

        return