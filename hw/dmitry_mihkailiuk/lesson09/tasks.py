import functools
from typing import Any
from typing import Callable


def task_01_do_twice(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        func(*args, **kwargs)
        func(*args, **kwargs)
        return None

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
        if func.__name__ in cache_benchmark:
            return cache_benchmark[func.__name__]
        else:
            cache_benchmark[func.__name__] = func(*args, **kwargs)
            return func(*args, **kwargs)

    return wrapper


def task_04_typecheck(func: Callable) -> Callable:
    def wrapper(**kwargs: Any) -> Any:
        func_result = func(**kwargs)
        keys_list = list(kwargs.keys())
        a = keys_list[0]
        b = keys_list[1]
        if not isinstance(kwargs[a], type(kwargs[b])):
            raise TypeError(f"{kwargs[a]} is not of type {type(kwargs[b])}")
        else:
            type_return_func = func.__annotations__["return"]
            if not isinstance(func_result, type_return_func):
                raise TypeError(
                    f"{func_result} is not of type {type_return_func}"
                )

        return func_result

    return wrapper


cache_05: dict = {}


def task_05_cache(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = func.__name__ + str(args) + str(kwargs)
        if key is cache_05:
            return cache_05[key]
        else:
            func_result = func(*args, **kwargs)
            cache_05[key] = func_result
            return func_result

    return wrapper
