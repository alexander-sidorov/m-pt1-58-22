from functools import wraps
from typing import Any
from typing import Callable

counter: dict = {}


def task_01_do_twice(func: Callable) -> Callable:
    def wrapper(
        *args,
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
        def inner(*args) -> Callable:
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
        def inner(*args) -> Callable:
            start = time.monotonic()
            res = func(*args)
            time_work = time.monotonic() - start
            benchmark[func.__name__] = time_work

            return res

        return inner

    return wrapper


def task_04_typecheck(func: Callable) -> Callable:
    def wrapper(**kwargs):

        res = func(**kwargs)
        for key, value in kwargs.items():
            if func.__annotations__[key] is Any:
                continue
            if not isinstance(value, func.__annotations__[key]):
                raise TypeError(
                    f"{value=!r} is not of type {func.__annotations__[key]}"
                )
        if func.__annotations__["return"] is res:
            return res
        if not isinstance(res, func.__annotations__["return"]):
            raise TypeError(
                f"{res=!r} is not of type {func.__annotations__['return']}"
            )
        return res

    return wrapper


def task_05_cache(func: Callable) -> Callable:
    cash_dict = {}

    @wraps(func)
    def wrapper(my_list5=[]) -> None:  # noqa: B006

        if (func, id(my_list5)) in cash_dict:
            return cash_dict[(func, id(my_list5))]
        cash_dict[(func, id(my_list5))] = func(my_list5)
        return cash_dict[(func, id(my_list5))]

    return wrapper
