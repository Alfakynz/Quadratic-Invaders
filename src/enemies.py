import pyxel
import random
from characters import Character
from player import Player
from enemy import Enemy

class Enemies(Character):
    """
    Class that manages the enemies and inherits the characteristics of the class Character
    """

    def __init__(self,
                 player: Player,
                 color: int = 4, # red
                 shape: str = "square",
                 hp: int = 1, # health points
                 damage: int = 1, # amount of hp that the enemies remove to the player when they touch them
                 speed: int = 2, # speed at which the enemies move (r in polar coordinates)
                 shield: int = 0, # reduces the damage taken
                 fire_rate: int = 60, # number of frames counted each time a bullet is shot
                 xp: int = 10) -> None: # amount of experience points dropped by the enemies when killed
        """
        Initializes the class Enemies

        color: int
        shape: str
        hp: int
        damage: int
        speed: int
        shield: int
        fire_rate: int
        xp: int
        -> None
        """

        super().__init__(color, shape, hp, damage, speed, shield, fire_rate, xp)

        self.color: int = color
        self.shape: str = shape
        self.hp: int = hp
        self.damage: int = damage
        self.speed: int = speed
        self.shield: int = shield
        self.fire_rate: int = fire_rate
        self.xp: int = xp

        self.window_width: int = 0 # width of the window (given by the class Game)
        self.window_height: int = 0 # height of the window (given by the class Game)

        self.enemies_list: list[Enemy] = [] # list where the coordinates of each enemy is stored
        self.creation_speed: int = 300 # number of frames counted each time time an enemy is created
        self.size: int = 40 # size of the enemies

        self.player: Player = player
        self.player_x: int = 0 # player's x position
        self.player_y: int = 0 # player's y position
        self.player_size: int = 0
        self.player_attack: int = 0

        self.bullets_list: list[list[float]] = []
        self.bullet_size: int = 0

    def enemies_creation(self) -> bool:
        """"
        Creates an enemy on a random side of the map every time a specific amount of frames is counted

        takes no arguments -> bool
        """

        side = random.randint(1, 4) # chooses a random side of the map
        if pyxel.frame_count % self.creation_speed == True:
            self.enemies_list.append({
                "x": 0,
                "y": 0,
                "reverse": False,
                "teta": 0,
                "count": 0,
                "color": self.color,
                "shape": self.shape,
                "hp": self.hp,
                "damage": self.damage,
                "speed": self.speed,
                "shield": self.shield,
                "fire_rate": self.fire_rate,
                "xp": self.xp
            })
            
            if side == 1:
                # creates an enemy on the top side of the window
                self.enemies_list[-1]["x"] = random.randint(0, self.window_width - self.size)
            elif side == 2:
                # creates an enemy on the bottom side of the window
                self.enemies_list[-1]["x"] = random.randint(0, self.window_width - self.size)
                self.enemies_list[-1]["y"] = self.window_height - self.size
            elif side == 3:
                # creates an enemy on the left side of the window
                self.enemies_list[-1]["y"] = random.randint(0, self.window_height - self.size)
            elif side == 4:
                # creates an enemy on the right side of the window
                self.enemies_list[-1]["x"] = self.window_width - self.size
                self.enemies_list[-1]["y"] = random.randint(0, self.window_height - self.size)

        return True

    def enemies_movements(self) -> bool:
        """
        Moves the enemies towards the player

        takes no arguments -> bool
        """

        for enemy in self.enemies_list:
            # calculates the teta between the position of the player and the position of the enemy (polar coordinates)
            teta: float = self.teta_calculation((self.player_x, self.player_y), (enemy["x"], enemy["y"]))

            if enemy["reverse"] == True:
                enemy["x"] -= 2*self.polar_to_cartesian(enemy["teta"], self.speed)[0]
                enemy["y"] -= 2*self.polar_to_cartesian(enemy["teta"], self.speed)[1]
                enemy["count"] += 1
            elif enemy["reverse"] == False:
                # moves the enemy (with the help of a conversion of polar coordinates into cartesian coordinates)
                enemy["x"] += self.polar_to_cartesian(teta, self.speed)[0]
                enemy["y"] += self.polar_to_cartesian(teta, self.speed)[1]
                enemy["count"] = 0

        return True

    def player_collision(self):
        for enemy in self.enemies_list:
            if enemy["x"] <= self.player_x+self.player_size and enemy["y"] <= self.player_y+self.player_size and enemy["x"]+self.size >= self.player_x and enemy["y"]+self.size >= self.player_y:
                enemy["reverse"] = True
                enemy["teta"] = self.teta_calculation((self.player_x, self.player_y), (enemy["x"], enemy["y"]))
            if enemy["reverse"] == True and enemy["count"] >= 30:
                enemy["reverse"] = False

    def bullet_collision(self, player: Player):
        for enemy in self.enemies_list:
            for bullet in self.bullets_list:
                if enemy["x"] <= bullet[0]+self.bullet_size and enemy["y"] <= bullet[1]+self.bullet_size and enemy["x"]+self.size >= bullet[0] and enemy["y"]+self.size >= bullet[1]:
                    enemy["hp"] = self.receive_damage(self.player_attack, enemy["hp"], enemy["shield"])
                    enemy["color"] = 2
                    if enemy["hp"] == 0:
                        self.enemies_list.remove(enemy)
                        player.add_xp(enemy["xp"])
                if pyxel.frame_count%15 == 0:
                    enemy["color"] = 4


    def update(self) -> bool:
        """
        Function that updates everything inside and is called infinitely in the class Game

        takes no arguments -> bool
        """

        self.enemies_creation() # creates enemies
        self.enemies_movements() # moves enemies
        self.player_collision()
        self.bullet_collision(self.player)

        return True

    def draw(self) -> bool:
        """
        Function that draws the enemies on the window and is called infinitely in the class Game

        takes no arguments -> bool
        """

        for enemy in self.enemies_list:
            pyxel.rect(enemy["x"], enemy["y"], self.size, self.size, enemy["color"]) # draws enemies/squares

        return True