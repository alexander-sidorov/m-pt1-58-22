import time
from typing import Any
from typing import cast

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


def test_04() -> None:
    @task_04_typecheck
    def xxx(*, arg: int) -> None:
        assert arg > 0 or arg <= 0

    @task_04_typecheck
    def yyy(*, arg: Any) -> None:
        return cast(None, arg)

    assert xxx(arg=10) is None
    assert yyy(arg=None) is None

    with pytest.raises(TypeError):
        xxx(arg="a")

    with pytest.raises(TypeError):
        yyy(arg="a")



@task_05_cache
def bad(x_lst: list = []) -> list:
    x_lst.append(1)
    return x_lst


def test_05()->None:
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
