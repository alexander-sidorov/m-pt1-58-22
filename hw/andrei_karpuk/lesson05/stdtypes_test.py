from typing import Hashable


def test_str() -> None:
    assert "pytho".ljust(6, "n") == "python"
    assert "plugnplay".partition("n") == ("plug", "n", "play")
    assert " ".isspace()
    assert "noise" in "white noise"
    assert "langpython".removeprefix("lang") == "python"
    assert "qwqwqw".replace("q", "k", 2) == "kwkwqw"
    assert "_".join("qwerty") == "q_w_e_r_t_y"
    assert "item"[1] == "t"
    assert "item".index("t") == 1
    assert "PYTHON".lower() == "python"
    assert "PYTHON".isupper()
    assert "creature,,,".removesuffix(",,,") == "creature"
    assert "python".islower()
    assert "csharp".translate({99: 110}) == "nsharp"
    assert " python ".strip() == "python"
    assert "error inside".find("inside") == 6
    assert "sssd".isidentifier()
    assert "12".isdigit()
    assert "ErRoR".swapcase() == "eRrOr"
    assert "qwe".center(7) == "  qwe  "
    assert "read only for".rsplit(" ", 1) == ["read only", "for"]
    assert "\u0033".isdecimal()
    assert "2233".isnumeric()
    assert "python".endswith("n")
    assert "ython".rjust(7, "p") == "ppython"
    assert "pyt{0}on".format("h") == "python"
    assert "text".isprintable()
    assert "title".title() == "Title"
    assert "text".isascii()
    assert "hohohohoho".rfind("h") == 8
    assert "hohohohoho".count("h") == 5
    assert "ErRoR".casefold() == "error"
    assert "NO\tRD".expandtabs(2) == "NO  RD"
    assert "11".zfill(4) == "0011"
    assert "Python".istitle()
    assert len("three") == 5
    assert "district13".isalnum()
    assert "python".maketrans("p", "c") == {112: 99}
    assert "out to in".rpartition("to") == ("out ", "to", " in")
    assert "{x}{y}".format_map({"x": "4", "y": "5"}) == "45"
    assert "pyt" + "hon" == "python"
    assert "python   ".rstrip() == "python"
    assert "pine#apple".split("#") == ["pine", "apple"]  # noqa: SIM905
    assert "Français".encode() == b"Fran\xc3\xa7ais"
    assert "python".startswith("p")
    assert "    python  ".lstrip() == "python  "
    assert isinstance("python", Hashable)
    assert "python".capitalize() == "Python"
    assert "%sq%s" % ("s", "l") == "sql"  # noqa: S001,MOD001
    assert "notnum".isalpha()
    assert "Three" * 3 == "ThreeThreeThree"
    assert "python".upper() == "PYTHON"
    assert "sci\nand\nfi".splitlines() == ["sci", "and", "fi"]
    assert "AAA" < "B"
    assert "abcabcabc".rindex("abc") == 6


def test_list() -> None:
    testing_list = [4, 2, 3]
    assert len(testing_list) == 3
    assert not isinstance(testing_list, Hashable)
    assert testing_list.copy() == [4, 2, 3]
    testing_list[1] = 5
    assert testing_list == [4, 5, 3]
    testing_list[2] = testing_list[2] * 3
    assert testing_list == [4, 5, 9]
    assert testing_list[0] + 3 == 7
    testing_list[0] = testing_list[0] + 3
    assert testing_list == [7, 5, 9]
    assert testing_list[0] * 2 == 14
    testing_list.extend([4, 2])
    assert testing_list == [7, 5, 9, 4, 2]
    testing_list.pop(1)
    assert testing_list == [7, 9, 4, 2]
    assert testing_list.index(9) == 1
    testing_list.reverse()
    assert testing_list == [2, 4, 9, 7]
    assert 2 in testing_list
    del testing_list[0]
    assert testing_list == [4, 9, 7]
    testing_list.sort()
    assert testing_list == [4, 7, 9]
    assert testing_list[1] == 7
    assert testing_list.count(4) == 1
    testing_list.remove(4)
    assert testing_list == [7, 9]
    testing_list.append(3)
    assert testing_list == [7, 9, 3]
    testing_list.insert(1, 8)
    assert testing_list == [7, 8, 9, 3]
    testing_list.clear()
    assert testing_list == []
    assert testing_list < [4, 6]
    assert ["a"] + ["b"] == ["a", "b"]
    list2 = ["a"]
    list2 += ["b"]
    assert list2 == ["a", "b"]
    list2 = ["a"]
    list2 *= 2
    assert list2 == ["a", "a"]



def test_dict() -> None:
    testing_dict = {1: "one", 2: "two"}
    assert testing_dict.items() == {(1, "one"), (2, "two")}
    testing_dict.update({3: "three"})
    assert testing_dict == {1: "one", 2: "two", 3: "three"}
    testing_dict = testing_dict | {3: "3"}
    assert testing_dict == {1: "one", 2: "two", 3: "3"}
    assert str(testing_dict.values()) == "dict_values(['one', 'two', '3'])"
    assert len(testing_dict) == 3
    testing_dict.pop(1)
    assert testing_dict == {2: "two", 3: "3"}
    testing_dict |= {4: "4"}
    assert testing_dict == {2: "two", 3: "3", 4: "4"}
    testing_dict.popitem()
    assert testing_dict == {2: "two", 3: "3"}
    assert testing_dict != {}
    assert 3 in testing_dict
    assert testing_dict.copy() == {2: "two", 3: "3"}
    assert testing_dict.get(2) == "two"
    testing_dict.setdefault(4, "4")
    assert testing_dict == {2: "two", 3: "3", 4: "4"}
    assert dict.fromkeys([1, 2, 3]) == {1: None, 2: None, 3: None}
    assert testing_dict[3] == "3"
    assert not isinstance(testing_dict, Hashable)
    assert str(testing_dict.keys()) == "dict_keys([2, 3, 4])"
    testing_dict[3] = "tri"
    assert testing_dict == {2: "two", 3: "tri", 4: "4"}
    del testing_dict[4]
    testing_dict.clear()
    assert testing_dict == {}


def test_set() -> None:
    t_set = {1, 2}
    t_set |= {3}
    assert t_set == {1, 2, 3}
    t_set.remove(1)
    assert t_set == {2, 3}
    temp_set = {3, 8, 4}
    t_set = t_set.symmetric_difference(temp_set)
    assert t_set == {8, 2, 4}
    t_set.difference_update({4, 7})
    assert t_set == {2, 8}
    assert 2 in t_set
    t_set.symmetric_difference_update({5, 4, 2})
    assert t_set == {4, 5, 8}
    assert not isinstance(t_set, Hashable)
    t_set = t_set & {4, 5, 1}
    assert t_set == {4, 5}
    t_set = t_set | {1, 4}
    assert t_set == {1, 4, 5}
    t_set = t_set.difference({1, 8})
    assert t_set == {4, 5}
    t_set = t_set ^ {5, 6, 7}
    assert t_set == {4, 6, 7}
    t_set ^= {7, 8}
    assert t_set == {4, 6, 8}
    assert t_set.isdisjoint({1, 2})
    t_set.discard(8)
    assert t_set == {4, 6}
    t_set &= {4, 7}
    assert t_set == {4}
    temp_set = t_set.copy()
    assert temp_set == t_set
    t_set.update({7, 8, 9})
    assert t_set == {8, 9, 4, 7}
    assert t_set.issuperset({4, 7})
    t_set = t_set.intersection({4, 6, 8})
    assert t_set == {8, 4}
    t_set = t_set.union({5, 9})
    assert t_set == {8, 9, 4, 5}
    t_set.intersection_update({4, 5, 9})
    assert t_set == {9, 4, 5}
    t_set -= {9}
    assert t_set == {4, 5}
    t_set.add(1)
    assert t_set == {1, 4, 5}
    assert len(t_set) == 3
    t_set = t_set - {
        4,
    }
    assert t_set == {1, 5}
    t_set.pop()
    assert t_set == {
        5,
    }
    assert set() < t_set
    assert set() <= t_set
    assert t_set > set()
    assert t_set >= set()
    assert t_set.issubset({4, 5, 6})
    t_set.clear()
    assert not t_set


def test_tuple() -> None:
    t_tuple = (1, 2)
    new_tuple = t_tuple + (3,)
    assert new_tuple == (1, 2, 3)
    assert new_tuple[1] == 2
    m_tuple = new_tuple * 2
    assert m_tuple == (1, 2, 3, 1, 2, 3)
    assert isinstance(m_tuple, Hashable)
    assert 3 in m_tuple
    assert len(m_tuple) == 6
    assert m_tuple.index(3) == 2
    assert m_tuple.count(3) == 2
    assert (1,) < m_tuple
    assert m_tuple >= (1,)
