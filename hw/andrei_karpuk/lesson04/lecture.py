from decimal import Decimal


def task_01_money(rubles: int, coin: int, amount: int) -> Decimal:
    rub = Decimal(rubles)
    co = Decimal(coin)
    amo = Decimal(amount)
    return (rub + co / 100) * amo


def task_02_sign(number: int | float | complex | Decimal) -> int:
    return (
        0
        if isinstance(number, complex) or number == 0
        else (+1 if number > 0 else -1)
    )


def task_03_triangle(side1: float, side2: float, side3: float) -> bool:
    s1 = side1
    s2 = side2
    s3 = side3
    return bool(s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2)


def task_04_palindrom(string: str) -> bool:
    string = string.lower()
    string = string.replace(" ", "")
    return bool(string == string[::-1])
