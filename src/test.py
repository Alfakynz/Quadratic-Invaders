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
    test1 = Character(0, 10, 10, 0, 0, 0, 0, 0).receive_damage(3, 10, 0) # 10 - 3 = 7
    test2 = 7
    test("Character receive_damage 1", test1, test2)

    test1 = Character(0, 10, 10, 0, 0, 0, 0, 0).receive_damage(3, 10, 50) # 10 - (3 * (1 - 50/100)) = 10 - 3 * 0.5 = 8.5 (arround : 8)
    test2 = 8
    test("Character receive_damage 2", test1, test2)

    test1 = round(Character(1, 10, 10, 1, 5, 0, 10, 0).teta_calculation((900, 700), (100, 200)), 10) # arctan((700 - 200) / (900 - 100)) = arctan(500 / 800) = 0.5585993153 (with the calculator)
    test2 = 0.5585993153
    test("Character teta_calculation 1", test1, test2)

    test1 = Character(1, 5, 15, 99, 50, 99, 100, 666).teta_calculation((500, 100), (200, 100)) # arctan((100 - 100) / (500 - 200)) = arctan(0 / 300) = 0.0
    test2 = 0.0
    test("Character teta_calculation 2", test1, test2)

    test1 = Character(1, 5, 15, 99, 50, 99, 100, 666).polar_to_cartesian(1.22, 10, 5) # (cos(1.22 + 5) * 10, sin(1.22 + 5) * 10) = (cos(6.22) * 10, sin(6.22) * 10) = (9.980044725, -0.6314327225) (with the calculator)
    x = round(test1[0], 9)
    y = round(test1[1], 10)
    test2 = (9.980044725, -0.6314327225)
    test("Character polar_to_cartesian 1", (x, y), test2)

    test1 = Character(1, 10, 10, 1, 5, 0, 10, 0).polar_to_cartesian(0, 50, 0) # (cos(0 + 0) * 50, sin(0 + 0) * 50) = (1 * 50, 0 * 50) = (50, 0)
    test2 = (50, 0)
    test("Character polar_to_cartesian 2", test1, test2)


def test(name: str, test1, test2) -> None:
    """
    Function to test 2 args with an assert.

    Args:
        name (str): Name of the test.
        test1 (any): The first item to test
        test2 (any): The second item to test
    """

    print(f"Test {name}: pending...")
    assert test1 == test2
    print(f"Test {name}: passed")