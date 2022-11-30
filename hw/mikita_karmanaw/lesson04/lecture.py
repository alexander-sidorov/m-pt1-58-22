from decimal import Decimal

def task_01_money(rubles, coins, amount):
    return(decimal((rubles + (coins / 100)) * amount))

def task_02_sign(number):
    if abs(number) == 0:
        sign = 0
    else:
        sign = (1 if abs(number) > 0 else -1)
    return(sign)

def task_03_triangle(side1, side2, side3):
    tria = [side1, side2, side3]
    for i in tria:
        if i <= 0: return(False)
    return(bool(tria.pop(tria.index(max(tria))) < (tria[0] + tria[1])))

def task_04_palindrom(string):
    string = string.lower()
    for i in ' ,.:;!?':
        string = string.replace(i, '')
    return(bool(string == string[::-1]))

print(task_02_sign(1j))