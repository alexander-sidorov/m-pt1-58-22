from hw.sergey_sakovich.lesson10.lesson import User
from hw.sergey_sakovich.lesson10.lesson import Counter


def test_01() -> None:
    hw_text = "hello world"
    petya = User("Петя")
    vasya = User("Вася")

    assert petya.get_name() == "Петя"
    assert petya.get_class_name() == User.__name__
    assert petya.get_hello_world() == hw_text

    assert vasya.get_name() == "Вася"
    assert vasya.get_class_name() == User.__name__
    assert vasya.get_hello_world() == hw_text


def test_02() -> None:
    c = Counter(10, 20)
    assert c.next() == 10
    assert c.next() == 11