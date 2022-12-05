from decimal import Decimal


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    dec_rubles = Decimal(rubles)
    dec_coins = Decimal(coins)
    dec_amount = Decimal(amount)
    resoult = (dec_rubles + (dec_coins / 100)) * dec_amount
    return resoult


def task_02_sign(number: Decimal) -> int:
    try:
        if number > 0:
            return 1
        if number < 0:
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


def task_04_palindrom(text: str) -> bool:
    text_full = text.replace(" ", "")
    text_lower = text_full.lower()
    text_back = text_lower[::-1]
    return text_back == text_lower
