from hw.vladislav_yurenya.lesson10.lesson import Counter
from hw.vladislav_yurenya.lesson10.lesson import User


def test_01() -> None:
    name01 = User("Zhora")
    name02 = User("Вася")
    assert name01.__str__() == "Zhora"
    assert name01.get_class_name() == User.__name__
    assert name01.get_hello_world() == "hello world"
    assert name02.__str__() == "Вася"
    assert name02.get_class_name() == User.__name__
    assert name02.get_hello_world() == "hello world"


def test_02() -> None:
    count = Counter(-3, 3)
    assert count.next() == -3
    assert count.next() == -2
