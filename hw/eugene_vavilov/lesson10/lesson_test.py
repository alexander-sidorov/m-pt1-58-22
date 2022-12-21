from hw.eugene_vavilov.lesson10.lesson import Counter
from hw.eugene_vavilov.lesson10.lesson import User


def test_01() -> None:
    hw_text = "hello world"
    petya = User("Петя")
    vasya = User("Вася")

    assert petya.__str__() == "Петя"
    assert petya.get_class_name() == User.__name__
    assert petya.get_hello_world() == hw_text

    assert vasya.__str__() == "Вася"
    assert vasya.get_class_name() == User.__name__
    assert vasya.get_hello_world() == hw_text


def test_02() -> None:
    counter = Counter(10, 20)
    assert counter.next() == 10
    assert counter.next() == 11
