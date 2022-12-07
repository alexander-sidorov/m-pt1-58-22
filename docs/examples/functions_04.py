from typing import Callable

T = str

text = "some text"


def repeat() -> T:
    name_in_repeat = text
    return name_in_repeat


def run(action: Callable[[], T]) -> T:
    return action()


alice = repeat()
bob = run(repeat)

global_namespace = globals()

# ------------------------------------------

assert alice is not repeat
assert bob is not repeat
assert alice == bob
assert alice is bob

assert "alice" in global_namespace
assert "bob" in global_namespace
assert "T" in global_namespace
assert "Callable" in global_namespace
assert "repeat" in global_namespace
assert "run" in global_namespace

assert "name_in_repeat" not in global_namespace
assert "action" not in global_namespace
