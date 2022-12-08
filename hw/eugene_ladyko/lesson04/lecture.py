from decimal import Decimal
from typing import Any


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    ru = Decimal(rubles)
    co = Decimal(coins)
    am = Decimal(amount)
    return (ru + co / 100) * am


def task_02_sing(numb: Any) -> int:
    if type(numb) == complex or numb == 0:
        return 0
    elif numb > 0:
        return 1
    elif numb < 0:
        return -1
