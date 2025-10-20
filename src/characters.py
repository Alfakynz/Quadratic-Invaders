class Character:
    def __init__(self,
                 color: int,
                 shape: str,
                 hp: int,
                 attack: int,
                 speed: int,
                 shield: int,
                 shoot_speed: int,
                 xp: int) -> None:
        self.color = color
        self.shape = shape
        self.xp = xp
        self.skills = {
            "hp": hp,
            "attack": attack,
            "shield": shield,
            "speed": speed,
            "shoot_speed": shoot_speed
        }

    def receive_damage(self, amount):
        self.skills["hp"] -= amount * (1 - self.skills["shield"] / 100)
        if self.skills["hp"] < 0:
            self.skills["hp"] = 0