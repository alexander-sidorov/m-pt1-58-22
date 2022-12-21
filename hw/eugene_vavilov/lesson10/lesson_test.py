from hw.eugene_vavilov.lesson10.lesson import Counter
from hw.eugene_vavilov.lesson10.lesson import User


def test_01() -> None:
    hw_text = "hello world"
    petya = User("Петя")
    vasya = User("Вася")

    assert str(petya) == "Петя"
    assert petya.get_class_name() == User.__name__
    assert petya.get_hello_world() == hw_text

    assert str(vasya) == "Вася"
    assert vasya.get_class_name() == User.__name__
    assert vasya.get_hello_world() == hw_text


def test_02() -> None:
    counter = Counter(10, 20)
    assert next(counter) == 10
    assert next(counter) == 11
    assert next(counter) == 12
    assert next(counter) == 13
    assert next(counter) == 14
    assert next(counter) == 15
    assert next(counter) == 16
    assert next(counter) == 17
    assert next(counter) == 18
    assert next(counter) == 19
    assert next(counter) == 20
