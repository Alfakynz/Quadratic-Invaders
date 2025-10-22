import pyxel
from player import Player
from skills import Skill

class Upgrade:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.upgrades = {
            "hp": Skill("hp", "Increase your health by 1", 25, 1),
            "attack": Skill("attack", "Increase your attack by 1", 10, 1),
            "shield": Skill("shield", "Increase your shield by 5", 50, 5),
            "speed": Skill("speed", "Increase your speed by 1", 5, 1),
            "fire_rate": Skill("fire_rate", "Increase your bulleting speed by 2", 10, 2),
        }
        self.selected_index = 0
        self.skill_names = list(self.upgrades.keys())

    def increase(self, skill: str, player: Player) -> None:
        """
        Increase the selected skill of the player if he has enough XP
        
        skill: str
        player: Player
        -> None
        """
        if skill not in self.upgrades:
            print("Skill not found")
            return
        
        upgrade = self.upgrades[skill]

        if player.xp < upgrade.price:
            print("Insufficient XP")
            return
        
        player.xp -= upgrade.price
        player.skills[skill] += upgrade.amount

        upgrade.price = int(upgrade.price * 1.5)
        upgrade.level += 1

    def update(self) -> bool:
        """
        Handle user input to navigate and purchase upgrades

        takes no arguments -> True
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
        pyxel.text(10, 10, "=== Upgrade Menu ===", pyxel.COLOR_YELLOW)
        pyxel.text(10, 25, f"XP: {self.player.xp}", pyxel.COLOR_WHITE)

        y_position = 50

        # Display each upgrade option
        for i, skill_name in enumerate(self.skill_names):
            upgrade = self.upgrades[skill_name]
            color = pyxel.COLOR_LIME if i == self.selected_index else pyxel.COLOR_WHITE
            pyxel.text(20, y_position, f"{skill_name.capitalize()} (Level: {upgrade.level}): {upgrade.description} (Cost: {upgrade.price})", color)
            y_position += 12

        pyxel.text(10, y_position + 10, "Press ENTER to buy | E to close", pyxel.COLOR_DARK_BLUE)

        return