import pyxel
import random
from characters import Character
from player import Player
from enemy import Enemy

class Enemies(Character):
    """
    Class that manages the enemies and inherits the characteristics of the class Character.
    """

    def __init__(self,
                 player: Player,
                 color: int = 4, # red
                 hp: int = 1, # health points
                 attack: int = 1, # amount of hp that the enemies remove to the player when they touch them
                 speed: int = 2, # speed at which the enemies move (r in polar coordinates)
                 shield: int = 0, # reduces the damage taken
                 fire_rate: int = 60, # number of frames counted each time a bullet is shot
                 xp: int = 10) -> None: # amount of experience points dropped by the enemies when killed
        """
        Initializes the class Enemies

        Args:
            color (int): Character color (not yet implemented).
            hp (int): Maximum health of the character.
            attack (int): Base attack damage the character can inflict.
            speed (int): Movement speed of the character.
            shield (int): Amount of damage the character can block before losing hp.
            fire_rate (int): Delay between attacks.
            xp (int): Experience points awarded when the character is defeated. 
        """

        super().__init__(color, hp, attack, speed, shield, fire_rate, xp) #calls the __init__ method of the parent class

        #initializes the attributes characterizing the Enemies class
        self.color: int = color
        self.hp: int = hp
        self.attack: int = attack
        self.speed: int = speed
        self.shield: int = shield
        self.fire_rate: int = fire_rate
        self.xp: int = xp

        self.window_width: int = 0 # width of the window (given by the class Game)
        self.window_height: int = 0 # height of the window (given by the class Game)

        self.enemies_array: list[Enemy] = [] # array where the coordinates of each enemy is stored
        self.creation_speed: int = 300 # number of frames counted each time time an enemy is created
        self.size: int = 40 # size of the enemies

        self.player: Player = player

        #initializes the attributes related to the player
        self.player_x: int = 0 # player's x position
        self.player_y: int = 0 # player's y position
        self.player_size: int = 0
        self.player_attack: int = 0

        #initializes the attributes related to the bullets
        self.bullets_array: list[list[float, float, float]] = []
        self.bullet_size: int = 0

    def enemies_creation(self) -> None:
        """"
        Creates an enemy on a random side of the map every time a specific amount of frames is counted.
        """

        side = random.randint(1, 4) # chooses a random side of the map
        if pyxel.frame_count % self.creation_speed == True:
            self.enemies_array.append({
                "x": 0,
                "y": 0,
                "reverse": False,
                "teta": 0,
                "count_player": 0,
                "count_bullet": 0,
                "bullet_touched": False,
                "color": self.color,
                "hp": self.hp,
                "attack": self.attack,
                "speed": self.speed,
                "shield": self.shield,
                "fire_rate": self.fire_rate,
                "xp": self.xp
            })
            
            if side == 1:
                # creates an enemy on the top side of the window
                self.enemies_array[-1]["x"] = random.randint(0, self.window_width - self.size)
            elif side == 2:
                # creates an enemy on the bottom side of the window
                self.enemies_array[-1]["x"] = random.randint(0, self.window_width - self.size)
                self.enemies_array[-1]["y"] = self.window_height - self.size
            elif side == 3:
                # creates an enemy on the left side of the window
                self.enemies_array[-1]["y"] = random.randint(0, self.window_height - self.size)
            elif side == 4:
                # creates an enemy on the right side of the window
                self.enemies_array[-1]["x"] = self.window_width - self.size
                self.enemies_array[-1]["y"] = random.randint(0, self.window_height - self.size)

    def enemies_movements(self) -> None:
        """
        Moves the enemies towards the player.
        """

        for enemy in self.enemies_array:
            # calculates the teta between the position of the player and the position of the enemy (polar coordinates)
            teta: float = self.teta_calculation((self.player_x, self.player_y), (enemy["x"], enemy["y"]))

            if enemy["reverse"] == True:
                #creates a repulsed effect when the enemy collides with the player
                enemy["x"] -= 2*self.polar_to_cartesian(enemy["teta"], self.speed)[0]
                enemy["y"] -= 2*self.polar_to_cartesian(enemy["teta"], self.speed)[1]
                enemy["count_player"] += 1
            elif enemy["reverse"] == False:
                # moves the enemy (with the help of a conversion of polar coordinates into cartesian coordinates)
                enemy["x"] += self.polar_to_cartesian(teta, self.speed)[0]
                enemy["y"] += self.polar_to_cartesian(teta, self.speed)[1]
                enemy["count_player"] = 0

    def player_collision(self):
        """
        Method that checks the collisions between enemies and the player.
        """

        for enemy in self.enemies_array:
            if enemy["x"] <= self.player_x+self.player_size and enemy["y"] <= self.player_y+self.player_size and enemy["x"]+self.size >= self.player_x and enemy["y"]+self.size >= self.player_y: #checks the collision
                enemy["reverse"] = True #turns on the repulse effect
                enemy["teta"] = self.teta_calculation((self.player_x, self.player_y), (enemy["x"], enemy["y"])) #saves the direction it was moving towards
            if enemy["reverse"] == True and enemy["count_player"] >= 30: #turns off the repulse effect after 0.5 seconds
                enemy["reverse"] = False

    def bullet_collision(self, player: Player):
        """
        Method that checks the collision between enemies and the bullets.
        """

        for enemy in self.enemies_array:
            for bullet in self.bullets_array:
                if enemy["x"] <= bullet[0]+self.bullet_size and enemy["y"] <= bullet[1]+self.bullet_size and enemy["x"]+self.size >= bullet[0] and enemy["y"]+self.size >= bullet[1]: #checks the collision
                    enemy["hp"] = self.receive_damage(self.player_attack, enemy["hp"], enemy["shield"]) #damages the enemy
                    enemy["color"] = 2 #turns the enemy purple to show that he took some damage
                    enemy["bullet_touched"] = True #shows that the enemy collided with a bullet
                    if enemy["hp"] == 0:
                        self.enemies_array.remove(enemy) #removes the enemy from the array when he dies
                        player.add_xp(enemy["xp"]) #gives the amount of xp that the enemy dropped when he died to the player
                
                if enemy["bullet_touched"] == False:
                    enemy["count_bullet"] = 0 #puts the counter back to 0 when the enemy does not collide with a bullet

                if enemy["bullet_touched"] == True:
                    enemy["count_bullet"] += 1 #counts the number of frames since enemy collided a bullet

                if enemy["bullet_touched"] == True and enemy["count_bullet"] >= 15: #checks if 0.25 secondes have passed since the enemy touched a bullet
                    enemy["color"] = 4 #turns back the enemy to red
                    enemy["bullet_touched"] = False #shows that it had been 0.25 seconds since the enemy had not collided with a bullet


    def update(self, player_x: int, player_y: int, player_size: int, player_attack: int, bullets_array: list[list[float, float, float]], bullet_size: int, window_width: int, window_height: int) -> None:
        """
        Method that updates everything inside and is called infinitely in the class Game.

        Args:
            player_x (int): X position of the player.
            player_y (int): Y position of the player.
            player_size (int): Size of the player.
            player_attack (int): Amount of hp that the player removes to an enemy when a bullet collides with them.
            bullets_array (list[list[float, float, float]]): Array containing the bullets shot and still in the window.
            bullet_size (int): Size of the bullets.
            window_width (int): Width of the window.
            window_height (int): Height of the window.
        """

        #updates the attributes related to the player
        self.player_x = player_x
        self.player_y = player_y
        self.player_size = player_size
        self.player_attack = player_attack

        #updates the attributes related to the bullets
        self.bullets_array = bullets_array
        self.bullet_size = bullet_size

        #updates the attributes related to the window
        self.window_width = window_width
        self.window_height = window_height

        self.enemies_creation() # creates enemies
        self.enemies_movements() # moves enemies
        self.player_collision() #checks the collision with the player
        self.bullet_collision(self.player) #checks the collision with the bullets

    def draw(self) -> None:
        """
        Method that draws the enemies on the window and is called infinitely in the class Game.
        """

        for enemy in self.enemies_array:
            pyxel.rect(enemy["x"], enemy["y"], self.size, self.size, enemy["color"]) # draws enemies/squares