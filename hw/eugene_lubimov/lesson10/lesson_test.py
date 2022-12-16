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
    coun = les.Counter(10, 20)

    assert coun.next() == 10
    assert coun.next() == 11
