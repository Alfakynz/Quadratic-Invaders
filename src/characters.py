import math

class Character:
    def __init__(self,
                 color: int,
                 shape: str,
                 hp: int,
                 attack: int,
                 speed: int,
                 shield: int,
                 fire_rate: int,
                 xp: int) -> None:
        self.color = color
        self.shape = shape
        self.xp = xp
        self.skills = {
            "hp": hp,
            "attack": attack,
            "shield": shield,
            "speed": speed,
            "fire_rate": fire_rate
        }

    def teta_calculation(self, coord1: tuple[float, float], coord2: tuple[float, float]) -> float:
        """
        Function that calculates teta, direction from the pole relative to the direction of the polar axis (polar coordinates), according to two tuples of coordinates

        coord1: tuple[float, float]
        coord2: tuple[float, float]
        -> float
        """

        dx: float = coord1[0] - coord2[0] # distance between x of coord1 and x of coord2
        dy: float = coord1[1] - coord2[1] # distance between y of coord1 and y of coord2
        teta: float = math.atan2(dy, dx) # calculation of teta
        return teta
    
    def polar_to_cartesian(self, teta: float, r: int, offset: float = 0) -> tuple[float, float]:
        """
        Function that turns polar coordinates into cartesian coordinates

        teta: float
        r: int
        offset: float
        -> tuple[float, float]
        """

        x: float = math.cos(teta + offset) * r # calculates x according to the polar coordinates given (if given an offset, adds it to the operation)
        y: float = math.sin(teta + offset) * r # calculates y according to the polar coordinates given (if given an offset, adds it to the operation)
        return (x, y)

    def receive_damage(self, amount, hp, shield) -> int:
        hp -= amount * (1 - shield // 100)
        if hp < 0:
            hp = 0
        
        return hp