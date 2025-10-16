import pyxel

class Game:
    def __init__(self) -> None:
        self.window_width: int = 1000
        self.window_height: int = 750

        pyxel.init(self.window_width, self.window_height, title="Window-Kill")

        pyxel.run(self.update, self.draw)
    
    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
