from decimal import Decimal
from typing import Any


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    return Decimal((rubles + (coins / 100)) * amount)


def task_02_sign(number: Any) -> int:
    try:
        if number > 0:
            return 1
        elif number < 0:
            return -1
        else:
            return 0
    except TypeError:
        return 0


def task_03_triangle(side1: int, side2: int, side3: int) -> bool:
    if (
        side1 + side2 > side3
        and side1 + side3 > side2
        and side3 + side2 > side1
    ):
        return True
    else:
        return False


def task_04_palindrom(string: str) -> bool:
    string = string.replace(" ", "").lower()
    re_string = string[::-1]
    if string == re_string:
        return True
    else:
        return False
