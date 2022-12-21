def func() -> int:
    return -1


def decor(func) -> None:
    def wrapper() -> None:
        try:
            func()
        except AssertionError:  # noqa: SIM105
            pass
        return None

    return None
