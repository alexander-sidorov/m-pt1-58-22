import hw.eugene_lubimov.lesson10.lesson as les


def test_user() -> None:
    hw_text = "hello world"
    person1 = les.User("Bob")

    assert person1.get_name == "Bob"
    assert person1.get_class_name() == les.User.__name__
    assert person1.get_hello_world() == hw_text

    person2 = les.User("Vasya")

    assert person2.get_name == "Vasya"
    assert person2.get_class_name() == les.User.__name__
    assert person2.get_hello_world() == hw_text


def test_counter() -> None:
    r1 = 1
    ctr1 = les.Counter(0, r1)

    r2 = 2
    ctr2 = les.Counter(0, r2)

    assert [ctr1.next() for _ in range(r1 + 1)] == [0, 1]
    assert [ctr2.next() for _ in range(r2 + 1)] == [0, 1, 2]
    assert [ctr2.next() for _ in range(r2 + 1)] == [2, 2, 2]