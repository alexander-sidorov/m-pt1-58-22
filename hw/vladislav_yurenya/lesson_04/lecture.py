from decimal import Decimal
from typing import Any


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    rubles_dec = Decimal(rubles)
    coins_dec = Decimal(coins)
    amount_dec = Decimal(amount)
    total = (rubles_dec + coins_dec / 100) * amount_dec
    return total


def task_02_sign(number: Any) -> int:
    if isinstance(number, complex):
        return 0
    elif number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0


def task_03_triangle(side1: float, side2: float, side3: float) -> bool:
    answer = (
        side1 + side2 > side3
        and side1 + side3 > side2
        and side2 + side3 > side1
    )
    return answer


def task_04_palindrom(string: str) -> bool:
    string = string.lower()
    string = string.split(" ")
    string = "".join(string)
    return string[::-1] == string
