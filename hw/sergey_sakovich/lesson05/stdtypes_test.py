from typing import Hashable


def test_stdtypes() -> None:
    str_13 = "python"
    assert "python" < "sfg"
    assert "%s" % 3 == 3  # noqa: S001,MOD001
    assert "python" + "Q" == "pythonQ"
    assert "y" in str_13
    assert str_13[3] == "h"
    assert isinstance(str_13, Hashable)
    assert len(str_13) == 6  # noqa: S001,MOD001
    assert str_13 * 2 == "pythonpython"
    assert str_13 <= str_13
    assert str_13.capitalize() == "Python"
    assert str_13.casefold() == "python"
    assert str_13.center(10) == "**python**"
    assert str_13.count("o") == 1
    assert str_13.encode() == b"python"
    assert str_13.endswith("thon")
    assert "p\tyt\tho\tn".expandtabs() == "p       yt      ho      n"
    assert str_13.find("o") == 4
    assert "{}".format("str_13") == "str_13"
    name = {"name": "str_13"}
    assert "{name} python".format_map(name) == "str_13 python"
    assert str_13.index("t") == 2
    assert str_13.isalnum()
    assert str_13.isalpha()
    assert str_13.isascii()
    assert not str_13.isdecimal()
    assert not str_13.isdigit()
    assert str_13.isidentifier()
    assert str_13.islower()
    assert not str_13.isnumeric()
    assert str_13.isprintable()
    assert not str_13.isspace()
    assert not str_13.istitle()
    assert not str_13.isupper()
    name1 = ".."
    assert name1.join("1..2") != "1........2"
    assert str_13.ljust(10, "s") == "pythonssss"
    assert str_13.lstrip("ptn") == "ython"
    assert str_13.maketrans({"p": "a", "h": "y", "n": "6"}) == {
        112: "a",
        104: "y",
        110: "6",
    }
    assert str_13.partition(".") == ("python", "", "")
    assert str_13.removeprefix("py") == "thon"
    assert str_13.removesuffix("on") == "pyth"
    assert str_13.replace("t", "r") == "pyrhon"
    assert str_13.rfind("yt") == 1
    assert str_13.rindex("th") == 2
    assert str_13.rjust(10, "w") == "wwwwpython"
    assert str_13.rpartition("th") == ("py", "th", "on")
    assert str_13.rsplit("th") == ["py", "on"]
    assert str_13.rstrip("on") == "pyth"
    assert str_13.split() == ["python"]
    name3 = "pyt\nhon"
    assert name3.splitlines() == ["pyt", "hon"]
    assert str_13.startswith("pyt")
    assert str_13.strip("pyon") == "th"
    assert str_13.swapcase() == "PYTHON"
    assert str_13.title() == "Python"
    assert "asd".translate({98: "d"}) == "asd"
    assert str_13.upper() == "PYTHON"
    assert str_13.zfill(10) == "0000python"
    assert str.lower("Python") == 'python'

    list_13 = [1, 9, "python"]

    assert [1] + [9] == [1, 9]
    assert [1] < [9]
    assert not [1] > [9]
    assert not [1] >= [9]
    assert [1] <= [9]
    assert [1] != [9]
    assert [1] not in [9]
    assert not [1] is [9]
    assert list_13[2] == "python"
    assert [19] * 5 == [19, 19, 19, 19, 19]
    list_13.append(13)
    assert list_13 == [1, 9, "python", 13]
    list_13.clear()
    assert not list_13
    assert list_13.copy() == []
    assert list_13.count("o") == 0
    list_13.extend([1, 9, 13])
    assert list_13 == [1, 9, 13]
    assert list_13.index(9) == 1
    list_13.insert(2, 7)
    assert list_13 == [1, 9, 7, 13]
    assert list_13.pop() == 13
    list_13.remove(1)
    assert list_13 == [9, 7]
    list_13.reverse()
    assert list_13 == [7, 9]
    assert list_13.sort() == [7, 9]
    assert not isinstance(list_13, Hashable)
    del list_13[1]
    assert list_13 == [7]
    list_13 += [2]
    assert list_13 == [7, 2]
    list_13 *= 2
    assert list_13 == [7, 2, 7, 2]
    assert len(list_13) == 4
    assert list_13[2] == 7
    tuple_13 = (19, 13, 8, 11)

    assert tuple_13[1] == 13
    assert tuple_13[1:3] == (13, 8)
    assert (1, 2) + (3, 4) == (1, 2, 3, 4)
    assert len(tuple_13) == 4
    assert 13 in tuple_13
    assert tuple_13 * 2 == (19, 13, 8, 11, 19, 13, 8, 11)
    assert tuple_13 + (12, 52) == (19, 13, 8, 11, 12, 52)
    assert tuple_13 >= (1, 8)
    assert tuple_13 > (1, 8)
    assert not tuple_13 < (1, 8)
    assert not tuple_13 <= (1, 8)
    assert tuple_13 != (1, 8)
    assert isinstance(tuple_13, Hashable)
    assert tuple_13.count(13) == 1
    assert tuple_13.index(13) == 1

    set_13 = {13, 19, 11, 25, 36, 11}

    assert set_13 > set()
    assert set_13 >= set()
    assert not set_13 < set()
    assert not set_13 <= set()
    assert set_13 == {13, 19, 11, 25, 36, 11}
    assert set_13 != {1}
    assert 13 in set_13
    set_13 -= {13}
    assert set_13 == {19, 36, 25, 11}
    set_13 ^= {12, 8}
    assert set_13 == {19, 36, 8, 25, 11, 12}
    assert len(set_13) == 6
    set_13.remove(25)
    assert set_13 == {19, 36, 8, 11, 12}
    set_13.add(13)
    assert set_13 == {19, 36, 8, 11, 12, 13}
    assert set_13.symmetric_difference([258, 356, 11, 35]) == {
        258,
        35,
        356,
        36,
        8,
        12,
        13,
        19,
    }
    assert set_13.copy() == {19, 36, 8, 11, 12, 13}
    set_13.symmetric_difference_update([12, 13, 19, 356])
    assert set_13 == {
        36,
        356,
        8,
        11,
    }
    assert set_13.difference([11]) == {356, 8, 36}
    set_13.difference_update([13])
    assert set_13 == {36, 356, 8, 11}
    set_13.discard(11)
    assert set_13 == {36, 356, 8}
    assert set_13.intersection([36, 8]) == {8, 36}
    set_13.intersection_update([36, 11, 8])
    assert set_13 == {8, 36}
    assert set_13.isdisjoint([26])
    assert set_13.isdisjoint([26])
    assert set_13.issubset([36, 13, 8])
    assert not set_13.issuperset([8, 36])
    assert set_13.pop() == 8
    assert set_13.union([1, 2, 3, 4, 5]) == {1, 2, 3, 36, 4, 5}
    set_13.update([45, 25])
    assert set_13 == {25, 36, 45}
    set_13.clear()
    assert not set_13
    assert {12, 25} & {35, 25} == {25}
    assert not isinstance(set_13, Hashable)
    set_13 = {12, 25}
    set_13 &= {13}
    assert set_13 == {13}
    set_13 = {12, 25}
    set_13 &= {13}
    assert set_13 == {12, 25, 13}
    assert {12, 25, 13} | {19} == {25, 19, 12, 13}
    assert {12, 25, 13} - {13} == {25, 12}
    assert {12, 25, 13} ^ {19} == {25, 19, 12, 13}

    dict_13 = {"a": 13, "b": 19}

    assert dict_13["a"] == 13
    dict_13["c"] = 11
    assert dict_13 == {"a": 13, "b": 19, "c": 11}
    assert "a" in dict_13
    del dict_13["b"]
    assert dict_13 == {"a": 13, "c": 11}
    assert len(dict_13) == 2
    assert dict_13 != {}
    assert dict_13 | {"d": 12} == {"a": 13, "c": 11, "d": 12}
    assert dict_13.copy() == {"a": 13, "c": 11}
    assert dict_13.fromkeys(["one", "two", "3"], 10) == {
        "one": 10,
        "two": 10,
        "3": 10,
    }
    assert dict_13.get("a") == 13
    assert dict_13.items() == "dict_items([('a', 13), ('c', 11)])"
    assert dict_13.keys() == "dict_keys(['a', 'c'])"
    assert dict_13.pop("a") == 13
    assert dict_13.popitem() == ("c", 11)
    dict_13.setdefault("i", 3)
    assert dict_13 == {"i", 3}
    dict_13.update({"i": 9})
    assert dict_13 == {"i": 9}
    assert str(dict_13.values()) == "dict_values([9])"
    assert not isinstance(dict_13, Hashable)
    dict_13.clear()
    assert not dict_13
    dict_13 = {1: 'python', 2: 'c++'}
    dict_13 |= {3: 'c'}
    assert dict_13 == {1: 'python', 2: 'c++', 3: 'c'}
