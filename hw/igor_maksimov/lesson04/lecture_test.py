from decimal import Decimal
from hw.igor_maksimov.lesson04.lecture import task_01_money

# Test for task number 1


def test_task_01_money() -> None:
    assert task_01_money(11, 4, 4) == Decimal(44.16)
