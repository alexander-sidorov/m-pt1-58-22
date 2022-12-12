from typing import Hashable

my_str = "maksimov"
my_tuple = ("igor", "yigal", "maksimov")
my_list = ["igor", "imri", "orly"]
my_set = {"yigal", "igor", "imri"}
my_dict = {"name": "Yigal", "age": "39", "sex": "male"}


def stdtypes_test() -> None:
    assert "maksi" + "mov" == "maksimov"
    assert "z" not in my_str
    assert my_str[5] == "m"
    assert len(my_str) == 8
    assert isinstance(my_str, Hashable)
    assert not my_str.isdecimal()
    assert not my_str.isdigit()
    assert my_str.capitalize() == "Maksimov"
    assert my_str.count("m") == 2
    assert my_str.index("a") == 1
    assert my_str.find("ksi") == 2
    assert my_str.endswith("v")
    assert my_str.ljust(10, "*") == "maksimov**"
    assert my_str.islower()
    assert "%".join(my_str) == "m%a%k%s%i%m%o%v"
    assert my_str.replace("maks", "abc") == "abcimov"
    assert my_str.title() == "Maksimov"
    assert len(my_tuple) == 3
    assert my_tuple.count("igor") == 1
    assert isinstance(my_tuple, Hashable)
    assert my_tuple[2] == "maksimov"
    assert len(my_set) < 5
    assert not isinstance(my_set, Hashable)
    assert not isinstance(my_dict, Hashable)
    assert len(my_dict) > 2
    assert my_dict.get("name") == "Yigal"
