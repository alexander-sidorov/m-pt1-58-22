from typing import Hashable


def test_list() -> None:
    list = [4, 5, 6]
    list.append(7)
    assert list[-1] == 7
    new_list = list.copy()
    assert new_list == list
    assert list.count(7) == 1
    list.clear()
    assert list == []
    assert list + [3, 33, 333] == [3, 33, 333]
    list = [3, 33, 333]
    list.extend([7, 77, 777])
    assert list == [3, 33, 333, 7, 77, 777]
    assert list.index(33) == 1
    list.insert(3, 3333)
    assert list == [3, 33, 333, 3333, 7, 77, 777]
    assert list[3] != 333
    list = [1, 2]
    list += [3]
    assert list == [1, 2, 3]
    list.reverse()
    assert list == [3, 2, 1]
    assert list.pop() == 1
    list = [5, 4, 3, 1, 2]
    list.sort()
    assert list == [1, 2, 3, 4, 5]
    list.remove(3)
    assert list == [1, 2, 4, 5]
    assert len(list) != 1
    list *= 3
    assert list == [1, 2, 4, 5, 1, 2, 4, 5, 1, 2, 4, 5]
    list = [1, 2, 3]
    list += [4]
    assert list == [1, 2, 3, 4]
    list[3] = 7
    assert list == [1, 2, 3, 7]
    assert 7 in list
    list_id = id(list)
    assert id(list) == list_id
    list.insert(3, 5)
    assert list == [1, 2, 3, 5, 7]
    list.clear()
    list = []
    assert id(list) != list_id
    assert not isinstance(list, Hashable)
    list_copy = list.copy()
    list = [1, 2, 2, 3, 3, 3]
    assert list != list_copy
    assert id(list.copy()) != list_id
    assert list > []
    assert list * 2 == [1, 2, 2, 3, 3, 3, 1, 2, 2, 3, 3, 3]
    list = [1, 2, 3]
    list.extend([4, 5])
    assert list == [1, 2, 3, 4, 5]


def test_tuple() -> None:
    tuple = (1, "string", [1, 2])
    assert tuple.index("string") == 1
    assert tuple + (2, 3) == (1, "string", [1, 2], 2, 3)
    assert tuple.count(3) != 3
    assert len(tuple) == 3
    assert tuple[1] == "string"
    assert isinstance(tuple, Hashable)
    assert tuple * 2 == (1, "string", [1, 2], 1, "string", [1, 2])
    assert 1 in tuple


def test_str() -> None:
    string = "this_is_tin"
    assert "i" in string
    assert string[4] == "_"
    assert string * 2 == "this_is_tinthis_is_tin"
    assert len(string) == 11
    assert string.lower() == "this_is_tin"
    assert string.upper() == "THIS_IS_TIN"
    string = "#@!this_is_tin#@!"
    string.replace("#@!", "")
    string = "this_is_tin"
    assert string == "this_is_tin"
    assert string < "tin"
    assert isinstance(string, Hashable)
    assert string.count("i") == 3
    assert string.capitalize() == "This_is_tin"
    assert string + "Q" == "this_is_tinQ"
    assert string.casefold() == "this_is_tin"
    assert string.center(4) == "this_is_tin"
    string = "        this_is_tin                             "
    assert string.strip() == "this_is_tin"
    str = "this_is_tin"
    assert str.islower()
    assert str.find("is") == 2
    assert str.split(" ") == ["this_is_tin"]
    assert ".".join(str) != "this_is_tin"
    assert "normal_this_is_tin".removeprefix("normal_") == str
    assert str.encode() == b"this_is_tin"
    assert not str.isspace()
    assert not str.istitle()
    assert not str.isupper()
    assert str.isprintable()
    assert "tHiS_Is_tIN".swapcase() == "ThIs_iS_Tin"
    assert str.endswith("n")
    assert "\tthis_is_tin".expandtabs(tabsize=3) == "   this_is_tin"
    assert (
        "{first}{second}".format_map({"first": "this_i", "second": "s_tin"})
        == "this_is_tin"
    )
    assert str.index("s") == 3
    assert " this_is_tin".lstrip() == str
    assert "this_is_tin     ".rstrip() == str
    assert str.isascii()
    assert not str.isnumeric()
    assert not str.isdecimal()
    assert "this _ is _ ting".rsplit(" ") == ["this", "_", "is", "_", "ting"]
    assert not str.isalpha()
    assert "324bhk2j3hfdf3".isalnum()
    assert not str.isdigit()
    assert str.isidentifier()
    assert not str.ljust(6) == "this_is_tin  "
    assert "this_is_tin".title() == "This_Is_Tin"
    assert str.startswith("this_i")
    assert str.zfill(12) == "0this_is_tin"
    assert "this_is_tin\nthis_is_tin".splitlines() == [str, str]
    assert str.rjust(12, "*") == "*this_is_tin"
    assert str.rpartition("*") == ("", "", str)
    assert "*this_is_tin".partition("*") == ("", "*", str)
    assert "this_is_tin!@#$".removesuffix("!@#$") == str
    assert str.rfind("n") == 10
    assert str.rindex("is") == 5
    assert "NOT {}".format(str) == "NOT this_is_tin"
    assert "%s" % 231 == "231"
    str = "DICH"
    dich = str.maketrans({"t": "D", "h": "I", "i": "C", "s": "H"})
    assert dich == {116: "D", 104: "I", 105: "C", 115: "H"}
    assert str.translate(dich) == str


def test_dict() -> None:

    dict = {1: "e", 2: "n", 3: "o"}
    dict_1 = {4: "u", 5: "h", 6: "h"}

    assert "h" not in dict_1
    del dict_1[5]
    assert 5 not in dict_1
    assert dict_1[6] == "h"
    assert not isinstance(dict_1, Hashable)
    dict.clear()
    assert dict == {}
    dict |= dict_1
    assert dict == {4: "u", 6: "h"}
    assert 1 not in dict
    dict = {1: "e", 2: "n", 3: "o"}
    dict_1 = {4: "u", 5: "h", 6: "h"}
    dict_new = dict.fromkeys([1, 3, 5])
    assert dict_new.pop(1, 3) is None
    assert dict_new.popitem()[1] is None
    assert dict_new.setdefault(10) is None
    assert dict_new.update(dict_new) is None
    dict = {1: "e", 2: "n", 3: "o"}
    dict_1 = {4: "u", 5: "h", 6: "h"}
    dict_new = dict.fromkeys([1, 3, 5])
    assert not dict_new[3] in dict.values()
    dict[1] = "c"
    assert len(dict | dict_new) == 4
    assert 3 in dict_new
    dict = {1: 9, 2: 8, 3: 7}
    dict_id = id(dict)
    dict_copy = dict.copy()
    assert id(dict) == dict_id
    assert dict_new[3] is None
    val_dict = dict.get(2, 'Not in "dict"')
    assert val_dict == 8
    assert (3, 7) in dict.items()
    assert 1 in dict
    assert len(dict) == 3


def test_set() -> None:

    set1 = {1, 3, 5}
    set2 = {2, 4, 6}

    assert not set1 == set2
    assert set1 & set2 != {3}
    assert 3 in set1
    assert not isinstance(set1, Hashable)
    set1 &= set2
    assert set1 == set()
    set1 = {1, 3, 5}
    set1 |= set2
    assert set1 == {1, 2, 3, 4, 5, 6}
    set1 -= set2
    assert set1 == {1, 3, 5}
    set1 ^= set2
    assert set1 == {1, 3, 4, 5, 2, 6}
    assert len(set1) == 6
    assert set1 | set2 == {1, 2, 3, 4, 5, 6}
    assert set1 - set2 == {1, 3, 5}
    assert set1 ^ set2 == {1, 3, 5}
    set2.add(3)
    assert 3 in set2
    set1.clear()
    set2.clear()
    assert set2 == set()
    set1 = {1, 3, 5}
    set2 = {2, 4, 6}
    set1_id = id(set1)
    copy_set1 = set1.copy()
    assert id(copy_set1) != set1_id
    del copy_set1
    assert set1.difference(set2) == {1, 3, 5}
    assert not set1.intersection(set2) == {3}
    assert set1.symmetric_difference(set2) == {1, 2, 4, 5, 3, 6}
    set1.difference_update(set2)
    assert len(set1) == 3
    set1 = {1, 2, 3, 6}
    set1.intersection_update(set2)
    assert set1 == {2, 6}
    set1 = {1, 3, 5}
    set1.symmetric_difference_update(set2)
    assert set1 == {1, 2, 3, 4, 5, 6}
    set1.discard(3)
    assert set1 == {1, 2, 4, 5, 6}
    assert 3 not in set1
    assert set1.isdisjoint({7, 8})
    assert {2, 5}.issubset(set1)
    assert set1.issuperset({5, 2})
    assert set1.union(set2) == {1, 2, 4, 5, 6}
    set2.update(set1)
    assert set2 == set1
    set2.remove(6)
    assert 6 not in set2
    chislo = set1.pop()
    assert chislo not in set1
