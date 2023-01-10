import json

from hw.alexander_sidorov.lesson10.lesson import Counter
from hw.alexander_sidorov.lesson10.lesson import User


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


def test_task_02() -> None:
    assert list(Counter(0, 2)) == [0, 1, 2]
    assert tuple(Counter(1, 3)) == (1, 2, 3)
    assert set(Counter(-1, 1)) == {-1, 0, 1}


def test_task_05() -> None:
    petya = User("P")
    js = petya.to_json()

    assert js == '{"name": "P"}'
    assert json.loads(js) == {"name": "P"}
