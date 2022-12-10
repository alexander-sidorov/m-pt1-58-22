from decimal import Decimal
from typing import Any


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    ru = Decimal(rubles)
    co = Decimal(coins)
    am = Decimal(amount)
    return (ru + co / 100) * am


def task_02_sign(numb: Any) -> int:
    if type(numb) == complex or numb == 0:
        if numb > 0:
            return 1
    else:
        return -1
    return 0


def task_03_triangle(side1: int, side2: int, side3: int) -> bool:
    result = (
            side1 + side2 > side3
            and side2 + side3 > side1
            and side1 + side3 > side2
    )
    return result


def task_04_palindrom(string1: str) -> bool:
    string1 = (string1.replace(" ", "")).lower()
    rev_string = string1[::-1]
    result = string1 == rev_string
    return result
