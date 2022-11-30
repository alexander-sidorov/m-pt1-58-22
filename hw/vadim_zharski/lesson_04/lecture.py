from ast import Str
from decimal import Decimal, getcontext

def task_01_money(rubles, coins, amount) -> Decimal:
    getcontext().prec = 3
    coins = Decimal(coins / 100)
    rubles = Decimal(rubles)
    amount = Decimal(amount)
    total_sum = rubles + coins
    result = total_sum * amount
    return result

def task_02_sign(num) -> int:
    try:
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0
    except:
        return 0

def task_03_triangle(side1, side2, side3) -> bool: 
    if ((side1+side2)>side3) and ((side1+side3)>side2) and ((side2+side3)>side1):
        return True
    else: 
        return False

def task_04_palindrom(str: Str) -> bool:
    str = str.lower().replace(" ","")
    temp_str = str[::-1]
    if str == temp_str: 
        return True
    else: return False


def main():
    # result = task_01_money(1, 16, 3)
    # print(type(result))
    # print(result)
    assert task_01_money(1, 2, 3) == Decimal("3.06")

    # print(task_02_sign(0))
    assert task_02_sign(0) == 0
    assert task_02_sign(0.3621) == 1
    assert task_02_sign(-123) == -1
    assert task_02_sign(Decimal("2")) == 1
    assert task_02_sign(1j) == 0


    assert task_03_triangle(3, 4, 5)
    assert not task_03_triangle(1, 2, 3)

    assert task_04_palindrom("Аргентина манит негра")
    assert not task_04_palindrom("Аргентина")
    


if __name__ == "__main__":
    main()