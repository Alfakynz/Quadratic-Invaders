from characters import Character

class MainCharacter(Character):
    def __init__(self,
                color: list[int] = [255, 255, 255],
                shape: str = "triangle",
                hp: int = 10,
                attack: int = 1,
                speed: int = 5,
                shield: int = 0,
                speed_shoot: int = 15,
                xp: int = 0) -> None:
        super().__init__(color, shape, hp, attack, speed, shield, speed_shoot, xp)

    def shoot(self) -> None:
        pass

    def add_xp(self, amount: int) -> None:
        self.xp += amount