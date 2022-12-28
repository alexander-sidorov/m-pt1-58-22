import time
from typing import Any
from typing import Callable


def task_01_do_twice(func: Callable) -> Callable:
    def inside(lst: list) -> list:
        func(lst)
        func(lst)
        return lst

    return inside


benchmarks: dict = {}


def task_03_benchmark(benchmarks: dict) -> Callable:
    def rex(func: Callable) -> Callable:
        def inside(*ar: Any, **kw: Any) -> Any:
            start = time.monotonic()
            result = func(*ar, **kw)
            end = time.monotonic()
            total = end - start
            benchmarks[func.__name__] = total
            return result

        return inside

    return rex


def task_04_typecheck(func: Callable) -> Callable:
    def inside(**kw: Any) -> Any:
        lst = list(kw.values())
        result = func(**kw)
        for i in range(len(lst)):
            if not isinstance(lst[i - 1], type(lst[i])):
                raise TypeError(f"{lst[i-1]=!r} is not of type {lst[i]}")
        type_func = func.__annotations__["return"]
        if not isinstance(type_func, type(result)):
            raise TypeError(f"{result} is not of type {type_func}")
        return result

    return inside


cache = {}


def task_05_cache(func: Callable) -> Callable:
    def inside(*args: Any, **kwargs: Any) -> Any:
        key = func.__name__ + str(args) + str(kwargs)
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return inside


counter: dict[str, int] = {}


def dec(counter: dict) -> Callable:
    def task_02_count_calls(func: Callable) -> Callable:
        def inside(*args: Any, **kwargs: Any) -> None:
            counter[func.__name__] = counter.get(func.__name__, 0) + 1
            func(*args, **kwargs)
            return None

        return inside

    return task_02_count_calls
