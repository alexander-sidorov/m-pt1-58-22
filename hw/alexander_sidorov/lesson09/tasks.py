import time
from functools import wraps
from typing import Any
from typing import Callable
from typing import ParamSpec
from typing import TypeVar
from typing import cast

UNDEFINED = object()

T = TypeVar("T")
P = ParamSpec("P")  # noqa: VNE001


def task_01_do_twice(func: Callable[P, T]) -> Callable[P, tuple[T, T]]:
    @wraps(func)
    def wrapper(*args: P.args, **kw: P.kwargs) -> tuple[T, T]:
        r1 = func(*args, **kw)
        r2 = func(*args, **kw)
        return (r1, r2)

    return wrapper


def task_02_count_calls(
    counter: dict[str, int]
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kw: P.kwargs) -> T:
            count = counter.get(func.__name__, 0)
            counter[func.__name__] = count + 1
            return func(*args, **kw)

        return wrapper

    return decorator


def task_03_benchmark(
    storage: dict[str, float]
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kw: P.kwargs) -> T:
            t0 = time.monotonic()
            try:
                return func(*args, **kw)
            finally:
                dt = time.monotonic() - t0
                storage[func.__name__] = dt

        return wrapper

    return decorator


def typecheck(value: Any, typ: Any, msg: str = "") -> None:
    if typ is UNDEFINED or typ is Any:
        return
    if value is None and typ is None:
        return

    if not isinstance(value, typ):
        errmsg = f"{value!r} is not of type {typ!r}"
        if msg:  # pragma: no cover
            errmsg = f"{msg}: {errmsg}"
        raise TypeError(errmsg)


def task_04_typecheck(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        if args:
            raise TypeError("positional arguments are not allowed")

        anno = func.__annotations__

        for param, value in kwargs.items():
            typ = anno.get(param, UNDEFINED)
            typecheck(value, typ, f"param {param} type error")

        result = func(**kwargs)

        typ_return = anno.get("return", UNDEFINED)
        typecheck(result, typ_return, f"{func.__name__} return type error")

        return result

    return wrapper


def task_05_cache(
    cache: dict[str, list[tuple[P.args, P.kwargs, T]]]
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kw: P.kwargs) -> T:
            saves = cache.setdefault(func.__name__, [])
            result: Any = UNDEFINED

            for saved_args, saved_kwargs, saved_result in saves:
                if saved_args == args and saved_kwargs == saved_kwargs:
                    result = saved_result
                    break

            if result is UNDEFINED:
                result = func(*args, **kw)
                call = (args, kw, result)
                saves.append(call)

            assert result != UNDEFINED
            return cast(T, result)

        return wrapper

    return decorator
