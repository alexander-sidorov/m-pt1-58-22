from hw.andrei_karpuk.lesson10.lesson import User
from hw.andrei_karpuk.lesson10.lesson import Counter
def test_01() -> None:
    hw_text = "hello world"
    petya = User("Петя")
    vasya = User("Вася")

    assert petya.get_name() == "Петя"
    assert petya.get_class_name() == User.__name__
    assert petya.get_hello_world() == hw_text

    assert vasya.get_name() == "Вася"
    assert vasya.get_class_name() == User.__name__
    assert vasya.get_hello_world() == hw_text

def test_02() -> None:
    c = Counter(10, 20)
    assert c.next() == 10
    assert c.next() == 20


def test_02() -> None:
    r1 = 1
    ctr1 = Counter(0, r1)

    r2 = 2
    ctr2 = Counter(0, r2)

    assert [ctr1.next() for _ in range(r1 + 1)] == [0, 1]
    assert [ctr2.next() for _ in range(r2 + 1)] == [0, 1, 2]
    assert [ctr2.next() for _ in range(r2 + 1)] == [2, 2, 2]