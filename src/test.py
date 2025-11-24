from ascii import ASCII
from characters import Character

def jeux_de_test() -> None:
    """
    Function that tests most functions in the project. 
    """

    # Test ASCII
    test1 = ASCII().convert("abc") # always a space after a letter
    test2 = [
        "  /\\   |--\\  /-- ",
        " /--\\  | -< |    ",
        "/    \\ |__/  \\__ "
    ]
    test("ASCII", test1, test2)

    # Test Character
    test1 = Character(0, 10, 0, 0, 0, 0, 0).receive_damage(3, 10, 0) # 10 - 3 = 7
    test2 = 7
    test("Character 1", test1, test2)

    test1 = Character(0, 10, 0, 0, 0, 0, 0).receive_damage(3, 10, 50) # 10 - (3 * (1 - 50/100)) = 10 - 3 * 0.5 = 8.5 (arround : 8)
    test2 = 8
    test("Character 2", test1, test2)

def test(name: str, test1, test2) -> None:
    """
    Function 

    Args:
        name (str): Name of the test.
        test1 (any): The first item to test
        test2 (any): The second item to test
    """

    print(f"Test {name}: pending...")
    assert test1 == test2
    print(f"Test {name}: passed")

jeux_de_test()