from main_character import MainCharacter
from skills import Skill

class Upgrade:
    def __init__(self) -> None:
        self.upgrades = {
            "hp": Skill("hp", "Increase your health by 1", 25, 1),
            "attack": Skill("attack", "Increase your attack by 1", 10, 1),
            "shield": Skill("shield", "Increase your shield by 5", 50, 5),
            "speed": Skill("speed", "Increase your speed by 6", 5, 6),
            "speed_shoot": Skill("speed_shoot", "Increase your shooting speed by 2", 10, 2),
        }
        self.price_hp: int = 25
        self.price_attack: int = 10
        self.price_shield: int = 50
        self.price_speed: int = 5
        self.price_speed_shoot: int = 10

    def increase(self, skill: str, player: MainCharacter) -> None:
        if skill not in self.upgrades:
            print("Skill not found")
            return
        
        if player.xp < self.upgrades[skill].price:
            print("Insufficient XP")
            return
        
        upgrade = self.upgrades[skill]
        player.xp -= upgrade.price
        player.skills[skill] += upgrade.amount

        upgrade.price = int(upgrade.price * 1.5)