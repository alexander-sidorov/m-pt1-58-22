from hw.mikita_karmanaw.lesson10.lesson import User


def test_01() -> None:
    alice = User('Alice')
    assert alice.get_user_name() == "Alice"
    assert alice.get_class_name() == "User"
    assert alice.get_hello_world() == "hello world"
