import time


from hw.jana_sergienko.lesson09.tasks import counter
from hw.jana_sergienko.lesson09.tasks import task_01_do_twice
from hw.jana_sergienko.lesson09.tasks import task_02_count_calls
from hw.jana_sergienko.lesson09.tasks import task_03_benchmark


@task_01_do_twice
def f01(lst: list) -> None:
    lst.append(1)


def test_task_01_do_twice() -> None:
    x01: list[None] = []
    f01(x01)
    assert len(x01) == 2


@task_02_count_calls
def f_count() -> None:
    pass


@task_02_count_calls
def g_count() -> None:
    pass


def test_task_02_count_calls() -> None:
    assert not counter
    [(f_count(), g_count()) for _ in "123"]
    [f_count() for _ in "123"]
    assert counter["f_count"] == 6
    assert counter["g_count"] == 3


@task_03_benchmark
def slowpoke(n):
    time.sleep(n)


def test_task_03_benchmark():
    t = time.monotonic()
    slowpoke(1)
    dt = time.monotonic() - t
    assert abs(dt - 1) < 0.1
