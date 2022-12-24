import time
from functools import wraps
from typing import Any
from typing import Callable


def task_01_do_twice(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


counter: dict = {}


def task_02_count_calls(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        counter[func.__name__] = counter.get(func.__name__, 0) + 1
        func(*args, **kwargs)
        return None

    return wrapper


cache_benchmark: dict = {}


def task_03_benchmark(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        t_start = time.monotonic()
        func_result = func(*args, **kwargs)
        result = time.monotonic() - t_start
        cache_benchmark[func.__name__] = result
        return func_result

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
