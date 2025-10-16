class Upgrade:
    def __init__(self, 
                 price_pv: int,
                 price_attack: int,
                 price_shield: int,
                 price_speed: int,
                 price_speed_shoot: int,
                 price_skills: int
                 ) -> None:
        self.price_pv = price_pv
        self.price_attack = price_attack
        self.price_shield = price_shield
        self.price_speed = price_speed
        self.price_speed_shoot = price_speed_shoot
        self.price_skills = price_skills

    def increase(self, skill):
        pass