from random import randint
from typing import Callable

T = str
R = randint(0, 10)
alice = f"Alice in Wonderland {R}"


def run_outer(arg_of_outer: T) -> Callable[[T], T]:
    def run_inner(arg_of_inner: T) -> T:
        return arg_of_inner + arg_of_outer

    return run_inner


bob = run_outer(alice)
charlie = bob(alice)

# ---------------------------------

assert bob != alice
assert bob is not alice

assert alice in charlie
assert charlie not in alice

assert alice * 2 in charlie
