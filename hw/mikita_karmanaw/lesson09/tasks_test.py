import time
from typing import Any

import pytest

from hw.mikita_karmanaw.lesson09.tasks import cache_factory
from hw.mikita_karmanaw.lesson09.tasks import counter_cache_factory
from hw.mikita_karmanaw.lesson09.tasks import func_cache_factory
from hw.mikita_karmanaw.lesson09.tasks import task_01_do_twice
from hw.mikita_karmanaw.lesson09.tasks import task_04_typecheck
from hw.mikita_karmanaw.lesson09.tasks import time_cache_factory


@task_01_do_twice
def f01(lst: list) -> None:
    lst.append(1)


def test_01() -> None:
    x01: list[None] = []
    f01(x01)
    assert len(x01) == 2


function_counter_cache: dict[str, int] = {}


@counter_cache_factory(function_counter_cache)
def f02() -> None:
    pass


@counter_cache_factory(function_counter_cache)
def g02() -> None:
    pass


def test_02() -> None:
    assert not function_counter_cache
    [(f02(), g02()) for _ in "123"]
    [f02() for _ in "123"]
    assert function_counter_cache["f02"] == 6
    assert function_counter_cache["g02"] == 3


function_time_cache: dict[str, float] = {}


@time_cache_factory(function_time_cache)
def slowpoke(n03: int) -> None:
    time.sleep(n03)


def test_03() -> None:
    slowpoke(1)
    assert abs(function_time_cache["slowpoke"] - 1) < 0.05


function_result_cache: dict[str, Any] = {}


@func_cache_factory(function_result_cache)
def bad(x05: list = []) -> list:
    x05.append(1)
    return x05


def test_05() -> None:
    y05 = bad()
    assert y05 == [1]

    z05 = [bad() for _ in "123"][-1]
    assert z05 is y05

    data = [1, 2, 3, 4]
    r1 = bad(data)
    r2 = bad(data)
    r3 = bad([1, 2])
    assert data == [1, 2, 3, 4, 1]
    assert r1 is data
    assert r2 is r1
    assert r3 is not r1
    assert r3 == [1, 2, 1]


func_total_cache: dict[str, list] = {}


@cache_factory(func_total_cache)
def cached_function(value: int) -> str:
    time.sleep(1)
    return "a" + str(value)


def test_cache() -> None:
    assert not func_total_cache
    cached_function(5)
    assert "cached_function&argument=&5" in func_total_cache
    assert func_total_cache["cached_function&argument=&5"] is list
    assert func_total_cache["cached_function&argument=&5"][0] == 6
    assert func_total_cache["cached_function&argument=&5"][1] > 1
    assert func_total_cache["cached_function&argument=&5"][2] == 1


@task_04_typecheck
def f04(*, a: int, b: int) -> int:
    return b * a


@task_04_typecheck
def g04() -> int:
    return "1"  # type: ignore


def test_04() -> None:
    assert f04(a=2, b=3) == 6

    with pytest.raises(TypeError):
        f04(a=2, b=0.2)

    with pytest.raises(TypeError):
        g04()
