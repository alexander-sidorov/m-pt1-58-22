from decimal import Decimal
from typing import Any


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    rub = Decimal(rubles)
    coi = Decimal(coins)
    amo = Decimal(amount)
    return (rub + (coi / 100)) * amo


def task_02_sign(number: Any) -> int:
    if type(number) == complex:
        return 0
    elif number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def task_03_triangle(side1: float, side2: float, side3: float) -> bool:

    return (
        (side1 + side2) > side3
        and (side2 + side3) > side1
        and (side3 + side1) > side2
    )


def task_04_palindrom(string: str) -> bool:
    string = string.lower().replace(" ", "")
    string_1 = string[::-1]
    return string_1 == string
