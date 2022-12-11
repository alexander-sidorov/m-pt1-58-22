from decimal import Decimal

from hw.eugene_vavilov.lesson04.lecture import task_01_money
from hw.eugene_vavilov.lesson04.lecture import task_02_sign
from hw.eugene_vavilov.lesson04.lecture import task_03_triangle
from hw.eugene_vavilov.lesson04.lecture import task_04_palindrom


def test_task_01_money() -> None:
    assert task_01_money(1, 2, 3) == Decimal("3.06")


def test_task_02_sign() -> None:
    assert task_02_sign(0) == 0
    assert task_02_sign(0.3621) == 1
    assert task_02_sign(-123) == -1
    assert task_02_sign(Decimal("2")) == 1
    assert task_02_sign(1j) == 0


def test_task_03_triangle() -> None:
    assert task_03_triangle(3, 4, 5)
    assert not task_03_triangle(1, 2, 3)


def test_task_04_palindrom() -> None:
    assert task_04_palindrom("Аргентина манит негра")
    assert not task_04_palindrom("Аргентина")
