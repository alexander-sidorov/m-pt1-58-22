import json

from hw.vadim_zharski.lesson10.lesson import Counter
from hw.vadim_zharski.lesson10.lesson import User


def test_01() -> None:
    petya = User("Petya")
    vasya = User("Vasya")
    assert petya.get_class_name() == User.__name__
    assert vasya.get_class_name() == User.__name__
    assert petya.get_hello_world() == "hello world"
    assert vasya.get_hello_world() == "hello world"
    assert petya != vasya

    assert str(vasya) == "Vasya"
    assert str(petya) == "Petya"
    assert vasya.__str__() == "Vasya"

    js = petya.to_json()
    assert js == '{"name": "Petya"}'
    assert json.loads(js) == {"name": "Petya"}


def test_02() -> None:
    assert list(Counter(8, 12)) == [8, 9, 10, 11, 12]
    assert list(Counter(-2, 2)) == [-2, -1, 0, 1, 2]
