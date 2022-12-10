def append(arg: list) -> list:
    name = arg
    name.append("+")
    return name


alice = ["alice"]
id_alice = id(alice)

bob = append(alice)
id_bob = id(bob)

global_namespace = globals()

# ----------------------------------------------------------------------------

assert alice != []
assert alice == bob
assert alice is bob


assert "append" in global_namespace
assert "alice" in global_namespace
assert "bob" in global_namespace
assert "arg" not in global_namespace
assert "name" not in global_namespace
