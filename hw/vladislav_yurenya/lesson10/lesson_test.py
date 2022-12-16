from hw.vladislav_yurenya.lesson10.lesson import User
def task_01()->None:
    txt='hello word'
    name='zhora'
    zhora=User('Петя')
    vasya=User('Вася')
    assert zhora.get_name()=='Петя'
    assert zhora.get_class_name() == User.__name__
    assert zhora.get_hello_word() == txt
    assert vasya.get_name() == 'Вася'
    assert vasya.get_class_name() == User.__name__
    assert vasya.get_hello_word() == txt

