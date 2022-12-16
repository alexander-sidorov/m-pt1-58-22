from hw.alexey_tyuhai.lesson10.lesson import User

def test_01():
    petya = User("Петя")
    assert petya.get_name == "Петя"
    assert petya.get_class_name() == "User"
    assert petya.get_hello_world() == "hello world"