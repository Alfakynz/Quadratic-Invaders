from typing import TypedDict

class Enemy(TypedDict):
    x: float
    y: float
    reverse: bool
    teta: float
    count: int
    color: int
    shape: str
    hp: int
    damage: int
    speed: float
    shield: int
    fire_rate: float
    xp: int