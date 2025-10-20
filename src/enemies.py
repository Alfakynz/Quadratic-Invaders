from characters import Character

class Enemy(Character):
    def __init__(self,
                 color: int,
                 shape: str,
                 hp: int,
                 damage: int,
                 speed: int,
                 shield: int,
                 shoot_speed: int,
                 xp: int) -> None:
        super().__init__(color, shape, hp, damage, speed, shield, shoot_speed, xp)

    def move(self):
        pass

    def collision(self):
        pass

    def attack(self):
        pass