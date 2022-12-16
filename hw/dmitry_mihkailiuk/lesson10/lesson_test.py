from hw.dmitry_mihkailiuk.lesson10.lesson import User


def test_01() -> None:
    dim = User("Dim")
    assert dim.get_name() == "Dim"
    assert dim.get_class_name() == "User"
    assert dim.get_hello_world() == "hello world"
