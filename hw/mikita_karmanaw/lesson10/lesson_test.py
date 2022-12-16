from hw.mikita_karmanaw.lesson10.lesson import User
from hw.mikita_karmanaw.lesson10.lesson import Counter


def test_01() -> None:
    alice = User("Alice")
    assert alice.get_user_name() == "Alice"
    assert alice.get_class_name() == "User"
    assert alice.get_hello_world() == "hello world"
    bob = User("Bob")
    assert bob.get_user_name() == "Bob"
    assert bob.get_class_name() == "User"
    assert bob.get_hello_world() == "hello world"


def test_02() -> None:
    c = Counter(10, 20)
    assert c.next() == 10
    assert c.next() == 11
