def append(arg: list = []) -> list:
    name = arg
    name.append("+")
    return name


alice = append()
id_alice = id(alice)

bob = append()
id_bob = id(bob)

charlie = append()
id_charlie = id(charlie)

dan = append()
id_dan = id(dan)

# ----------------------------------------------------------------------------

assert alice != []
assert alice == bob
assert bob is charlie
assert charlie is dan
assert len(dan) == 4
