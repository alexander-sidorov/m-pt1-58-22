import time
from typing import Any
from typing import Callable


def task_01_do_twice(func: Callable) -> Callable:
    def inside(lst):
        func(lst)
        func(lst)

    return inside


benchmarks: dict = {}


def task_03_benchmark(benchmarks):
    def rex(func):
        def inside(*ar, **kw):
            start = time.monotonic()
            resault = func(*ar, **kw)
            end = time.monotonic()
            total = end - start
            benchmarks[func.__name__] = total
            return resault

        return inside

    return rex


def task_04_typecheck(func: Callable) -> Callable:
    def inside(**kw: Any) -> Any:
        lst = list(kw.values())
        resault = func(**kw)
        for i in range(len(lst)):
            if not isinstance(lst[i], type(lst[i - 1])):
                raise TypeError(f"{lst[i-1]=!r} is not of type {lst[i]}")
        type_func = func.__annotations__["return"]
        if not isinstance(type_func, type(resault)):
            raise TypeError(f"{resault} is not of type {type_func}")
        return resault

    return inside
