import json

from hw.vladislav_yurenya.lesson10.lesson import Counter
from hw.vladislav_yurenya.lesson10.lesson import User


def test_01() -> None:
    name01 = User("Zhora")
    name02 = User("Вася")
    assert str(name01) == "Zhora"
    assert name01.get_class_name() == User.__name__
    assert name01.get_hello_world() == "hello world"
    assert str(name02) == "Вася"
    assert name02.get_class_name() == User.__name__
    assert name02.get_hello_world() == "hello world"


def test_02() -> None:
    assert list(Counter(3, 5)) == [3, 4, 5]
    assert list(Counter(6, 10)) == [6, 7, 8, 9, 10]


def test_03() -> None:
    for_json = User("None")
    js = for_json.to_json()
    assert js == '{"rabbit": "None"}'
    assert json.loads(js) == {"rabbit": "None"}
