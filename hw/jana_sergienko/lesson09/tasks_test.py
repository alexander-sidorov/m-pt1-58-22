import time
from typing import Any

import pytest

from hw.jana_sergienko.lesson09.tasks import cache_benchmark
from hw.jana_sergienko.lesson09.tasks import counter
from hw.jana_sergienko.lesson09.tasks import task_01_do_twice
from hw.jana_sergienko.lesson09.tasks import task_02_count_calls
from hw.jana_sergienko.lesson09.tasks import task_03_benchmark
from hw.jana_sergienko.lesson09.tasks import task_04_typecheck


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
