from typing import Hashable


def test_list() -> None:

    my_list = [1, 2, 3]
    my_list_id = id(my_list)

    assert 3 in my_list
    my_list *= 2
    assert my_list == [1, 2, 3, 1, 2, 3]
    assert id(my_list) == my_list_id
    assert len(my_list) != 1
    my_list.clear()
    assert my_list == []
    assert id(my_list) == my_list_id
    assert my_list + [5, 4, 6, 7] == [5, 4, 6, 7]
    assert my_list.count(5) != 1
    my_list = [1, 2, 3]
    assert my_list[0] != 5
    my_list.append(6)
    assert my_list[-1] == 6
    my_list.extend([1, 2])
    assert my_list == [1, 2, 3, 6, 1, 2]
    my_list.reverse()
    assert my_list == [2, 1, 6, 3, 2, 1]
    my_list = [1, 2, 3]
    my_list += [5]
    assert my_list == [1, 2, 3, 5]
    assert my_list.pop() == 5
    my_list = [2, 1, 6, 3, 2, 1]
    my_list.remove(6)
    assert my_list == [2, 1, 3, 2, 1]
    my_list[0] = 7
    assert my_list == [7, 1, 3, 2, 1]
    my_list.extend([1, 2])
    assert my_list == [7, 1, 3, 2, 1, 1, 2]
    assert my_list.index(7) == 0
    my_list.insert(0, 5)
    assert my_list == [5, 7, 1, 3, 2, 1, 1, 2]
    assert not isinstance(my_list, Hashable)
    my_list = [3, 2, 1]
    my_list.sort()
    assert my_list == [1, 2, 3]
    assert id(my_list.copy()) != my_list_id
    assert my_list * 2 == [1, 2, 3, 1, 2, 3]
    assert not my_list < []
    my_list = [3, 2, 1]
    del my_list[0]
    assert 3 not in my_list


def test_tuple() -> None:

    my_tuple = (1, 2, 3)

    assert my_tuple.count(1) == 1
    assert my_tuple + (4, 5) == (1, 2, 3, 4, 5)
    assert my_tuple.index(1) == 0
    assert len(my_tuple) == 3
    assert my_tuple[0] == 1
    assert 1 in my_tuple
    assert isinstance(my_tuple, Hashable)
    assert my_tuple * 2 == (1, 2, 3, 1, 2, 3)
    assert (1, 2) < my_tuple


def test_str() -> None:

    my_str = "fake"

    assert my_str + "A" == "fakeA"
    assert "f" in my_str
    assert my_str[1] == "a"
    assert isinstance(my_str, Hashable)
    assert len(my_str) == 4
    assert "%s" % 1 == "1"  # noqa: S001,MOD001
    assert my_str * 2 == "fakefake"
    assert my_str.capitalize() == "Fake"
    assert my_str.casefold() == "fake"
    assert my_str.center(6) == " fake "
    assert my_str.count("f") == 1
    assert my_str.encode() == b"fake"
    assert my_str.endswith("e")
    assert "\tfake".expandtabs(tabsize=2) == "  fake"
    assert my_str.find("g") == -1
    assert "all {}".format(my_str) == "all fake"
    my_dict = {"name": "Brad"}
    assert "{name} Pitt".format_map(my_dict) == "Brad Pitt"
    assert my_str.index("f") == 0
    assert "12ab".isalnum()
    assert my_str.isalpha()
    assert my_str.isascii()
    assert not my_str.isdecimal()
    assert not my_str.isdigit()
    assert my_str.isidentifier()
    assert my_str.islower()
    assert not my_str.isnumeric()
    assert my_str.isprintable()
    assert not my_str.isspace()
    assert not my_str.istitle()
    assert not my_str.isupper()
    assert my_str.join(["*", "*"]) == "*fake*"
    assert my_str.ljust(6) == "fake  "
    assert "FAKE".lower() == my_str
    assert " fake".lstrip() == my_str
    trance_table = str.maketrans({"t": "f", "r": "a", "u": "k"})
    assert trance_table == {116: "f", 114: "a", 117: "k"}
    assert "*fake".partition("*") == ("", "*", my_str)
    assert "notfake".removeprefix("not") == my_str
    assert "fakehot".removesuffix("hot") == my_str
    assert "fake!".replace("!", "") == my_str
    assert my_str.rfind("e") == 3
    assert my_str.rindex("e") == 3
    assert my_str.rjust(6, "*") == "**fake"
    assert my_str.rpartition("*") == ("", "", my_str)
    new_str = "a b c"
    assert isinstance(new_str.split(), list)
    assert "fake  ".rstrip() == my_str
    assert "a b c".rsplit() == ["a", "b", "c"]
    assert "fake\nfake".splitlines() == [my_str, my_str]
    assert my_str.startswith("fa")
    assert " fake ".strip() == my_str
    assert "FaKe".swapcase() == "fAkE"
    assert "fake news".title() == "Fake News"
    assert "true".translate(trance_table) == my_str
    assert my_str.upper() == "FAKE"
    assert my_str.zfill(6) == "00fake"
    assert my_str < "z"


def test_set() -> None:

    my_set1 = {1, 2, 3}
    my_set2 = {3, 4, 5}

    assert not (my_set1 < my_set2)
    assert my_set1 & my_set2 == {3}
    assert 1 in my_set1
    assert not isinstance(my_set1, Hashable)
    my_set1 &= my_set2
    assert my_set1 == {3}
    my_set1 = {1, 2, 3}
    my_set1 |= my_set2
    assert my_set1 == {1, 2, 3, 4, 5}
    my_set1 -= my_set2
    assert my_set1 == {1, 2}
    my_set1 = {1, 2, 3}
    my_set1 ^= my_set2
    assert my_set1 == {1, 2, 4, 5}
    assert len(my_set1) == 4
    assert my_set1 | my_set2 == {1, 2, 3, 4, 5}
    assert my_set1 - my_set2 == {1, 2}
    assert my_set1 ^ my_set2 == {1, 2, 3}
    my_set1.add(3)
    assert 3 in my_set1
    my_set1.clear()
    assert my_set1 == set()
    my_set2_id = id(my_set2)
    assert id(my_set2.copy()) != my_set2_id
    my_set1 = {1, 2, 3}
    my_set2 = {3, 4, 5}
    assert my_set1.difference(my_set2) == {1, 2}
    assert my_set1.intersection(my_set2) == {3}
    assert my_set1.symmetric_difference(my_set2) == {1, 2, 4, 5}
    my_set1.difference_update(my_set2)
    assert len(my_set1) == 2
    my_set1 = {1, 2, 3}
    my_set1.intersection_update(my_set2)
    assert my_set1 == {3}
    my_set1 = {1, 2, 3}
    my_set1.symmetric_difference_update(my_set2)
    assert my_set1 == {1, 2, 4, 5}
    my_set1.discard(5)
    assert 5 not in my_set1
    assert my_set1.isdisjoint({10, 11})
    assert {1, 2}.issubset(my_set1)
    assert my_set1.issuperset({1, 2})
    assert my_set1.union(my_set2) == {1, 2, 3, 4, 5}
    my_set1.update(my_set2)
    assert my_set1 == {1, 2, 3, 4, 5}
    my_set1.remove(1)
    assert 1 not in my_set1
    num = my_set1.pop()
    assert num not in my_set1


def test_dict() -> None:

    my_dict1 = {1: 1, 2: 2, 3: 3}
    my_dict2 = {4: 4, 5: 5, 6: 6}

    assert len(my_dict1.keys()) == 3
    assert 1 in my_dict1
    del my_dict1[1]
    assert 1 not in my_dict1
    assert my_dict1[2] == 2
    assert not isinstance(my_dict1, Hashable)
    my_dict1 |= my_dict2
    assert 6 in my_dict1
    assert len(my_dict1) == 5
    my_dict2[7] = 7
    assert len(my_dict1 | my_dict2) == 6
    assert 7 in my_dict2
    my_dict1.clear()
    assert my_dict1 == {}
    my_dict1 = {1: 1, 2: 2, 3: 3}
    my_dict1_id = id(my_dict1)
    copy_dict = my_dict1.copy()
    assert id(copy_dict) != my_dict1_id
    my_dict3 = dict.fromkeys([7, 8, 9])
    assert my_dict3[7] is None
    assert my_dict3.get(7) is None
    assert (7, None) in my_dict3.items()
    assert 7 in my_dict3
    assert my_dict3.pop(7) is None
    assert my_dict3.popitem()[1] is None
    assert my_dict3.setdefault(10) is None
    assert my_dict1.update({1: 6}) is None
    assert my_dict3[10] in my_dict3.values()
