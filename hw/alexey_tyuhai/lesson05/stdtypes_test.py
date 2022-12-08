from typing import Hashable


def test_list() -> None:

    my_list = [1, 2, 3]
    my_list_id = id(my_list)

    my_list.append(4)
    assert my_list[-1] == 4
    my_list.clear()
    assert my_list == []
    assert id(my_list.copy()) != my_list_id
    assert my_list.count(3) != 1
    my_list.extend([1, 2])
    assert my_list == [1, 2]
    my_list = [1, 2, 3]
    assert my_list.index(1) == 0
    my_list.insert(3, 4)
    assert my_list == [1, 2, 3, 4]
    my_list += [5]
    assert my_list == [1, 2, 3, 4, 5]
    assert my_list.pop() == 5
    my_list.append(5)
    my_list.remove(5)
    assert my_list == [1, 2, 3, 4]
    my_list.reverse()
    assert my_list == [4, 3, 2, 1]
    my_list.sort()
    assert my_list == [1, 2, 3, 4]
    assert my_list + [5, 6] == [5, 6]
    assert 5 in my_list
    del my_list[-1]
    assert 6 not in my_list
    assert my_list[2] == 3
    my_list *= 2
    assert my_list == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    assert len(my_list) != 1
    my_list = [1, 2, 3]
    assert my_list * 2 == [1, 2, 3, 1, 2, 3]
    assert not isinstance(my_list, Hashable)


def test_tuple() -> None:
    my_tuple = (1, 2, 3)

    assert my_tuple + (4, 5) == (1, 2, 3, 4, 5)
    assert 1 in my_tuple
    assert 6 not in my_tuple
    assert my_tuple[2] == 3
    assert len(my_tuple) == 3
    assert my_tuple * 2 == (1, 2, 3, 1, 2, 3)
    assert my_tuple.count(1) == 1
    assert my_tuple.index(3) == 2
    assert (1, 2) < my_tuple
    assert isinstance(my_tuple, Hashable)


def test_str() -> None:

    my_str = "flag"

    assert my_str + "S" == "flagS"
    assert "l" in my_str
    assert my_str[3] == "g"
    assert isinstance(my_str, Hashable)
    assert len(my_str) == 4
    assert "%s" % 1 == "1"
    assert my_str * 2 == "flagflag"
    assert my_str.capitalize() == "Flag"
    assert my_str.casefold() == "flag"
    assert my_str.center(8) == "  flag  "
    assert my_str.count("a") == 1
    assert my_str.encode() == b"flag"
    assert my_str.endswith("g")
    assert "\tflag".expandtabs(tabsize=3) == "   flag"
    assert my_str.find("t") == -1
    assert "rise {}".format(my_str) == "rise flag"
    my_dict = {"name": "Charlie"}
    assert "{name} Shin".format_map(my_dict) == "Charlie Shin"
    assert my_str.index("a") == 2
    assert "12ab".isalnum()
    assert my_str.isalpha()
    assert my_str.isascii()
    assert not my_str.isdigit()
    assert not my_str.isdecimal()
    assert my_str.isidentifier()
    assert my_str.islower()
    assert not my_str.isnumeric()
    assert my_str.isprintable()
    assert not my_str.isspace()
    assert not my_str.istitle()
    assert not my_str.isupper()
    assert my_str.join(["@", "@"]) == "@flag@"
    assert my_str.ljust(7) == "flag   "
    assert "FLAG".lower() == my_str
    assert " flag".lstrip() == my_str
    trance_table = str.maketrans({"s": "f", "l": "l", "u": "a"})
    assert trance_table == {115: "f", 108: "l", 117: "a"}
    assert "@flag".partition("@") == ("", "@", my_str)
    assert "fallflag".removeprefix("fall") == my_str
    assert "flagshtok".removesuffix("shtok") == my_str
    assert "flag!".replace("!", "") == my_str
    assert my_str.rfind("g") == 3
    assert my_str.rindex("g") == 3
    assert my_str.rjust(7, "@") == "@@@flag"
    assert my_str.rpartition("@") == ("", "", my_str)
    n_str = "q w e"
    assert isinstance(n_str.split(), list)
    assert "flag ".rstrip() == my_str
    assert "q w e".rsplit() == ["q", "w", "e"]
    assert "flag\nflag".splitlines() == [my_str, my_str]
    assert my_str.startswith("fl")
    assert " flag  ".strip() == my_str
    assert "FlAg".swapcase() == "fLaG"
    assert "raise flag".title() == "Raise Flag"
    assert "slug".translate(trance_table) == my_str
    assert my_str.upper() == "FLAG"
    assert my_str.zfill(8) == "0000flag"
    assert my_str < "w"


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
