import pyxel
from characters import Character

class Enemies(Character):
    def __init__(self,
                 color: int = 8,
                 shape: str = "square",
                 hp: int = 10,
                 damage: int = 1,
                 speed: int = 5,
                 shield: int = 0,
                 shoot_speed: int = 10,
                 xp: int = 0) -> None:
        super().__init__(color, shape, hp, damage, speed, shield, shoot_speed, xp)

    def move(self):
        pass

    def collision(self):
        pass

    def attack(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass