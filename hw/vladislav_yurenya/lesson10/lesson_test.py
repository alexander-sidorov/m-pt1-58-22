import json

import pytest

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
    count = Counter(3, 7)
    iteration = iter(count)
    assert next(iteration) == 3
    assert next(iteration) == 4
    assert next(iteration) == 5
    assert next(iteration) == 6
    assert next(iteration) == 7

    with pytest.raises(StopIteration):
        next(iteration)


def test_03() -> None:
    for_json = User({"rabbit": None})  # type: dict[str, None]
    js = for_json.to_json()
    assert js == '{"rabbit": null}'
    assert json.loads(js) == {"rabbit": None}
