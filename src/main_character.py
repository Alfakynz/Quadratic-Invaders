import pyxel
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

        self.mc_x = 500
        self.mc_y = 375

    def move(self):

        if pyxel.btn(pyxel.KEY_RIGHT) and self.mc_x<1000:
            self.mc_x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.mc_x>0:
            self.mc_x += -1
        if pyxel.btn(pyxel.KEY_DOWN) and self.mc_y<750:
            self.mc_y += 1
        if pyxel.btn(pyxel.KEY_UP) and self.mc_y>0:
            self.mc_y += -1

    def shoot(self):
        pass

    def add_xp(self, amount: int) -> None:
        self.xp += amount

    def update(self):
        self.move()

    def draw(self):
        #pyxel.tri(self.mc_x, self.mc_y, x2, y2, x3, y3, col)
        pass