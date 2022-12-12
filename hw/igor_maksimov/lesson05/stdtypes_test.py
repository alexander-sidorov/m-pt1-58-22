from typing import Hashable


def stdtypes_test() -> None:
    assert "maksi" + "mov" == "maksimov"
    assert "z" not in "maksimov"
    assert "maksimov"[5] == "m"
    assert isinstance('maksimov', Hashable)
    assert "maksimov".capitalize() == "Maksimov"
    assert 'maksimov'.count('m') == 2
    assert "maksimov".index("a") == 1
    assert "maksimov".find('ksi') == 2


stdtypes_test()
