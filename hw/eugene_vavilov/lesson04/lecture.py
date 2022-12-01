from decimal import Decimal


def task_01_money(rubles: int, coins: int, amount: int) -> float:
    summa = float((Decimal(rubles) + (Decimal(coins) / 100)) * Decimal(amount))
    return summa


def task_02_sign(number: int) -> int:
    if (
        isinstance(number, int | float | Decimal) != 1
        or number == 0
        or number == complex
    ):
        return 0
    else:
        if number > 0:
            return 1
        else:
            if number < 0:
                return -1
            else:
                assert 0, "Ошибка"


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
    if rev_string == string1:
        return True
    else:
        return False
