from typing import Callable

T = str


def create() -> T:
    return "result of create()"


def repeat() -> T:
    return create()


def refer() -> Callable[[], T]:
    return create


# ------------------------------------------------------


alice = create()
bob = repeat()
charlie = refer()

assert alice is bob
assert alice is not charlie

assert alice is not create
assert bob is not repeat
assert charlie is not refer

assert charlie is create
