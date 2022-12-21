import json

import hw.eugene_lubimov.lesson10.lesson as les


def test_user() -> None:
    hw_text: str = "hello world"
    person1 = les.User("Bob")
    js = person1.to_json()

    assert js == '{"name": "Bob"}'
    assert json.loads(js) == {"name": "Bob"}
    assert str(person1) == "Bob"
    assert person1.get_class_name() == les.User.__name__
    assert person1.get_hello_world() == hw_text

    person2 = les.User("Vasya")

    assert str(person2) == "Vasya"
    assert person2.get_class_name() == les.User.__name__
    assert person2.get_hello_world() == hw_text


def test_counter() -> None:

    ctr1 = les.Counter(0, 3)

    ctr2 = les.Counter(0, 4)

    assert list(ctr2) == [0, 1, 2, 3, 4]
    assert list(ctr1) == [0, 1, 2, 3]
