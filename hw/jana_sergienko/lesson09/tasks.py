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
    @wraps
    def wrapper(**kwargs: Any) -> Any:
        result_func = func(**kwargs)
        an_func = func.__annotations__
        for key, value in kwargs.items():
            if an_func[key] is Any:
                continue
            if not isinstance(value, an_func[key]):
                raise TypeError(f"{value=!r} "
                                f"is not of type {an_func[key]}")
        if not isinstance(result_func, type(an_func["return"])):
            raise TypeError(f"{result_func=!r} "
                            f"is not of type {an_func['return']}")
        return result_func

    return wrapper
