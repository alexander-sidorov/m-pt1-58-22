from typing import Any
from decimal import Decimal


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    return Decimal((rubles + (coins / 100)) * amount)


def task_02_sign(number: Any) -> int:
    try:
        Decimal(number)
        if number > 0:
            return 1
        elif number < 0:
            return -1
        else:
            return 0
    except TypeError:
        return 0


def task_03_triangle(side1: float, side2: float, side3: float) -> bool:
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        return True
    else:
        return False


def task_04_palindrom(string: str) -> bool:
    string_rep = string.lower().replace(" ", "")
    string_rev = string_rep[::-1]

    return string_rep == string_rev
