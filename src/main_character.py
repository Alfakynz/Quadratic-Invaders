from characters import Character

class MainCharacter(Character):
    def __init_(self,
                color: list[int],
                shape: str,
                hp: int,
                damage: int,
                speed: int,
                shield: int,
                speed_shoot: int,
                xp: int) -> None:
        super().__init__(color, shape, hp, damage, speed, shield, speed_shoot, xp)

    def shoot(self) -> None:
        pass

    def add_xp(self, amount: int) -> None:
        self.xp += amount