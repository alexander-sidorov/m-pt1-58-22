from decimal import Decimal


def task_01_money(rubles, coins, amount):
    return (rubles + (coins / 100)) * amount


print(task_01_money(1, 2, 3))


def task_02_sign(number):
    try:
        Decimal(number)
        if number > 0:
            return 1
        elif number < 0:
            return -1
        else:
            return 0
    except TypeError:
        return 0


def task_03_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        return True
    else:
        return False


print(task_03_triangle(3, 4, 5))
print(task_03_triangle(1, 2, 3))


def task_04_palindrom(string):
    string_rep = string.lower().replace(" ", "")
    string_rev = string_rep[::-1]

    return string_rep == string_rev
