import pyxel

class Game:
    def __init__(self) -> None:
        self.window_width: int = 1000
        self.window_height: int = 750
        self.window_title: str = "Window-Kill"

        pyxel.init(self.window_width, self.window_height, title=self.window_title)

        pyxel.run(self.update, self.draw)
    
    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
