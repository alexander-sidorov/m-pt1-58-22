from hw.vladislav_yurenya.lesson09.tasks import task_01_do_twice
from hw.vladislav_yurenya.lesson09.tasks import ask_02_count_calls

def test_01():
    @task_01_do_twice
    def f(lst):
        lst.append(1)

    def test_01():
        x = []
        f(x)
        assert len(x) == 2

def test_02():
    @task_02_count_calls
    def f(): pass

    @task_02_count_calls
    def g(): pass

    def test_02():
        assert not counter
        [ (f(), g()) for _ in "123" ]
        [ f() for _ in "123" ]
        assert counter["f"] == 6
        assert counter["g"] == 3
