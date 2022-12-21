from hw.eugene_bakun.lesson_10.lesson import Counter
from hw.eugene_bakun.lesson_10.lesson import User


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
    r1 = 1
    ctr1 = Counter(0, r1)

    r2 = 2
    ctr2 = Counter(0, r2)

    assert list(ctr1) == [0, 1, 3, 4]
    assert list(ctr2) == [0, 1, 3, 4]

