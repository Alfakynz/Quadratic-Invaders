from characters import Character

class MainCharacter(Character):
    def __init_(self, color: list[int], shape: str, hp: int, damage: int, speed: int, shield: int, speed_shoot: int):
        super().__init__(color, shape, hp, damage, speed, shieldn, speed_shoot, xp)

    def shoot(self):
        pass

    def add_xp(self, amount: int):
        self.xp += amount