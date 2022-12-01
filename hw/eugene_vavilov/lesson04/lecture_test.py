from lecture import task_01_money
from lecture import task_02_sign
from lecture import task_03_triangle
from lecture import task_04_palindrom
from decimal import Decimal

assert task_01_money(1, 2, 3) == 3.06
assert task_02_sign(0) == 0
assert task_02_sign(0.3621) == 1
assert task_02_sign(-123) == -1
assert task_02_sign(Decimal("2")) == 1
assert task_02_sign(1j) == 0
assert task_03_triangle(3, 4, 5)
assert not task_03_triangle(1, 2, 3)
assert task_04_palindrom("Аргентина манит негра")
assert not task_04_palindrom("Аргентина")

# x1 = task_01_money(1, 2, 3)
# x2 = task_02_sign(2)
# x3 = task_03_trianle(2, 2, 3)
# x4 = task_04_palindrom("ao a")

# print(x1)
# print(x2)
# print(x3)
# print(x4)
