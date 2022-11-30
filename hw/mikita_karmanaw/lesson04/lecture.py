from decimal import Decimal


def task_01_money(rubles: int, coins: int, amount: int) -> float:
    rb = Decimal(rubles)
    cn = Decimal(coins)
    am = Decimal(amount)
    return (rb + (cn / 100)) * am


def task_02_sign(number) -> int:
    if number == 0 or isinstance(number, complex):
        sign = 0
    else:
        sign = (1 if number > 0 else -1)
    return sign


def task_03_triangle(side1, side2, side3) -> bool:
    tria = [side1, side2, side3]
    for i in tria:
        if i <= 0: return(False)
    return bool(tria.pop(tria.index(max(tria))) < (tria[0] + tria[1]))


def task_04_palindrom(string) -> bool:
    string = string.lower()
    for i in ' ,.:;!?':
        string = string.replace(i, '')
    return bool(string == string[::-1])
