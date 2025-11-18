class Skill:
    """
    Class that manages the skills.
    """

    def __init__(self,
                 name: str,
                 description: str,
                 price: int,
                 amount: int,
                 level: int = 0) -> None:
        """
        Create a skill with a name, description, price, amount and level.

        Args:
            name (str): The skill name.
            description (str): The skill description.
            price (int): The skill price.
            amount (int): The skill amount represents how much the skill increases.
            level (int): The skill level, 0 by default.
        """

        self.name = name
        self.description = description
        self.price = price
        self.amount = amount
        self.level = level