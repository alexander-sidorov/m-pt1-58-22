from decimal import Decimal


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    coins = Decimal(coins)
    rubles = Decimal(rubles)
    amount = Decimal(amount)
    coins = coins / 100
    total_sum = rubles + coins
    result = total_sum * amount
    return result


def task_02_sign(num: int) -> int:
    try:
        if num > 0:
            return 1
        elif num < 0:
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
