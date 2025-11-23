import pyxel
from typing import Callable
from enemy import Enemy

class Bullets:
    """
    Class that manages the bullets shot by the player.
    """

    def __init__(self, player_x: int, player_y: int) -> None:
        """
        Initializes the class Bullet.

        Args:
            player_x (int): Player x position.
            player_y (int): Player y position.
        """

        self.player_x: int = player_x # player's x position
        self.player_y: int = player_y # player's y position

        #initializes the attributes related to the enemies
        self.enemies_array: list[Enemy] = []
        self.ENEMY_SIZE: int = 0

        #initializes the attributes related to the window
        self.WINDOW_WIDTH = 0 
        self.WINDOW_HEIGHT = 0

        #initializes the attributes related to the window
        self.fire_rate: int = 0 # number of frames counted each time a bullet is shot
        self.teta: float = 0 # value of teta between the position of the mouse and the position of the player (calculated in the method update of the class Player)

        self.BULLET_SPEED: int = 10 # speed of the bullet (also r in polar coordinates)
        self.SIZE: int = 10 # size of the bullet/circle
        self.COLOR: int = 10 # yellow
        self.bullets_array: list[list[float]] = [] # array containing the coordinates and the direction of each bullet
        self.count: int = 0 #initializes the counter used in bullets_creation
        self.can_shoot: bool = True 

    def bullets_creation(self) -> None:
        """
        Creates bullets every time a specific amount of frames is counted and when left click is continuously pressed.
        """
        self.count += 1

        if self.count >= 60:
            self.can_shoot = True
        
        if self.can_shoot == True:
            self.count = 0

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.count % self.fire_rate == 0 and self.can_shoot == True:
            self.bullets_array.append([self.player_x, self.player_y, self.teta]) # adds to bullets_array an array containing the coordinates and the direction of the bullet
            self.can_shoot = False

    def bullets_movements(self, polar_to_cartesian: Callable) -> None:
        """
        Moves the bullet towards the place the mouse clicked and removes it when it goes out of bounds.

        Args:
            polar_to_cartesian (Callable): A Callable function that converts polar coordinates into cartesian coordinates.
        """

        for bullet in self.bullets_array:
            # moves the bullet (with the help of a conversion of polar coordinates into cartesian coordinates)
            bullet[0] += polar_to_cartesian(bullet[2], self.BULLET_SPEED)[0]
            bullet[1] += polar_to_cartesian(bullet[2], self.BULLET_SPEED)[1]
            if  bullet[0] < 0 - self.SIZE or bullet[0] > self.WINDOW_WIDTH + self.SIZE or bullet[1] < 0 - self.SIZE or bullet[1] > self.WINDOW_HEIGHT + self.SIZE:
                self.bullets_array.remove(bullet) #removes the bullet when it goes out of bounds

    def update(self, polar_to_cartesian: Callable, enemies_array: list[Enemy], enemies_size: int, window_width: int, window_height: int, fire_rate: int, teta: float) -> None:
        """
        Method that updates everything inside and is called infinitely in the class Player.

        Args:
            polar_to_cartesian (Callable): A callable function
            enemies_array (list[Enemy]): Array containing the enemies created and still alive.
            enemies_size (int): Size of the enemies.
            window_width (int): Width of the window.
            window_height (int): Height of the window.
            fire_rate (int): Number of frames counted each time a bullet is shot.
            teta (float): value of teta between the position of the mouse and the position of the player
        """

        #updates the attributes related to the enemies
        self.enemies_array = enemies_array
        self.ENEMY_SIZE = enemies_size

        #updates the attributes related to the window
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height

        #updates the attributes related to the bullets
        self.fire_rate = fire_rate
        self.teta = teta

        self.bullets_creation() # creates bullets
        self.bullets_movements(polar_to_cartesian) # moves bullets

    def draw(self) -> None:
        """
        Method that draws the bullets on the window and is called infinitely in the class Player.
        """

        for bullet in self.bullets_array:
            pyxel.circ(bullet[0], bullet[1], self.SIZE, self.COLOR) # draws bullets/circles
