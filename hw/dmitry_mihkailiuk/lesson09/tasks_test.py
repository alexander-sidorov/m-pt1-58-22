import time

import pytest

from hw.dmitry_mihkailiuk.lesson09.tasks import counter
from hw.dmitry_mihkailiuk.lesson09.tasks import task_01_do_twice
from hw.dmitry_mihkailiuk.lesson09.tasks import task_02_count_calls
from hw.dmitry_mihkailiuk.lesson09.tasks import task_03_benchmark
from hw.dmitry_mihkailiuk.lesson09.tasks import task_04_typecheck
from hw.dmitry_mihkailiuk.lesson09.tasks import task_05_cache


@task_01_do_twice
def f_do(lst: list) -> None:
    lst.append(1)


def test_01() -> None:
    x_list: list = []
    f_do(x_list)
    assert len(x_list) == 2


@task_02_count_calls
def f_count() -> None:
    pass


@task_02_count_calls
def g_count() -> None:
    pass


def test_02() -> None:
    assert not counter
    [(f_count(), g_count()) for _ in "123"]
    [f_count() for _ in "123"]
    assert counter["f_count"] == 6
    assert counter["g_count"] == 3


@task_03_benchmark
def slowpoke(number: int) -> None:
    time.sleep(number)


def test_03() -> None:
    t_start = time.monotonic()
    slowpoke(1)
    dt = time.monotonic() - t_start
    t_cache = time.monotonic()
    slowpoke(1)
    dt_cache = time.monotonic() - t_cache
    assert dt_cache < dt


@task_04_typecheck
def f_type(*, a_type: int, b_type: int) -> int:
    return b_type * a_type


@task_04_typecheck
def g_type() -> int:
    return "1"  # type: ignore


def test_04() -> None:
    assert f_type(a_type=2, b_type=3) == 6

    with pytest.raises(TypeError):
        f_type(a_type=2, b_type=0.2)

    with pytest.raises(TypeError):
        g_type()


@task_05_cache
def bad(x_cache: list = []) -> list:
    x_cache.append(1)
    return x_cache


def test_05() -> None:
    y_cache = bad()
    assert y_cache == [1]

    z_cache = [bad() for _ in "123"][-1]
    assert z_cache is y_cache

    data = [1, 2, 3, 4]
    r1 = bad(data)
    r2 = bad(data)
    r3 = bad([1, 2])
    assert data == [1, 2, 3, 4, 1, 1]
    assert r1 is data
    assert r2 is r1
    assert r3 is not r1
    assert r3 == [1, 2, 1]
