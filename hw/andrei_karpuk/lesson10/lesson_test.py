import json

from hw.andrei_karpuk.lesson10.lesson import Counter
from hw.andrei_karpuk.lesson10.lesson import User


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
    r1 = 1
    ctr1 = Counter(0, r1)

    r2 = 2
    ctr2 = Counter(0, r2)

    assert list(ctr1) == [0, 1]
    assert list(ctr2) == [0, 1, 2]


def test_03() -> None:
    petya = User("P")
    js = petya.to_json()

    assert js == '{"name": "P"}'
    assert json.loads(js) == {"name": "P"}
