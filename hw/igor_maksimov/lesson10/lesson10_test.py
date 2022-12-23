import json

from hw.igor_maksimov.lesson10.lesson10 import Counter
from hw.igor_maksimov.lesson10.lesson10 import User


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

    ctr1 = Counter(0, 3)

    ctr2 = Counter(1, 4)

    assert list(ctr1) == [0, 1, 2, 3]
    assert list(ctr2) == [1, 2, 3, 4]


def test_05() -> None:

    petya = User("P")
    js = petya.to_json()

    assert js == '{"name": "P"}'
    assert json.loads(js) == {"name": "P"}

