from decimal import Decimal

import hw.eugene_lubimov.lesson04.lecture as lec


def test_task_01_money() -> None:

    assert lec.task_01_money(1, 2, 3) == Decimal("3.06")
    assert lec.task_01_money(8, 5, 4) == Decimal("32.2")


def test_task_02_sign() -> None:

    assert lec.task_02_sign(0) == 0
    assert lec.task_02_sign(0.3621) == 1
    assert lec.task_02_sign(-123) == -1
    assert lec.task_02_sign(Decimal("2")) == 1
    assert lec.task_02_sign(1j) == 0


def test_task_03_triangle() -> None:

    assert lec.task_03_triangle(3, 4, 5)
    assert not lec.task_03_triangle(1, 2, 3)


def test_task_04_palindrom() -> None:

    assert lec.task_04_palindrom("Аргентина манит негра")
    assert not lec.task_04_palindrom("Аргентина")
    assert not lec.task_04_palindrom('12321')
