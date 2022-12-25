import time

import pytest

from hw.vladislav_yurenya.lesson09.tasks import dec
from hw.vladislav_yurenya.lesson09.tasks import task_01_do_twice
from hw.vladislav_yurenya.lesson09.tasks import task_03_benchmark
from hw.vladislav_yurenya.lesson09.tasks import task_04_typecheck
from hw.vladislav_yurenya.lesson09.tasks import task_05_cache


def test_01() -> None:
    @task_01_do_twice
    def func(data: list) -> None:
        data.append(1)

    xxx: list = []
    func(xxx)
    assert xxx == [1, 1]


def test_03() -> None:
    benchmarks: dict = {}

    @task_03_benchmark(benchmarks)
    def slowpoke(timeout: int) -> None:
        time.sleep(timeout)

    t0 = time.monotonic()
    slowpoke(1)
    dt = time.monotonic() - t0
    assert abs(dt - 1) < 0.1


@task_04_typecheck
def f(*, a: int, b: int) -> int:
    return b * a


@task_04_typecheck
def g() -> int:
    return "1"  # type: ignore


def test_04() -> None:
    assert f(a=2, b=3) == 6

    with pytest.raises(TypeError):
        f(a=2, b=0.2)

    with pytest.raises(TypeError):
        g()


@task_05_cache
def bad(x_lst: list = []) -> list:  # noqa: B006
    x_lst.append(1)
    return x_lst


def test_05() -> None:
    y_x = bad()
    assert y_x == [1]
    z_bad = [bad() for _ in "123"][-1]
    assert z_bad is y_x
    data = [1, 2, 3, 4]
    r1 = bad(data)
    r2 = bad(data)
    r3 = bad([1, 2])
    assert data == [1, 2, 3, 4, 1, 1]
    assert r1 is data
    assert r2 is r1
    assert r3 is not r1
    assert r3 == [1, 2, 1]


counter: dict = {}


@dec(counter)
def f_count() -> None:
    pass


@dec(counter)
def g_count() -> None:
    pass


def test_02() -> None:
    assert not counter
    [(f_count(), g_count()) for _ in "123"]
    [f_count() for _ in "123"]
    assert counter["f_count"] == 6
    assert counter["g_count"] == 3
