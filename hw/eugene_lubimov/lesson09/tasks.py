from functools import wraps
from typing import Any
from typing import Callable

counter: dict = {}


def task_01_do_twice(func: Callable) -> Callable:
    def wrapper(
        *args: tuple,
    ) -> None:
        func(
            *args,
        )
        func(
            *args,
        )

    return wrapper


def task_02_count_calls(counter: dict) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: tuple) -> Any:
            res = func(
                *args,
            )
            counter[func.__name__] = counter.get(func.__name__, 0) + 1

            return res

        return inner

    return wrapper


def task_03_benchmark(benchmark: dict) -> Callable:

    import time

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: tuple) -> Any:
            start = time.monotonic()
            res = func(*args)
            time_work = time.monotonic() - start
            benchmark[func.__name__] = time_work

            return res

        return inner

    return wrapper


def task_04_typecheck(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(**kwargs: dict) -> Any:
        res = func(**kwargs)
        annot = func.__annotations__
        for key, value in kwargs.items():
            if annot[key] is Any:
                continue
            if not isinstance(value, annot[key]):
                raise TypeError(f"{value=!r} is not of type {annot[key]}")

        if not isinstance(res, type(annot["return"])):
            raise TypeError(f"{res=!r} is not of type {annot['return']}")
        return res

    return wrapper


def task_05_cache(cash: dict) -> Callable:
    def dec(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            runs = cash.get(func.__name__)
            if runs is not None:
                for run in runs:
                    arg, kwarg, result = run
                    if arg == args and kwarg == kwargs:
                        return result
            res = func(*args, **kwargs)
            cash[func.__name__].append([args, kwargs, res])
            return res

        return wrapper

    return dec
