from decimal import Decimal

from hw.alexey_tyuhai.lesson04.lecture import task_01_money as task1
from hw.alexey_tyuhai.lesson04.lecture import task_02_sign as task2
from hw.alexey_tyuhai.lesson04.lecture import task_03_triangle as task3
from hw.alexey_tyuhai.lesson04.lecture import task_04_palindrom as task4


def task1() -> None:
    assert task1(1, 2, 3) == Decimal("3.06")


def task2() -> None:
    assert task2(0) == 0
    assert task2(0.3621) == 1
    assert task2(Decimal("2")) == 1
    assert task2(1j) == 0


def task3() -> None:
    assert task3(3, 4, 5)
    assert not task3(1, 2, 3)


def task4() -> None:
    assert task4("Аргентина манит негра")
    assert not task4("Аргентина")
