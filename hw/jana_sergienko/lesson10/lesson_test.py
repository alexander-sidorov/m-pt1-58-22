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
    c = Counter(Counter(10, 20))
    assert c.next() == 10
    assert c.next() == 11
