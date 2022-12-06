from hw.alexander_sidorov import helpers


def test_helpers() -> None:
    assert len(helpers.ATTRS_NO_TEST) == 32
    assert len(helpers.CITIES) == 28
