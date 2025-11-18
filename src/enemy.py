from typing import TypedDict

class Enemy(TypedDict):
    """
    An enemy with his characteristic.

    Args:
        x (float): The x position.
        y (float): The y position.
        reverse (bool): If the enemy has touched the player.
        teta (float): The direction from the pole relative to the direction of the polar axis.
        count (int): The time after having touched the player.
        color (int): The enemy color.
        shape (str): The enemy shape (not yet implemented).
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
    count: int
    color: int
    shape: str
    hp: int
    attack: int
    speed: float
    shield: int
    fire_rate: float
    xp: int