from typing import TypedDict

class Enemy(TypedDict):
    """
    An enemy with their characteristics.

    Args:
        x (float): The x position.
        y (float): The y position.
        reverse (bool): Repulse effect when the enemy touches the player.
        teta (float): The direction from the pole relative to the direction of the polar axis.
        count_player (int): The time after having touched the player.
        count_bullet (int): The time after having touched a bullet.
        bullet_touched (bool): True if collided with a bullet, False otherwise.
        color (int): The enemy color.
        hp (int): The enemy hp.
        attack (int): The enemy attack.
        speed (float): The enemy speed.
        shield (int): The enemy shield.
        fire_rate (float): The enemy fire rate.
        xp (int): The enemy xp.
    """

    x: float
    y: float
    reverse: bool
    teta: float
    count_player: int
    count_bullet: int
    bullet_touched: int
    color: int
    hp: int
    attack: int
    speed: float
    shield: int
    fire_rate: float
    xp: int