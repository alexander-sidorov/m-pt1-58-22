from decimal import Decimal
def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    rubles=Decimal(rubles)
    coins=Decimal(coins/100)
    amount=Decimal(amount)
    total = (rubles + coins) * amount
    return total

def task_02_sign(number:int or float or complex) -> int:
    if isinstance(number,complex) or number==0:
        return 0
    elif number<0:
        return -1
    elif number>0:
        return 1

def task_03_triangle(side1: float,side2: float,side3: float) -> bool:
    answer=(side1+side2>side3 and side1+side3>side2 and side2+side3>side1)
    return answer

def task_04_palindrom(string):
    string=string.lower()
    string=string.split(' ')
    string=''.join(string)
    if string[::-1]==string:
        return True
    else:
        return False


