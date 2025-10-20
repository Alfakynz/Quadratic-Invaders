import pyxel
import math
from characters import Character

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
                 shoot_speed: int = 15,
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

        self.color = color
        self.shape = shape
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.shield = shield
        self.shoot_speed = shoot_speed
        self.xp = xp

        # player's starting position
        self.player_x = 500
        self.player_y = 375

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

    def shoot(self) -> None:
        pass

    def add_xp(self, amount: int) -> None:
        self.xp += amount

    def update(self) -> None:
        """
        Function that updates everything inside and is called infinitely in the class Game

        takes no arguments and returns None
        """
        self.move() # moves the player

    def draw(self) -> None:
        """
        Function that draws the objects on the window and is called infinitely in the class Game

        takes no arguments and returns None
        """
        dx = pyxel.mouse_x - self.player_x # distance between x of mouse and x of player
        dy = pyxel.mouse_y - self.player_y # distance between y of mouse and y of player
        teta = math.atan2(dy, dx) # calculation of teta, direction from the pole relative to the direction of the polar axis

        r = 20 # distance from the pole

        p1 = (math.cos(teta) * r, math.sin(teta) * r) # conversion of polar coordinates into cartesian coordinates for the vertex of the triangle that is orientated to the mouse
        # conversion for the other vertexes of the triangle
        p2 = (math.cos(teta + 3*math.pi/4) * r, math.sin(teta + 3*math.pi/4) * r)
        p3 = (math.cos(teta - 3*math.pi/4) * r, math.sin(teta - 3*math.pi/4) * r)

        # drawing of the triangle/player
        pyxel.tri(self.player_x + p1[0], self.player_y + p1[1],
                  self.player_x + p2[0], self.player_y + p2[1],
                  self.player_x + p3[0], self.player_y + p3[1],
                  self.color)