import pyxel
from typing import Callable
from enemy import Enemy

class Bullets:
    """
    Class that manages the bullets shot by the player
    """

    def __init__(self, player_x: int, player_y: int) -> None:
        """
        Initializes the class Bullet

        player_x: int
        player_y: int
        -> None
        """

        self.player_x: int = player_x # player's x position
        self.player_y: int = player_y # player's y position

        self.enemies_list: list[Enemy] = []
        self.enemy_size: int = 0

        self.window_width = 0 # width of the window (given by the class Game)
        self.window_height = 0 # height of the window (given by the class Game)
        self.fire_rate: int = 0 # number of frames counted each time a bullet is shot
        self.teta: float = 0 # value of teta between the position of the mouse and the position of the player (calculated in the function update of the class Player)

        self.bullet_speed: int = 10 # speed of the bullet (also r in polar coordinates)
        self.size: int = 10 # size of the bullet/circle
        self.color: int = 10 # yellow
        self.bullets_list: list[list[float]] = [] # list where the coordinates and the direction of each bullet is stored

    def bullets_creation(self) -> bool:
        """
        Creates bullets every time a specific amount of frames is counted and when left click is continuously pressed

        takes no arguments -> bool
        """

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and pyxel.frame_count % self.fire_rate == True:
            self.bullets_list.append([self.player_x, self.player_y, self.teta]) # adds to bullets_list a list of the coordinates and the direction of the bullet

        return True

    def bullets_movements(self, polar_to_cartesian: Callable) -> bool:
        """
        Moves the bullet towards the place the mouse clicked and removes it when it goes out of bounds

        polar_to_cartesian: callable (function) -> bool
        """

        for bullet in self.bullets_list:
            # moves the bullet (with the help of a conversion of polar coordinates into cartesian coordinates)
            bullet[0] += polar_to_cartesian(bullet[2], self.bullet_speed)[0]
            bullet[1] += polar_to_cartesian(bullet[2], self.bullet_speed)[1]
            if  bullet[0] < 0 - self.size or bullet[0] > self.window_width + self.size or bullet[1] < 0 - self.size or bullet[1] > self.window_height + self.size:
                self.bullets_list.remove(bullet) #removes the bullet when it goes out of bounds

        return True
    
    def enemy_collision(self):
        for enemy in self.enemies_list:
            for bullet in self.bullets_list:
                if enemy["x"] <= bullet[0] + self.size and enemy["y"] <= bullet[1] + self.size and enemy["x"] + self.enemy_size >= bullet[0] and enemy["y"] + self.enemy_size >= bullet[1]:
                    self.bullets_list.remove(bullet)

    def update(self, polar_to_cartesian: Callable) -> bool:
        """
        Function that updates everything inside and is called infinitely in the class Player

        polar_to_cartesian: callable (function) -> bool
        """

        self.bullets_creation() # creates bullets
        self.bullets_movements(polar_to_cartesian) # moves bullets
        #self.enemy_collision()

        return True

    def draw(self) -> bool:
        """
        Function that draws the bullets on the window and is called infinitely in the class Player

        takes no arguments -> bool
        """

        for bullet in self.bullets_list:
            pyxel.circ(bullet[0], bullet[1], self.size, self.color) # draws bullets/circles

        return True
