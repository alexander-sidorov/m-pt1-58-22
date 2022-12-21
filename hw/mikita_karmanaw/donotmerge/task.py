from typing import Callable


def func() -> int:
    return -1


def decor(function: Callable) -> None:
    def wrapper() -> None:
        try:  # noqa: SIM105
            function()
        except AssertionError:  # noqa: SIM105
            pass
        return None

    return None
