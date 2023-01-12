import re
from decimal import Decimal


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    return (rubles + coins / Decimal(100)) * amount


def task_02_sign(number: int | float | complex) -> int:
    if not number or not isinstance(number, int | float):
        return 0

    return -1 if number < 0 else 1


def task_03_triangle(side1: int, side2: int, side3: int) -> bool:
    sides = (side1, side2, side3)
    for i in range(3):
        j = (i + 1) % 3  # noqa: VNE001
        k = (i + 2) % 3  # noqa: VNE001
        if sides[i] >= (sides[j] + sides[k]):
            return False
    return True


def task_04_palindrom(text: str) -> bool:
    text = re.sub(r"\s+", "", text.lower())
    return text == text[::-1]
