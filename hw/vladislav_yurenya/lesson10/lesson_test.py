from hw.vladislav_yurenya.lesson10.lesson import Counter
from hw.vladislav_yurenya.lesson10.lesson import User


def test_01() -> None:
    txt = "hello word"
    zhora = User("Петя")
    vasya = User("Вася")
    assert zhora.get_name() == "Петя"
    assert zhora.get_class_name() == User.__name__
    assert zhora.get_hello_word() == txt
    assert vasya.get_name() == "Вася"
    assert vasya.get_class_name() == User.__name__
    assert vasya.get_hello_word() == txt


def test_02() -> None:
    r1 = 1
    ctr1 = Counter(0, r1)
    r2 = 2
    ctr2 = Counter(0, r2)
    assert [ctr1.next() for _ in range(r1 + 1)] == [0, 1]
    assert [ctr2.next() for _ in range(r2 + 1)] == [0, 1, 2]
    assert [ctr2.next() for _ in range(r2 + 1)] == [2, 2, 2]
