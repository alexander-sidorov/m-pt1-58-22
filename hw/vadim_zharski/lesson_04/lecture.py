from decimal import Decimal
from typing import Any


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    dec_coins = Decimal(coins)
    dec_rubles = Decimal(rubles)
    dec_amount = Decimal(amount)
    dec_coins = dec_coins / 100
    total_sum = dec_rubles + dec_coins
    result = total_sum * dec_amount
    return result


def task_02_sign(num: Any) -> int:
    try:
        temp_num = float(num)
        if temp_num > 0:
            return 1
        elif temp_num < 0:
            return -1
        else:
            return 0
    except TypeError:
        return 0


def task_03_triangle(side1: float, side2: float, side3: float) -> bool:
    result = (
        (side1 + side2) > side3
        and (side1 + side3) > side2
        and (side2 + side3) > side1
    )
    return result


def task_04_palindrom(phrase: str) -> bool:
    phrase = phrase.lower().replace(" ", "")
    temp_phrase = phrase[::-1]
    return phrase == temp_phrase
