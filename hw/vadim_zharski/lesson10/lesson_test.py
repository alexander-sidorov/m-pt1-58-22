from hw.vadim_zharski.lesson10.lesson import User


def test_01() -> None:
    petya = User("Petya")
    vasya = User("Vasya")
    assert petya.get_class_name() == User.__name__
    assert vasya.get_class_name() == User.__name__
    assert petya.get_hello_world() == "hello world"
    assert vasya.get_hello_world() == "hello world"
    assert not petya == vasya
