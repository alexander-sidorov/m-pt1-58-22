import time
from typing import Any
from typing import Callable


def fabric_benchmark(cashe_dict: dict) -> Callable:
    def cashe_creator(func: Callable) -> Callable:
        def inner(*args: tuple, **kwargs: dict) -> Any:
            inner.__name__ = func.__name__
            start_time = time.monotonic()
            res = func(*args, **kwargs)
            cashe_dict[inner.__name__] = time.monotonic() - start_time
            return res

        return inner

    return cashe_creator


def cashe_factory(cashe_dict: dict) -> Callable:
    def cashe_creator(func: Callable) -> Callable:
        cashe_dict[func.__name__] = []

        def inner(*args: tuple, **kwargs: dict) -> Any:
            inner.__name__ = func.__name__
            is_cashe = cashe_dict[func.__name__]
            for cash in is_cashe:
                if args in cash and kwargs in cash:
                    return cash[2]
            res = func(*args, **kwargs)
            temp_list: list = [args, kwargs, res]
            cashe_dict[func.__name__].append(temp_list)
            return res

        return inner

    return cashe_creator


def typecheck(func: Callable) -> Callable:
    def checker(**kwargs: dict) -> Any:
        checker.__name__ = func.__name__
        res = func(**kwargs)
        func_annot = func.__annotations__
        for key, num in kwargs.items():
            if func_annot[key] is not Any:  # noqa SIM102
                if not isinstance(num, func_annot[key]):
                    raise TypeError(
                        f"{num=!r} is not of type {func_annot[key]}"
                    )
            if not isinstance(res, type(func_annot["return"])):
                raise TypeError(
                    f"{res=!r} is not of type {func_annot['return']}"
                )
        return res

    return checker


def counter_factory(counter_dict: dict) -> Callable:
    def counter(func: Callable) -> Callable:
        counter_dict.setdefault(func.__name__, 0)

        def call_counter() -> Any:
            call_counter.__name__ = func.__name__
            res = func()
            counter_dict[func.__name__] += 1
            return res

        return call_counter

    return counter


def do_twice(func: Callable) -> Callable:
    def doubler(*args: tuple, **kwargs: dict) -> str:
        text = func(*args, **kwargs)
        restart = func(*args, **kwargs)
        return f"{text}{restart}"

    return doubler
