from decimal import Decimal


def task_01_money(rubles: int, coin: int, amount: int) -> Decimal:

    return (rubles + coin/100) * amount


def task_02_sign(number: int | float | complex) -> int:

    return +1 if task_02_sign(number) > 0 else(-1 if task_02_sign(number) < 0 else 0)


def task_03_triangle(side1: float, side2: float, side3: float) -> bool:
    s1 = side1
    s2 = side2
    s3 = side3
    if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2:
        return True
    else:
        False


def task_04_palindrom(string: str) -> bool:
    string = string.lower()
    string = string.replace(" ", "")
    if string == string[::-1]:
        return True
    else:
        return False