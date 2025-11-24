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
                 hp_max: int = 1, # max health points
                 attack: int = 1, # amount of hp that the enemies remove to the player when they touch them
                 speed: int = 2, # speed at which the enemies move (r in polar coordinates)
                 shield: int = 0, # reduces the damage taken
                 fire_rate: int = 60, # number of frames counted each time a bullet is shot
                 xp: int = 1) -> None: # amount of experience points dropped by the enemies when killed
        """
        Initializes the class Enemies

        Args:
            color (int): Character color (not yet implemented).
            hp (int): Current health of the character.
            hp_max (int): Maximum health of the character.
            attack (int): Base attack damage the character can inflict.
            speed (int): Movement speed of the character.
            shield (int): Amount of damage the character can block before losing hp.
            fire_rate (int): Delay between attacks.
            xp (int): Experience points awarded when the character is defeated. 
        """

        super().__init__(color, hp, hp_max, attack, speed, shield, fire_rate, xp) #calls the __init__ method of the parent class

        #initializes the attributes characterizing the Enemies class
        self.color: int = color
        self.hp: int = hp
        self.hp_max: int = hp_max
        self.attack: int = attack
        self.speed: int = speed
        self.shield: int = shield
        self.fire_rate: int = fire_rate
        self.xp: int = xp

        self.WINDOW_WIDTH: int = 0 # width of the window (given by the class Game)
        self.WINDOW_HEIGHT: int = 0 # height of the window (given by the class Game)

        self.enemies_array: list[Enemy] = [] # array where the coordinates of each enemy is stored
        self.creation_speed: int = 180 # initializes the number of frames counted each time an enemy is created
        self.SIZE: int = 40 # size of the enemies

        self.UPGRADE_SPEED: int = 900 #number of frames counted each time an enemy is upgraded
        self.upgrades_order: str = "creation_speed" #puts the creation speed as the first skill to be upgraded 
        self.upgrades: dict[str, int] = {"creation_speed": self.creation_speed, "speed": self.speed, "hp": self.hp, "attack": self.attack, "shield": self.shield} #skills that can be upgraded

        self.player: Player = player

        #initializes the attributes related to the player
        self.player_x: int = 0 # player's x position
        self.player_y: int = 0 # player's y position
        self.PLAYER_SIZE: int = 0
        self.player_attack: int = 0

        #initializes the attributes related to the bullets
        self.bullets_array: list[list[float]] = []
        self.BULLET_SIZE: int = 0

    def enemies_creation(self) -> None:
        """"
        Creates an enemy on a random side of the map every time a specific amount of frames is counted.
        """

        side = random.randint(1, 4) # chooses a random side of the map
        if pyxel.frame_count % self.upgrades["creation_speed"] == 0: #creates an enemy every given frames
            self.enemies_array.append({
                "x": 0,
                "y": 0,
                "reverse": False,
                "teta": 0,
                "count_bullet": 0,
                "bullet_touched": False,
                "color": self.color,
                "hp": self.upgrades["hp"],
                "attack": self.upgrades["attack"],
                "speed": self.upgrades["speed"],
                "shield": self.upgrades["shield"],
                "fire_rate": self.fire_rate,
                "xp": self.xp,
                "knockback_speed": 0.0
            }) #creates the characteristics of the enemy
            
            if side == 1:
                # creates an enemy on the top side of the window
                self.enemies_array[-1]["x"] = random.randint(0, self.WINDOW_WIDTH - self.SIZE)
            elif side == 2:
                # creates an enemy on the bottom side of the window
                self.enemies_array[-1]["x"] = random.randint(0, self.WINDOW_WIDTH - self.SIZE)
                self.enemies_array[-1]["y"] = self.WINDOW_HEIGHT - self.SIZE
            elif side == 3:
                # creates an enemy on the left side of the window
                self.enemies_array[-1]["y"] = random.randint(0, self.WINDOW_HEIGHT - self.SIZE)
            elif side == 4:
                # creates an enemy on the right side of the window
                self.enemies_array[-1]["x"] = self.WINDOW_WIDTH - self.SIZE
                self.enemies_array[-1]["y"] = random.randint(0, self.WINDOW_HEIGHT - self.SIZE)

    def enemies_movements(self) -> None:
        """
        Moves the enemies towards the player.
        """

        for enemy in self.enemies_array:
            # calculates the teta between the position of the player and the position of the enemy (polar coordinates)
            teta_to_player: float = self.teta_calculation((self.player_x, self.player_y), (enemy["x"], enemy["y"]))

            if enemy["reverse"] == True:
                #creates a knockback effect when the enemy collides with the player
                enemy["x"] -= self.polar_to_cartesian(teta_to_player, enemy["knockback_speed"])[0]
                enemy["y"] -= self.polar_to_cartesian(teta_to_player, enemy["knockback_speed"])[1]
                
                enemy["knockback_speed"] *= 0.85 #creates friction

                if enemy["knockback_speed"] < enemy["speed"] * 0.5: #stops the knockback effect when the knockback_speed is about to be normal again
                    enemy["reverse"] = False #turns off the knockback effect
                    enemy["knockback_speed"] = 0.0 #resets the knockback_speed

            elif enemy["reverse"] == False:
                # moves the enemy (with the help of a conversion of polar coordinates into cartesian coordinates)
                enemy["x"] += self.polar_to_cartesian(teta_to_player, enemy["speed"])[0]
                enemy["y"] += self.polar_to_cartesian(teta_to_player, enemy["speed"])[1]

    def player_collision(self) -> None:
        """
        Method that checks the collisions between enemies and the player.
        """

        for enemy in self.enemies_array:
            if enemy["x"] <= self.player_x+self.PLAYER_SIZE and enemy["y"] <= self.player_y+self.PLAYER_SIZE and enemy["x"]+self.SIZE >= self.player_x and enemy["y"]+self.SIZE >= self.player_y: #checks the collision
                if not enemy["reverse"]: #makes sure the knockback is not reactivated when it is already turned on
                    enemy["reverse"] = True #turns on the knockback effect
                    enemy["teta"] = self.teta_calculation((self.player_x, self.player_y), (enemy["x"], enemy["y"])) #saves the direction it was moving towards
                    enemy["knockback_speed"] = enemy["speed"] * 5 #knockback power

    def bullet_collision(self, player: Player) -> None:
        """
        Method that checks the collision between enemies and the bullets.
        """

        for enemy in self.enemies_array:
            for bullet in self.bullets_array[:]: #goes throught a copy of the array
                if enemy["x"] <= bullet[0]+self.BULLET_SIZE and enemy["y"] <= bullet[1]+self.BULLET_SIZE and enemy["x"]+self.SIZE >= bullet[0] and enemy["y"]+self.SIZE >= bullet[1]: #checks the collision
                    self.bullets_array.remove(bullet)
                    enemy["hp"] = self.receive_damage(self.player_attack, enemy["hp"], enemy["shield"]) #damages the enemy
                    enemy["color"] = 2 #turns the enemy purple to show that he took some damage
                    enemy["bullet_touched"] = True #shows that the enemy collided with a bullet
                    if enemy["hp"] == 0:
                        self.enemies_array.remove(enemy) #removes the enemy from the array when he dies
                        player.add_xp(enemy["xp"]) #gives the amount of xp that the enemy dropped when he died to the player
                        break
            if enemy["bullet_touched"] == False:
                enemy["count_bullet"] = 0 #puts the counter back to 0 when the enemy does not collide with a bullet

            if enemy["bullet_touched"] == True:
                enemy["count_bullet"] += 1 #counts the number of frames since enemy collided a bullet

            if enemy["bullet_touched"] == True and enemy["count_bullet"] >= 15: #checks if 0.25 secondes have passed since the enemy touched a bullet
                enemy["color"] = 4 #turns back the enemy to red
                enemy["bullet_touched"] = False #shows that it had been 0.25 seconds since the enemy had not collided with a bullet

    def enemies_upgrade(self, in_control: bool, in_menu: bool, in_upgrade_menu: bool) -> None:
        """
        Method that upgrades a skill of the enemies every 10 seconds.

        Args:
            in_control (bool): True if the control menu is displayed, False otherwise
            in_menu (bool): True if the main menu is displayed, False otherwise
            in_upgrade_menu (bool): True if the upgrade menu is displayed, False otherwise
        """


        if pyxel.frame_count % 600 == 0 and pyxel.frame_count != 0 and not in_control and not in_menu and not in_upgrade_menu: #checks if 10 seconds had passed and if the controls, the menu or the upgrade menu is displayed
            if self.upgrades_order == "creation_speed" and self.upgrades[self.upgrades_order] > 30: #checks if it's the turn of the creation speed to be upgraded and limits the creation speed to higher than 0.1 seconds
                self.upgrades[self.upgrades_order] -= 30 #decreases the creation speed of 0.5 seconds
                self.xp += 1
                self.upgrades_order = "speed" #next skill to be upgraded: speed
            elif self.upgrades_order == "speed" and self.upgrades[self.upgrades_order] < 15: #checks if it's the turn of the speed to be upgraded and limits the speed to below 15
                self.upgrades[self.upgrades_order] += 1 #increases the speed of 1
                self.xp += 1
                self.upgrades_order = "hp" #next skill to be upgraded: hp
            elif self.upgrades_order == "hp": #checks if it's the turn of the hp to be upgraded
                self.upgrades[self.upgrades_order] += 1 #increases the hp of 1
                self.xp += 1
                self.upgrades_order = "attack" #next skill to be upgraded: attack
            elif self.upgrades_order == "attack": #checks if it's the turn of the attack to be upgraded
                self.upgrades[self.upgrades_order] += 1 #increases the attack of 1
                self.xp += 1
                self.upgrades_order = "shield" #next skill to be upgraded: shield
            elif self.upgrades_order == "shield" and self.upgrades[self.upgrades_order] < 94: #checks if it's the turn of the shield to be upgraded and limits the shield to below 95%
                self.upgrades[self.upgrades_order] += 2 #increases the shield of 2
                self.xp += 1
                self.upgrades_order = "creation_speed" #next skill to be upgraded: creation speed


    def update(self, player_x: int, player_y: int, player_size: int, player_attack: int, bullets_array: list[list[float]], bullet_size: int, window_width: int, window_height: int, in_control: bool, in_menu: bool, in_upgrade_menu: bool) -> None:
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
            in_control (bool): True if the control menu is displayed, False otherwise
            in_menu (bool): True if the main menu is displayed, False otherwise
            in_upgrade_menu (bool): True if the upgrade menu is displayed, False otherwise
        """

        #updates the attributes related to the player
        self.player_x = player_x
        self.player_y = player_y
        self.PLAYER_SIZE = player_size
        self.player_attack = player_attack

        #updates the attributes related to the bullets
        self.bullets_array = bullets_array
        self.BULLET_SIZE = bullet_size

        #updates the attributes related to the window
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height

        self.enemies_creation() # creates enemies
        self.enemies_movements() # moves enemies
        self.player_collision() #checks the collision with the player
        self.bullet_collision(self.player) #checks the collision with the bullets
        self.enemies_upgrade(in_control, in_menu, in_upgrade_menu) #upgrades the enemies

    def draw(self) -> None:
        """
        Method that draws the enemies on the window and is called infinitely in the class Game.
        """

        for enemy in self.enemies_array:
            pyxel.rect(enemy["x"], enemy["y"], self.SIZE, self.SIZE, enemy["color"]) # draws enemies/squares