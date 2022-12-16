from hw.igor_maksimov.lesson10.lesson10 import User

def test_01():
    igor = User("Igor")
    vasia = User("Vasia")
    assert igor.get_name() == "Igor"
    assert igor.get_class_name() == User.__name__
    assert igor.get_hello_world()=== "hello world"
    assert vasia.get_name == "Vasia"
    assert vasia.get_class_name()== User.__name__
    assert vasia.get_hello_world == 'hello world'

