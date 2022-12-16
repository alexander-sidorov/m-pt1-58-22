from hw.jana_sergienko.lesson10.lesson import User


def test_01() -> None:
    hw_text = "hello world"
    name = "Петя"
    petya = User(name)
    assert petya.get_name() == name
    petya = User("Петя")
    vasya = User("Вася")

    assert petya.get_name() == "Петя"
    assert petya.get_class_name() == User.__name__
    assert petya.get_hello_world() == hw_text

    name = "Вася"
    vasya = User(name)
    assert vasya.get_name() == name
    assert vasya.get_name() == "Вася"
    assert vasya.get_class_name() == User.__name__
    assert vasya.get_hello_world() == hw_text