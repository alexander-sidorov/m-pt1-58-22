import hw.eugene_lubimov.lesson10.lesson as les


def test_user() -> None:
    person = les.User("Bob")

    assert person.get_name() == "Bob"
    assert person.get_class_name() == "User"
    assert person.get_hello_world() == "hello world"
