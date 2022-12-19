import time
from typing import Any
from typing import cast

import pytest

from hw.vladislav_yurenya.lesson09.tasks import task_01_do_twice
from hw.vladislav_yurenya.lesson09.tasks import task_03_benchmark
from hw.vladislav_yurenya.lesson09.tasks import task_04_typecheck


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
