from hw.dmitry_mihkailiuk.lesson10.lesson import Counter
from hw.dmitry_mihkailiuk.lesson10.lesson import User


def test_01() -> None:
    dim = User("Dim")
    assert dim.get_name() == "Dim"
    assert dim.get_class_name() == "User"
    assert dim.get_hello_world() == "hello world"


def test_02() -> None:
    r1 = 1
    ctr1 = Counter(0, r1)

    r2 = 2
    ctr2 = Counter(0, r2)

    assert [ctr1.next() for _ in range(r1 + 1)] == [0, 1]
    assert [ctr2.next() for _ in range(r2 + 1)] == [0, 1, 2]
    assert [ctr2.next() for _ in range(r2 + 1)] == [2, 2, 2]
