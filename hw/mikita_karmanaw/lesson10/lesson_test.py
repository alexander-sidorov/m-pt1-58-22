import json

from hw.mikita_karmanaw.lesson10.lesson import Counter
from hw.mikita_karmanaw.lesson10.lesson import User


def test_01() -> None:
    alice = User("Alice")
    assert alice.get_class_name() == "User"
    assert alice.get_hello_world() == "hello world"
    assert str(alice) == "Alice"
    alice_js = alice.to_json()
    assert alice_js == '{"name": "Alice"}'
    assert json.loads(alice_js) == {"name": "Alice"}
    bob = User("Bob")
    assert bob.get_class_name() == "User"
    assert bob.get_hello_world() == "hello world"
    assert str(bob) == "Bob"
    bob_js = bob.to_json()
    assert bob_js == '{"name": "Bob"}'
    assert json.loads(bob_js) == {"name": "Bob"}


def test_02() -> None:
    count = Counter(10, 20)
    assert next(count) == 10
    assert next(count) == 11
    count_2 = Counter(-5, 3)
    assert list(count_2) == [-5, -4, -3, -2, -1, 0, 1, 2, 3]
    count_2.cursor(-3)
    assert list(count_2) == [-5, -4, -3, -2, -1, 0, 1, 2, 3]
    count_2.cursor(5)
    assert list(count_2) == [0, 1, 2, 3]
    