class Upgrade:
    def __init__(self) -> None:
        self.price_hp: int = 25
        self.price_attack: int = 10
        self.price_shield: int = 50
        self.price_speed: int = 5
        self.price_speed_shoot: int = 10
        self.price_skills: int = 100

    def increase(self, skill: str) -> None:
        match skill:
            case "hp":
                self.price_hp = int(self.price_hp * 1.5)
            case "attack":
                self.price_attack = int(self.price_attack * 1.5)
            case "shield":
                self.price_shield = int(self.price_shield * 1.5)
            case "speed":
                self.price_speed = int(self.price_speed * 1.5)
            case "speed_shoot":
                self.price_speed_shoot = int(self.price_speed_shoot * 1.5)
            case "skills":
                self.price_skills = int(self.price_skills * 1.5)
            case _:
                print("Skill not found")
