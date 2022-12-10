from random import randint
from typing import Callable

T = str
R = randint(0, 10)
alice = f"Alice in Wonderland {R}"


def echo(arg_of_echo: T) -> T:
    return arg_of_echo


def run(action: Callable[[T], T], arg_of_run: T) -> T:
    return action(arg_of_run)


bob = echo(alice)
charlie = run(echo, alice)

global_namespace = globals()

# --------------------------------------


assert bob == alice
assert bob is alice
assert charlie == alice
assert charlie is alice

assert alice is not echo
assert bob is not echo
assert charlie is not run

assert "echo" in global_namespace
assert "arg_of_echo" not in global_namespace

assert "run" in global_namespace
assert "action" not in global_namespace
assert "arg_of_run" not in global_namespace
