from decimal import Decimal
from typing import Any


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    rubles_d = Decimal(rubles)
    coins_d = Decimal(coins)
    amount_d = Decimal(amount)
    return (rubles_d + (coins_d / 100)) * amount_d


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


def task_03_triangle(side1: float, side2: float, side3: float) -> bool:
    result = (
        side1 + side2 > side3
        and side2 + side3 > side1
        and side1 + side3 > side2
    )
    return result


def task_04_palindrom(string: str) -> bool:
    string = string.replace(" ", "").lower()
    re_string = string[::-1]
    return string == re_string
