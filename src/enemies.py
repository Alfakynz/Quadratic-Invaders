import pyxel
import random
from characters import Character

class Enemies(Character):
    """
    Class that manages the enemies and inherits the characteristics of the class Character
    """
    def __init__(self,
                 color: int = 8, # pink
                 shape: str = "square",
                 hp: int = 1, # health points
                 damage: int = 1, # amount of hp that the enemies remove to the player when they touch them
                 speed: int = 2, # speed at which the enemies move (r in polar coordinates)
                 shield: int = 0, # reduces the damage taken
                 fire_rate: int = 60, # number of frames counted each time a bullet is shot
                 xp: int = 0) -> None: # amount of experience points dropped by the enemies when killed
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

        self.enemies_list: list[list[float]] = [] # list where the coordinates of each enemy is stored
        self.creation_speed: int = 300 # number of frames counted each time time an enemy is created
        self.size: int = 40 # size of the enemies
        self.player_x: int = 0 # player's x position
        self.player_y: int = 0 # player's y position

    def enemies_creation(self) -> bool:
        """"
        Creates an enemy on a random side of the map every time a specific amount of frames is counted

        takes no arguments -> True
        """

        side = random.randint(1, 4) # chooses a random side of the map
        if pyxel.frame_count % self.creation_speed == True:
            if side == 1:
                self.enemies_list.append([random.randint(0, self.window_width - self.size), 0]) # creates an enemy on the top side of the window
            elif side == 2:
                self.enemies_list.append([random.randint(0, self.window_width - self.size), self.window_height - self.size]) # creates an enemy on the bottom side of the window
            elif side == 3:
                self.enemies_list.append([0, random.randint(0, self.window_height - self.size)]) # creates an enemy on the left side of the window
            elif side == 4:
                self.enemies_list.append([self.window_width - self.size, random.randint(0, self.window_height - self.size)]) # creates an enemy on the right side of the window

        return True

    def enemies_movements(self) -> bool:
        """
        Moves the enemies towards the player

        takes no arguments -> True
        """

        for enemy in self.enemies_list:
            # calculates the teta between the position of the player and the position of the enemy (polar coordinates)
            teta: float = self.teta_calculation((self.player_x, self.player_y), (enemy[0], enemy[1]))

            # moves the enemy (with the help of a conversion of polar coordinates into cartesian coordinates)
            enemy[0] += self.polar_to_cartesian(teta, self.speed)[0]
            enemy[1] += self.polar_to_cartesian(teta, self.speed)[1]

        return True

    def collision(self):
        pass

    def attack(self):
        pass

    def update(self) -> bool:
        """
        Function that updates everything inside and is called infinitely in the class Game

        takes no arguments -> True
        """

        self.enemies_creation() # creates enemies
        self.enemies_movements() # moves enemies

        return True

    def draw(self) -> bool:
        """
        Function that draws the enemies on the window and is called infinitely in the class Game

        takes no arguments -> True
        """

        for enemy in self.enemies_list:
            pyxel.rect(enemy[0], enemy[1], self.size, self.size, self.color) # draws enemies/squares

        return True