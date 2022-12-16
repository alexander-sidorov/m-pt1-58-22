from hw.jana_sergienko.lesson10.lesson import User
from hw.jana_sergienko.lesson10.lesson import Counter


def test_01() -> None:
    hw_text = "hello world"
    name = User("Петя")
    petya = User("Вася")

    assert name.get_name() == "Петя"
    assert name.get_class_name() == User.__name__
    assert name.get_hello_world() == hw_text
    assert petya.get_name() == "Вася"
    assert petya.get_class_name() == User.__name__
    assert petya.get_hello_world() == hw_text


def test_02() -> None:
    r1 = 1
    ctr1 = Counter(0, r1)

    r2 = 2
    ctr2 = Counter(0, r2)

    assert [ctr1.next() for _ in range(r1 + 1)] == [0, 1]
    assert [ctr2.next() for _ in range(r2 + 1)] == [0, 1, 2]
    assert [ctr2.next() for _ in range(r2 + 1)] == [2, 2, 2]
