from decimal import Decimal

assert task_01_money(1, 2, 3) == Decimal("3.06")


from decimal import Decimal

assert task_02_sign(0) == 0
assert task_02_sign(0.3621) == 1
assert task_02_sign(-123) == -1
assert task_02_sign(Decimal("2")) == 1
assert task_02_sign(1j) == 0


assert task_03_triangle(3, 4, 5)
assert not task_03_triangle(1, 2, 3)


assert task_04_palindrom("Аргентина манит негра")
assert not task_04_palindrom("Аргентина")