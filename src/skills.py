class Skill:
    def __init__(self,
                 name: str,
                 description: str,
                 price: int,
                 amount: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount
        self.level = 0