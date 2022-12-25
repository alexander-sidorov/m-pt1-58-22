import time
from typing import Any
from typing import cast

import pytest

from hw.alexander_sidorov.lesson09.tasks import task_01_do_twice
from hw.alexander_sidorov.lesson09.tasks import task_02_count_calls
from hw.alexander_sidorov.lesson09.tasks import task_03_benchmark
from hw.alexander_sidorov.lesson09.tasks import task_04_typecheck
from hw.alexander_sidorov.lesson09.tasks import task_05_cache


def test_01() -> None:
    @task_01_do_twice
    def func(data: list) -> None:
        data.append(1)

    xxx: list = []
    func(xxx)

    assert xxx == [1, 1]


def test_02() -> None:
    calls: dict = {}

    @task_02_count_calls(calls)
    def func1() -> None:
        pass

    @task_02_count_calls(calls)
    def func2() -> None:
        pass

    [func1() for _ in "123"]
    [(func1(), func2()) for _ in "123"]

    assert calls == {
        func1.__name__: 6,
        func2.__name__: 3,
    }


def test_03() -> None:
    benchmarks: dict = {}

    @task_03_benchmark(benchmarks)
    def slowpoke(timeout: int) -> None:
        time.sleep(timeout)

    t0 = time.monotonic()
    slowpoke(1)
    dt = time.monotonic() - t0

    assert abs(dt - 1) < 0.1

    bt = benchmarks.get(slowpoke.__name__)
    assert isinstance(bt, float)
    assert abs(dt - bt) < 0.1


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
        xxx("a")  # type: ignore

    with pytest.raises(TypeError):
        xxx(arg="a")  # type: ignore

    with pytest.raises(TypeError):
        yyy(arg="a")


def test_05() -> None:
    cache: dict = {}

    @task_05_cache(cache)  # type: ignore
    def func1(arg: list) -> list:
        arg.append(1)
        return arg

    data1: list = []
    data2: list = ["x"]

    [func1(data1) for _ in "123"]  # type: ignore
    [func1(data2) for _ in "123"]  # type: ignore
    assert cache.get(func1.__name__) == [
        (
            ([1],),
            {},
            [1],
        ),
        (
            (["x", 1],),
            {},
            ["x", 1],
        ),
    ]

    ret = func1(data1)  # type: ignore
    assert ret == [1]

    cached_calls = cache.get(func1.__name__)
    assert isinstance(cached_calls, list)
    assert (([1],), {}, ret) in cached_calls


if __name__ == "__main__":
    test_05()
