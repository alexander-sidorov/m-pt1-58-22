from hw.alexander_sidorov.lesson10.lesson import User


def test_01():
    hw_text = "hello world"
    name = "Петя"
    petya = User(name)
    assert petya.get_name() == name
    assert petya.get_class_name() == User.__name__
    assert petya.get_hello_world() == hw_text

    name = "Вася"
    vasya = User(name)
    assert vasya.get_name() == name
    assert vasya.get_class_name() == User.__name__
    assert vasya.get_hello_world() == hw_text
