import time
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
        result_func = func(*args, **kwargs)
        result = time.monotonic() - t_start
        cache_benchmark[func.__name__] = result
        return result_func

    return wrapper
