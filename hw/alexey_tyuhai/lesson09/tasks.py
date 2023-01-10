import time
from typing import Any
from typing import Callable


def task_01_do_twice(func: Callable) -> Callable:
    def w(*args: Any, **kwargs: Any) -> None:
        func(*args, **kwargs)
        func(*args, **kwargs)
        return None

    return w


counter: dict = {}


def task_02_count_calls(func: Callable) -> Callable:
    def w(*args: Any, **kwargs: Any) -> None:
        counter[func.__name__] = counter.get(func.__name__, 0) + 1
        func(*args, **kwargs)
        return None

    return w


cache_benchmark: dict = {}


def task_03_benchmark(func: Callable) -> Callable:
    def w(*args: Any, **kwargs: Any) -> Any:
        t_start = time.monotonic()
        func_result = func(*args, **kwargs)
        dt = time.monotonic() - t_start
        cache_benchmark[func.__name__] = dt
        return func_result

    return w


def task_04_typecheck(func: Callable) -> Callable:
    def w(**kwargs: Any) -> Any:
        func_result = func(**kwargs)
        keys_list = list(kwargs.keys())
        if len(keys_list) == 2:
            vel_a = keys_list[0]
            vel_b = keys_list[1]
            if not isinstance(kwargs[vel_a], type(kwargs[vel_b])):
                raise TypeError(
                    f"{kwargs[vel_a]} is not of type {type(kwargs[vel_b])}"
                )
        type_return_func = func.__annotations__["return"]
        if not isinstance(func_result, type_return_func):
            raise TypeError(f"{func_result} is not of type {type_return_func}")

        return func_result

    return w


cache_05: dict = {}


def task_05_cache(func: Callable) -> Callable:
    def w(*args: Any, **kwargs: Any) -> Any:
        key = func.__name__ + str(args) + str(kwargs)
        try:
            return cache_05[key]
        except KeyError:
            func_result = func(*args, **kwargs)
            cache_05[key] = func_result
            return func_result

    return w
