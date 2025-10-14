from characters import Character

class Enemy(Character):
    def __init_(self, color: list[int], shape: str, hp: int, damage: int, speed: int, shield: int, speed_shoot: int):
        super().__init__(color, shape, hp, damage, speed, shieldn, speed_shoot, xp)

    def move(self):
        pass

    def collision(self):
        pass

    def attack(self):
        pass