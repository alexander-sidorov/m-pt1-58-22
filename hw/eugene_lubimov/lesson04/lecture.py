from decimal import Decimal


def task_01_money(rubles: int, coins: int, amount: int) -> object:

    return Decimal(str((rubles * 100 + coins) * amount / 100))


def task_02_sign(number: object) -> int:
    if not isinstance(number, (int, float, Decimal)):
        return 0
    if number > 0:
        return 1
    if number < 0:
        return -1
    return 0


def task_03_triangle(side1: int, side2: int, side3: int) -> bool:

    return (
        side1 < (side2 + side3)
        and side2 < (side1 + side3)
        and side3 < (side1 + side2)
    )


def task_04_palindrom(string: str) -> bool:

    new_string = "".join([i for i in string if i.isalpha()]).lower()
    return new_string == new_string[::-1]
