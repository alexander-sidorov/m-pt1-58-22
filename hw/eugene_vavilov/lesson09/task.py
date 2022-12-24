import time
from typing import Any
from typing import Callable


def task_01_do_twice(original_func: Callable) -> Callable:
    def wrapper(lst: list) -> None:
        original_func(lst)
        original_func(lst)

    return wrapper


@task_01_do_twice
def task_01(lst: list) -> None:
    lst.append(1)


counter: dict = {}


def task_02_count_calls(func: Any) -> Callable:
    func_name = func.__name__

    def wrapper() -> None:
        if func_name in counter:
            counter[func_name] += 1
        else:
            counter[func_name] = 1

    func()
    return wrapper


@task_02_count_calls
def f02() -> None:
    pass


@task_02_count_calls
def g02() -> None:
    pass


def test_03_benchmark(func: Callable) -> Callable:
    def wrapper(sleep_time: int) -> float:
        lets_start = time.monotonic()
        func(sleep_time)
        return time.monotonic() - lets_start

    return wrapper


@test_03_benchmark
def slowpoke(sleep_time: int) -> None:
    time.sleep(sleep_time)


def task_04_typecheck(func: Callable) -> Callable:
    def wrapper(**kwargs: Any) -> Any:
        result = func(**kwargs)
        annotations = func.__annotations__
        for annotation in annotations:
            try:
                if type(kwargs[annotation]) != annotations[annotation]:
                    raise TypeError(
                        f"{kwargs[annotation]!r} is not of type {annotations[annotation]}"  # noqa E501
                    )
            except KeyError:
                if type(result) != annotations[annotation]:
                    raise TypeError(
                        f"{result!r} is not of type {annotations[annotation]}"
                    )
        return result

    return wrapper


@task_04_typecheck
def f04(*, a: int, b: int) -> int:
    return b * a


@task_04_typecheck
def g04() -> int:
    return "1"  # type: ignore


cache: dict = {}


def task_05_cache(func: Callable) -> Callable:
    def wrapper(*args: Any) -> Any:
        key = func.__name__ + str(*args)
        if key in cache:
            return cache[key]
        else:
            func_result = func(*args)
            cache[key] = func_result
            return func_result

    return wrapper


@task_05_cache
def bad(x: list = []) -> Any:  # noqa: VNE001, B006
    x.append(1)
    return x
