class Character:
    def __init__(self, color: list[int], shape: str, hp: int, damage: int, speed: int, shield: int, speed_shoot: int, xp: int):
        self.color = color
        self.shape = shape
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.shield = shield
        self.speed_shoot = speed_shoot
        self.xp = xp

    def move(self):
        pass

    def receive_damage(self, amount):
        self.hp -= amount