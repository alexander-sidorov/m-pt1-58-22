from random import randint

T = str
R = randint(0, 10)
alice = f"Alice in Wonderland {R}"


def run_outer(arg_of_outer: T) -> T:
    def run_inner(arg_of_inner: T) -> T:
        return arg_of_inner

    return run_inner(arg_of_outer)


bob = run_outer(alice)

global_namespace = globals()

# --------------------------------------

assert bob == alice
assert bob is alice

assert "run_outer" in global_namespace
assert "arg_of_outer" not in global_namespace
assert "T" in global_namespace

assert "run_inner" not in global_namespace
assert "arg_of_inner" not in global_namespace
