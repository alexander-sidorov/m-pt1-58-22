from decimal import Decimal
from typing import Any


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    rub = Decimal(rubles)
    coin = Decimal(coins)
    amt = Decimal(amount)
    return (rub + (coin/100)) * amt


def task_02_sign(number: Any) -> int:
    if type(number) == complex:
        return 0
    else:
        if number > 0:
            return 1
        elif number < 0:
            return -1
        else:
            return 0


def task_03_triangle(side1: float, side2: float, side3: float) -> bool:
    if side1 > 0 and side2 > 0 and side3 > 0:
        if (side1 + side2) > side3 and (side2 + side3) > side1 and (side1 + side3) > side2:
            return True
        else:
            return False
    else:
        return False


def task_04_palindrom(string: str) -> bool:
    string = string.replace(" ", "").lower()
    str_ = string[::-1]
    return string == str_