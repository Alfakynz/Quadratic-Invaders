import pyxel
import math
from characters import Character
from bullets import Bullets
from ascii import ASCII

class Player(Character):
    """
    Class that manages the player and inherits the characteristics of the class Character

    """
    def __init__(self,
                 color: int = 7, # white
                 shape: str = "triangle",
                 hp: int = 10, # health points
                 attack: int = 1, # amount of hp that the player removes to the enemies touched by a bullet
                 speed: int = 5, # speed at which the player moves (in cartesian coordinates)
                 shield: int = 0, # reduces the damage taken
                 fire_rate: int = 30, # number of frames counted each time a bullet is shot
                 xp: int = 0) -> None: # amount of experience points collected by the player
        """
        Initialize the class Player

        color: int
        shape : str
        hp: int
        attack: int
        speed: int
        shield: int
        fire_rate: int
        xp: int
        -> None
        """
        super().__init__(color, shape, hp, attack, speed, shield, fire_rate, xp)
        self.ascii: ASCII = ASCII()

        self.window_width: int = 0 # width of the window (given by the class Game)
        self.window_height: int = 0 # height of the window (given by the class Game)

        # player's starting position
        self.player_x: int = 500
        self.player_y: int = 375

        self.r: int = 20 # distance from the pole in polar coodinates (also size)
        self.took_damage: bool = False
        self.count: int = 0

        self.enemies_list: list[dict[float, float, bool, float, int, int, str, int, int, int, int, int, int]] = []
        self.enemies_damage: int = 0
        self.enemy_size: int = 0

        self.bullets: Bullets = Bullets(self.player_x, self.player_y) # creates the objet Bullets
        self.bullets.fire_rate = self.skills["fire_rate"] # gives the fire rate to the bullet

        return None

    def player_movements(self) -> bool:
        """
        Move the player according to the arrow keys pressed and stops it when it is about to go out of bounds

        takes no arguments -> bool
        """
        if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)) and self.player_x < self.window_width:
            self.player_x += self.skills["speed"] # moves to the right
            for enemy in self.enemies_list:
                if enemy["x"] <= self.player_x+self.r and enemy["y"] <= self.player_y+self.r and enemy["x"]+self.enemy_size >= self.player_x and enemy["y"]+self.enemy_size >= self.player_y:
                    self.player_x -= self.skills["speed"]
        if (pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q)) and self.player_x > 0:
            self.player_x -= self.skills["speed"] # moves to the left
            for enemy in self.enemies_list:
                if enemy["x"] <= self.player_x+self.r and enemy["y"] <= self.player_y+self.r and enemy["x"]+self.enemy_size >= self.player_x and enemy["y"]+self.enemy_size >= self.player_y:
                    self.player_x += self.skills["speed"]
        if (pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S)) and self.player_y < self.window_height:
            self.player_y += self.skills["speed"] # moves down
            for enemy in self.enemies_list:
                if enemy["x"] <= self.player_x+self.r and enemy["y"] <= self.player_y+self.r and enemy["x"]+self.enemy_size >= self.player_x and enemy["y"]+self.enemy_size >= self.player_y:
                    self.player_y -= self.skills["speed"]
        if (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z)) and self.player_y > 0:
            self.player_y -= self.skills["speed"] # moves up
            for enemy in self.enemies_list:
                if enemy["x"] <= self.player_x+self.r and enemy["y"] <= self.player_y+self.r and enemy["x"]+self.enemy_size >= self.player_x and enemy["y"]+self.enemy_size >= self.player_y:
                    self.player_y -= self.skills["speed"]
            

        return True

    def damage(self) -> bool:
        for enemy in self.enemies_list:
            if enemy["x"] <= self.player_x+self.r and enemy["y"] <= self.player_y+self.r and enemy["x"]+self.enemy_size >= self.player_x and enemy["y"]+self.enemy_size >= self.player_y and self.took_damage == False:
                self.skills["hp"] = self.receive_damage(self.enemies_damage, self.skills["hp"], self.skills["shield"])
                self.color = 13
                self.took_damage = True
            
            if self.took_damage == False:
                self.count = 0
            elif self.took_damage == True:
                self.count += 1

            if self.count >= 60 :
                self.color = 7
                self.took_damage = False
                
    def add_xp(self, amount: int) -> bool:
        self.xp += amount
        return True

    def update(self) -> bool:
        """
        Function that updates everything inside and is called infinitely in the class Game

        takes no arguments -> bool
        """

        self.player_movements() # moves the player

        self.damage()

        # gives the position of the player to the bullet
        self.bullets.player_x = self.player_x
        self.bullets.player_y = self.player_y

        # calculates the teta between the position of the mouse and the position of the player (polar coordinates)
        self.teta: float = self.teta_calculation((pyxel.mouse_x, pyxel.mouse_y), (self.player_x, self.player_y))
        self.bullets.teta = self.teta # gives teta to the bullet in order use it as the direction the bullet will move towards

        self.bullets.update(self.polar_to_cartesian) # updates the bullets

        return True

    def draw(self) -> bool:
        """
        Function that draws the objects on the window and is called infinitely in the class Game

        takes no arguments -> bool
        """

        # conversion of polar coordinates into cartesian coordinates for the vertex of the triangle that is orientated to the mouse
        p1: tuple[float, float] = self.polar_to_cartesian(self.teta, self.r)
        # conversion for the other vertexes of the triangle (with an offset of 3pi/4)
        p2: tuple[float, float] = self.polar_to_cartesian(self.teta, self.r, 3*math.pi/4)
        p3: tuple[float, float] = self.polar_to_cartesian(self.teta, self.r, -3*math.pi/4)

        # drawing of the triangle/player
        pyxel.tri(self.player_x + p1[0], self.player_y + p1[1],
                  self.player_x + p2[0], self.player_y + p2[1],
                  self.player_x + p3[0], self.player_y + p3[1],
                  self.color)
        
        self.bullets.draw() # draws the bullets

        self.draw_hp()

        return True
    
    def draw_hp(self):
        color = pyxel.COLOR_GREEN

        hp = self.skills["hp"]

        if hp > 7:
            color = pyxel.COLOR_GREEN
        elif hp > 5:
            color = pyxel.COLOR_YELLOW
        elif hp > 3:
            color = pyxel.COLOR_ORANGE
        else:
            color = pyxel.COLOR_RED

        self.ascii.text(25, 25, f"{self.skills["hp"]} HP", color)