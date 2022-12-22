import time
from collections import defaultdict
from typing import Any

import pytest

from hw.jana_sergienko.lesson09.tasks import cache_benchmark
from hw.jana_sergienko.lesson09.tasks import counter
from hw.jana_sergienko.lesson09.tasks import task_01_do_twice
from hw.jana_sergienko.lesson09.tasks import task_02_count_calls
from hw.jana_sergienko.lesson09.tasks import task_03_benchmark
from hw.jana_sergienko.lesson09.tasks import task_04_typecheck
from hw.jana_sergienko.lesson09.tasks import task_05_cache


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
def slowpoke(num: int) -> None:
    time.sleep(num)


def test_task_03_benchmark() -> None:
    slowpoke(1)
    assert abs(cache_benchmark["slowpoke"] - 1) < 0.1


def test_task_04_typecheck() -> None:
    @task_04_typecheck
    def xxx(*, arg: int) -> None:
        pass

    @task_04_typecheck
    def yyy(*, arg: Any) -> None:
        return arg  # type: ignore

    assert xxx(arg=10) is None
    assert yyy(arg=None) is None

    with pytest.raises(TypeError):
        xxx(arg="a")

    with pytest.raises(TypeError):
        yyy(arg="a")


def test_task_05_cache() -> None:
    cache: dict = defaultdict(list)

    @task_05_cache(cache)
    def func1(arg: list) -> list:
        arg.append(1)
        return arg

    data1: list = []
    data2: list = ["x"]

    [func1(data1) for _ in "123"]
    [func1(data2) for _ in "123"]
    assert cache.get(func1.__name__) == [
        [
            ([1],),
            {},
            [1],
        ],
        [
            (["x", 1],),
            {},
            ["x", 1],
        ],
    ]

    ret = func1(data1)
    assert ret == [1]

    cached_calls = cache.get(func1.__name__)
    assert isinstance(cached_calls, list)
    assert [([1],), {}, ret] in cached_calls
