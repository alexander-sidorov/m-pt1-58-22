from typing import Hashable


def test_list() -> None:
    list1 = [4, 5, 6]
    list1.append(7)
    assert list1[-1] == 7
    new_list = list1.copy()
    assert new_list == list1
    assert list1.count(7) == 1
    list1.clear()
    assert list1 == []
    assert list1 + [3, 33, 333] == [3, 33, 333]
    list1 = [3, 33, 333]
    list1.extend([7, 77, 777])
    assert list1 == [3, 33, 333, 7, 77, 777]
    assert list1.index(33) == 1
    list1.insert(3, 3333)
    assert list1 == [3, 33, 333, 3333, 7, 77, 777]
    assert list1[3] != 333
    list1 = [1, 2]
    list1 += [3]
    assert list1 == [1, 2, 3]
    list1.reverse()
    assert list1 == [3, 2, 1]
    assert list1.pop() == 1
    list1 = [5, 4, 3, 1, 2]
    list1.sort()
    assert list1 == [1, 2, 3, 4, 5]
    list1.remove(3)
    assert list1 == [1, 2, 4, 5]
    assert len(list1) != 1
    list1 *= 3
    assert list1 == [1, 2, 4, 5, 1, 2, 4, 5, 1, 2, 4, 5]
    list1 = [1, 2, 3]
    list1 += [4]
    assert list1 == [1, 2, 3, 4]
    list1[3] = 7
    assert list1 == [1, 2, 3, 7]
    assert 7 in list1
    list_id = id(list1)
    assert id(list1) == list_id
    list1.insert(3, 5)
    assert list1 == [1, 2, 3, 5, 7]
    list1.clear()
    list1 = []
    assert id(list1) != list_id
    assert not isinstance(list1, Hashable)
    list_copy = list1.copy()
    list1 = [1, 2, 2, 3, 3, 3]
    assert list1 != list_copy
    assert id(list1.copy()) != list_id
    assert list1 > []
    assert list1 * 2 == [1, 2, 2, 3, 3, 3, 1, 2, 2, 3, 3, 3]
    list1 = [1, 2, 3]
    list1.extend([4, 5])
    assert list1 == [1, 2, 3, 4, 5]


def test_tuple() -> None:
    tuple1 = (1, "string", [1, 2])
    assert tuple1.index("string") == 1
    assert tuple1 + (2, 3) == (1, "string", [1, 2], 2, 3)
    assert tuple1.count(3) != 3
    assert len(tuple1) == 3
    assert tuple1[1] == "string"
    assert isinstance(tuple1, Hashable)
    assert tuple1 * 2 == (1, "string", [1, 2], 1, "string", [1, 2])
    assert 1 in tuple1


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
    string = "this_is_tin"
    assert string.islower()
    assert string.find("is") == 2
    assert string.split(" ") == ["this_is_tin"]
    assert ".".join(string) != "this_is_tin"
    assert "normal_this_is_tin".removeprefix("normal_") == string
    assert string.encode() == b"this_is_tin"
    assert not string.isspace()
    assert not string.istitle()
    assert not string.isupper()
    assert string.isprintable()
    assert "tHiS_Is_tIN".swapcase() == "ThIs_iS_Tin"
    assert string.endswith("n")
    assert "\tthis_is_tin".expandtabs(tabsize=3) == "   this_is_tin"
    assert (
        "{first}{second}".format_map({"first": "this_i", "second": "s_tin"})
        == "this_is_tin"
    )
    assert string.index("s") == 3
    assert " this_is_tin".lstrip() == string
    assert "this_is_tin     ".rstrip() == string
    assert string.isascii()
    assert not string.isnumeric()
    assert not string.isdecimal()
    assert "this _ is _ ting".rsplit(" ") == ["this", "_", "is", "_", "ting"]
    assert not string.isalpha()
    assert "324bhk2j3hfdf3".isalnum()
    assert not string.isdigit()
    assert string.isidentifier()
    assert string.ljust(6) != "this_is_tin  "
    assert "this_is_tin".title() == "This_Is_Tin"
    assert string.startswith("this_i")
    assert string.zfill(12) == "0this_is_tin"
    assert "this_is_tin\nthis_is_tin".splitlines() == [string, string]
    assert string.rjust(12, "*") == "*this_is_tin"
    assert string.rpartition("*") == ("", "", string)
    assert "*this_is_tin".partition("*") == ("", "*", string)
    assert "this_is_tin!@#$".removesuffix("!@#$") == string
    assert string.rfind("n") == 10
    assert string.rindex("is") == 5
    assert "NOT {}".format(string) == "NOT this_is_tin"
    assert "%s" % 231 == "231"  ## noqa: S001,MOD001
    string = "DICH"
    dich = string.maketrans({"t": "D", "h": "I", "i": "C", "s": "H"})
    assert dich == {116: "D", 104: "I", 105: "C", 115: "H"}
    assert string.translate(dich) == string


def test_dict() -> None:

    dict1 = {1: "e", 2: "n", 3: "o"}
    dict_1 = {4: "u", 5: "h", 6: "h"}

    assert "h" not in dict_1
    del dict_1[5]
    assert 5 not in dict_1
    assert dict_1[6] == "h"
    assert not isinstance(dict_1, Hashable)
    dict1.clear()
    assert dict1 == {}
    dict1 |= dict_1
    assert dict1 == {4: "u", 6: "h"}
    assert 1 not in dict1
    dict1 = {1: "e", 2: "n", 3: "o"}
    dict_1 = {4: "u", 5: "h", 6: "h"}
    dict_new = dict1.fromkeys([1, 3, 5])
    assert dict_new.pop(1, 3) is None
    assert dict_new.popitem()[1] is None
    assert dict_new.setdefault(10) is None
    assert dict_new.update(dict_new) is None
    dict1 = {1: "e", 2: "n", 3: "o"}
    dict_1 = {4: "u", 5: "h", 6: "h"}
    dict_new = dict1.fromkeys([1, 3, 5])
    assert not dict_new[3] in dict1.values()
    dict1[1] = "c"
    assert len(dict1 | dict_new) == 4
    assert 3 in dict_new
    dict1 = {1: 9, 2: 8, 3: 7}
    dict_id = id(dict1)
    dict_copy = dict1.copy()
    assert id(dict1) == dict_id
    assert dict_new[3] is None
    val_dict = dict1.get(2, 'Not in "dict1"')
    assert val_dict == 8
    assert (3, 7) in dict1.items()
    assert 1 in dict1
    assert len(dict1) == 3


def test_set() -> None:

    set1 = {1, 3, 5}
    set2 = {2, 4, 6}

    assert set1 != set2
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
    assert set1.intersection(set2) != {3}
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
