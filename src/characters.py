class Character:
    def __init__(self, color: list[int], shape: str, hp: int, attack: int, speed: int, shield: int, speed_shoot: int, xp: int) -> None:
        self.color = color
        self.shape = shape
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.shield = shield
        self.speed_shoot = speed_shoot
        self.xp = xp

    def receive_damage(self, amount):
        self.hp -= amount * (1 - self.shield / 100)
        if self.hp < 0:
            self.hp = 0