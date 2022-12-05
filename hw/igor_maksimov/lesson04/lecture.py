from decimal import Decimal
from typing import Any


# Task number 1


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    rubles = Decimal(rubles)
    coins = Decimal(coins)
    amount = Decimal(amount)
    total = (rubles + (coins / 100)) * amount
    return total


# Task number 2


def task_02_sign(number: Any) -> int:
    if number > 0:
        return +1
    elif number < 0:
        return -1
    else:
        return 0


# Task number 3

def task_03_triangle(side1: float, side2: float, side3: float) -> bool:
    result = (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1)
    if result:
        print('Its triangle!!')
    else:
        print("Its not triangle")
    return result


# Task number 4


def task_04_palindrom(string: str) -> bool:
    string = string.lower()
    string = string.replace(" ", "")
    result = string[::-1] == string
    return result
