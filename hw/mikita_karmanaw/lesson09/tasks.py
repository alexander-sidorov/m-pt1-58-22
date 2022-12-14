import time
from typing import Any
from typing import Callable


def task_01_do_twice(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


def counter_cache_factory(counter_cache: dict) -> Callable:
    def task_02_count_calls(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                counter_cache[func.__name__] += 1
            except KeyError:
                counter_cache[func.__name__] = int(1)
            return func(*args, **kwargs)

        return wrapper

    return task_02_count_calls


def func_cache_factory(func_cache: dict) -> Callable:
    def task_05_cache(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            ar = str(args) + str(kwargs)
            try:
                return func_cache[ar]
            except KeyError:
                res = func(*args, **kwargs)
                func_cache[ar] = res
                return res

        return wrapper

    return task_05_cache


def time_cache_factory(time_cache: dict) -> Callable:
    def task_03_benchmark(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            t_start = time.perf_counter()
            res = func(*args, **kwargs)
            time_spent = time.perf_counter() - t_start
            time_cache[func.__name__] = time_spent
            return res

        return wrapper

    return task_03_benchmark


def cache_factory(cache: dict) -> Callable:
    def cache_func(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            cache_key = func.__name__ + "&argument=&" + str(args) + str(kwargs)
            try:
                result = cache[cache_key]
                cache[cache_key][2] += 1
                return result
            except KeyError:
                time_start_count = time.perf_counter()
                result = func(*args, **kwargs)
                time_spent = time.perf_counter() - time_start_count
                cache[cache_key] = [result, time_spent, int(1)]
            return result

        return wrapper

    return cache_func


def task_04_typecheck(func: Callable) -> Callable:
    def wrapper(**kwargs: Any) -> Any:
        result = func(**kwargs)
        annotations = func.__annotations__
        try:
            return_type = annotations["return"]
            if not isinstance(result, return_type):
                raise TypeError(f"{result!r} is not of type {return_type}")
            annotations.__delitem__("return")
        except KeyError:
            pass
        for annotation in annotations:
            var_arg = kwargs[annotation]
            var_type = annotations[annotation]
            if not isinstance(var_arg, var_type):
                raise TypeError(f"{var_arg!r} is not of type {var_type}")
        return result

    return wrapper
