from hw.maksim_lamaka.lesson10.lesson import Counter
from hw.maksim_lamaka.lesson10.lesson import User

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


def test_02() -> None:

    ctr1 = Counter(0, 3)

    ctr2 = Counter(1, 4)

    assert lst(ctr1) == [0, 1, 2, 3]
    assert lst(ctr2) == [1, 2, 3, 4]

