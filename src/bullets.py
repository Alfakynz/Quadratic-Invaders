import pyxel
import math

class Bullets:
    def __init__(self, player_x, player_y, player_r, shoot_speed):

        self.player_x = player_x
        self.player_y = player_y
        self.player_r = player_r
        self.shoot_speed = shoot_speed

        self.bullet_speed = 10
        self.size = 10
        self.color = 10
        self.bullets_list: list[list[float]] = []

    def bullets_creation(self):
        
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and pyxel.frame_count % self.shoot_speed == True:
            # distance between the position of the mouse and the start position of the bullet
            dx: int = pyxel.mouse_x - (self.player_x + self.player_r)
            dy: int = pyxel.mouse_y - (self.player_y + self.player_r)
            teta: float = math.atan2(dy, dx) # calculation of teta, direction from the pole relative to the direction of the polar axis

            self.bullets_list.append([self.player_x + self.player_r, self.player_y + self.player_r, teta])

    def bullets_movements(self):
        for bullet in  self.bullets_list:
            bullet[0] += math.cos(bullet[2]) * self.bullet_speed
            bullet[1] += math.sin(bullet[2]) * self.bullet_speed
            if  bullet[0]<-10 or bullet[0]>1010 or bullet[1]<-10 or bullet[1]>760:
                self.bullets_list.remove(bullet)

    def update(self):
        self.bullets_creation()
        self.bullets_movements()

    def draw(self):
        for bullet in self.bullets_list:
            pyxel.circ(bullet[0], bullet[1], self.size, self.color)
