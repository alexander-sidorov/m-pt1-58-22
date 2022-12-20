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
        counter[func.__name__] = 0
        if (wrapper):
            counter[func.__name__] += 1
        func(*args, **kwargs)
        return None

    return wrapper
