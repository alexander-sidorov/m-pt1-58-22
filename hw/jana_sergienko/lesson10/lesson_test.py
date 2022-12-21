from hw.jana_sergienko.lesson10.lesson import Counter
from hw.jana_sergienko.lesson10.lesson import User


def test_01() -> None:
    hw_text = "hello world"
    name = User("Петя")
    petya = User("Вася")

    assert name.__str__() == "Петя"
    assert name.get_class_name() == User.__name__
    assert name.get_hello_world() == hw_text
    assert petya.__str__() == "Вася"
    assert petya.get_class_name() == User.__name__
    assert petya.get_hello_world() == hw_text


def test_02() -> None:
    ctr1 = Counter(0, 3)
    ctr2 = Counter(0, 5)

    assert next(ctr1) == 0
    lst = list(ctr1)
    assert lst == [1, 2, 3]
    assert next(ctr2) == 0
    assert next(ctr2) == 1
