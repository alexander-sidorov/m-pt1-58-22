import time

def task_01_do_twice(func):
    def w(lst):
        func(lst)
        func(lst)
        return lst
    return w


@task_01_do_twice
def f(lst):
    lst.append(1)

counter = {}


def task_02_count_calls(counter):
    def wrapper(func):
        def inside(*ar, **kw):
            resault = func(*ar, **kw)
            counter[func.__name__] = counter.get(func.__name__, 0) + 1
            return resault

        return inside

    return wrapper


@task_02_count_calls(counter)
def f():
    pass


@task_02_count_calls(counter)
def g():
    pass


def test_02():
    assert not counter
    [(f(), g()) for _ in "123"]
    [f() for _ in "123"]
    assert counter["f"] == 6
    assert counter["g"] == 3
