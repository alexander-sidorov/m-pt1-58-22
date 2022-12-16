from hw.igor_maksimov.lesson10.lesson10 import User
from hw.igor_maksimov.lesson10.lesson10 import Counter

def test_01():
    igor = User("Igor")
    vasia = User("Vasia")
    assert igor.get_name() == "Igor"
    assert igor.get_class_name() == User.__name__
    assert igor.get_hello_world() == "hello world"
    assert vasia.get_name() == "Vasia"
    assert vasia.get_class_name() == User.__name__
    assert vasia.get_hello_world() == 'hello world'

def test_02():
    r1 = 1
    ctr1 = Counter(0, r1)

    r2 = 2
    ctr2 = Counter(0, r2)

    assert [ctr1.next() for _ in range(r1 + 1)] == [0, 1]
    assert [ctr2.next() for _ in range(r2 + 1)] == [0, 1, 2]
    assert [ctr2.next() for _ in range(r2 + 1)] == [2, 2, 2]