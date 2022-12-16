from hw.vadim_zharski.lesson10.lesson import Counter
from hw.vadim_zharski.lesson10.lesson import User


def test_01() -> None:
    petya = User("Petya")
    vasya = User("Vasya")
    assert petya.get_name() == "Petya"
    assert vasya.get_name() == "Vasya"
    assert petya.get_class_name() == User.__name__
    assert vasya.get_class_name() == User.__name__
    assert petya.get_hello_world() == "hello world"
    assert vasya.get_hello_world() == "hello world"
    assert petya != vasya


def test_02() -> None:
    counter = Counter(8, 12)
    assert counter.next() == 9
    assert counter.next() == 10
    assert counter.next() == 11
    assert counter.next() == 12
    assert counter.next() != 13
