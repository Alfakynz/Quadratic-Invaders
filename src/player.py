import pyxel
import math
from characters import Character
from bullets import Bullets
class Player(Character):
    """
    Class that manages the player and inherits the characteristics of the class Character

    """
    def __init__(self,
                 color: int = 7,
                 shape: str = "triangle",
                 hp: int = 10,
                 attack: int = 1,
                 speed: int = 5,
                 shield: int = 0,
                 shoot_speed: int = 30,
                 xp: int = 0) -> None:
        """
        Initialize the class Player

        color: int
        shape : str
        hp: int
        attack: int
        speed: int
        shield: int
        shoot_speed: int
        xp: int
        -> None
        """
        super().__init__(color, shape, hp, attack, speed, shield, shoot_speed, xp)


        self.color: int = color
        self.shape: str = shape
        self.hp: int = hp
        self.attack: int = attack
        self.speed: int = speed
        self.shield: int = shield
        self.shoot_speed: int = shoot_speed
        self.xp: int = xp

        # player's starting position
        self.player_x: int = 500
        self.player_y: int = 375

        self.r: int = 0 # distance from the pole in polar coodinates (used in the draw function)
        self.bullets = Bullets(self.player_x, self.player_y, self.r, self.shoot_speed)

    def move(self) -> None:
        """
        Move the player according to the arrow keys pressed and stops it when it is about to go out of bounds

        takes no arguments and returns None
        """
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x<1000:
            self.player_x += self.speed
        if pyxel.btn(pyxel.KEY_LEFT) and self.player_x>0:
            self.player_x -= self.speed
        if pyxel.btn(pyxel.KEY_DOWN) and self.player_y<750:
            self.player_y += self.speed
        if pyxel.btn(pyxel.KEY_UP) and self.player_y>0:
            self.player_y -= self.speed

    def add_xp(self, amount: int) -> None:
        self.xp += amount

    def update(self) -> None:
        """
        Function that updates everything inside and is called infinitely in the class Game

        takes no arguments and returns None
        """
        self.move() # moves the player
        self.bullets.player_x = self.player_x
        self.bullets.player_y = self.player_y
        self.bullets.update()

    def draw(self) -> None:
        """
        Function that draws the objects on the window and is called infinitely in the class Game

        takes no arguments and returns None
        """

        dx: int = pyxel.mouse_x - self.player_x # distance between x of mouse and x of player
        dy: int = pyxel.mouse_y - self.player_y # distance between y of mouse and y of player
        teta: float = math.atan2(dy, dx) # calculation of teta, direction from the pole relative to the direction of the polar axis

        self.r = 20 # distance from the pole

        p1: tuple = (math.cos(teta) * self.r, math.sin(teta) * self.r) # conversion of polar coordinates into cartesian coordinates for the vertex of the triangle that is orientated to the mouse
        # conversion for the other vertexes of the triangle
        p2: tuple = (math.cos(teta + 3*math.pi/4) * self.r, math.sin(teta + 3*math.pi/4) * self.r)
        p3: tuple = (math.cos(teta - 3*math.pi/4) * self.r, math.sin(teta - 3*math.pi/4) * self.r)

        # drawing of the triangle/player
        pyxel.tri(self.player_x + p1[0], self.player_y + p1[1],
                  self.player_x + p2[0], self.player_y + p2[1],
                  self.player_x + p3[0], self.player_y + p3[1],
                  self.color)
        
        self.bullets.draw()