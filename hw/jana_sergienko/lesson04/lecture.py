from decimal import Decimal
from typing import Any


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    rub = Decimal(rubles)
    coin = Decimal(coins)
    amt = Decimal(amount)
    return (rub + (coin / 100)) * amt


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
        tringle = [side1, side2, side3]
        for i in tringle:
            if i <= 0:
                return False
        return (tringle[0] + tringle[1] > tringle[2]
                and tringle[1] + tringle[2] > tringle[0]
                and tringle[0] + tringle[2] > tringle[1])


def task_04_palindrom(string: str) -> bool:
    string = string.replace(" ", "").lower()
    str_ = string[::-1]
    return string == str_