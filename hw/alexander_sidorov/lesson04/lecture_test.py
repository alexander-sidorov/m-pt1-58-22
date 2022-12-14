from decimal import Decimal

from .lecture import task_01_money
from .lecture import task_02_sign
from .lecture import task_03_triangle
from .lecture import task_04_palindrom


def test_task_01_money() -> None:
    assert task_01_money(1, 2, 3) == Decimal("3.06")


def test_task_02_sign() -> None:
    assert task_02_sign(-100) == -1
    assert task_02_sign(+100) == +1
    assert task_02_sign(0) == 0
    assert task_02_sign(1j) == 0


def test_task_03_triangle() -> None:
    assert not task_03_triangle(1, 2, 3)
    assert task_03_triangle(3, 4, 5)


def test_task_04_palindrom() -> None:
    assert task_04_palindrom("Аргентина манит негра")
    assert task_04_palindrom("12321")
    assert not task_04_palindrom("Аргентина")
    assert not task_04_palindrom("123")
