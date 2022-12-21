def func():
    return -1


def decor(func):
    def wrapper():
        try:
            func()
        except AssertionError:
            pass
        return None
    return None
