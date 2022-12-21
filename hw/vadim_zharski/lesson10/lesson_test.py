import pytest
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
    assert js == '{"name":"Petya"}'
    assert json.loads(js) == {"name": "Petya"}


def test_02() -> None:
    counter = Counter(8, 12)
    iter_count = iter(counter)
    assert next(iter_count) == 9
    assert next(iter_count) == 10
    assert next(iter_count) == 11
    assert next(iter_count) == 12

    with pytest.raises(StopIteration):
        next(iter_count)



