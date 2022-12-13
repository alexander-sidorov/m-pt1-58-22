from typing import Hashable


def test_stdtypes() -> None:
    my_list = [1, 2, 3]
    my_list_id = id(my_list)
    my_list *= 2
    assert my_list == [1, 2, 3, 1, 2, 3]
    assert 3 in my_list
    assert id(my_list) == my_list_id
    assert len(my_list) != 0
    my_list.append(4)
    assert my_list[-1] == 4
    my_list.extend([5, 6])
    assert my_list == [1, 2, 3, 1, 2, 3, 4, 5, 6]
    my_list.clear()
    assert my_list == []
    my_list += [1, 2, 3]
    assert my_list == [1, 2, 3]
    my_list.reverse()
    assert my_list == [3, 2, 1]
    assert my_list[0] != 2
    assert my_list.count(1) != 2
    my_list += [0]
    assert my_list == [3, 2, 1, 0]
    my_list.remove(0)
    assert my_list == [3, 2, 1]
    my_list[0] = 4
    assert my_list == [4, 2, 1]
    assert my_list.index(2) == 1
    my_list.insert(1, 3)
    assert my_list == [4, 3, 2, 1]
    my_list.sort()
    assert my_list == [1, 2, 3, 4]
    my_list_copy = my_list.copy()
    assert id(my_list_copy) != my_list_id
    del my_list[0]
    assert my_list == [2, 3, 4]

    my_dict = {1: 11, 2: 22}
    my_dict.clear()
    assert not my_dict
    assert my_dict == {}
    my_dict_copy = my_dict.copy()
    assert my_dict_copy == {}
    my_dict = {1: 11, 2: 22}
    assert my_dict.fromkeys([1, 2]) == {1: None, 2: None}
    assert my_dict.get(1) == 11
    assert str(my_dict.items()) == "dict_items([(1, 11), (2, 22)])"
    assert str(my_dict.keys()) == "dict_keys([1, 2])"
    assert my_dict.pop(1) == 11
    assert my_dict.setdefault(1, 111) == 111
    my_dict.update({2: 222})
    assert my_dict == {1: 111, 2: 222}
    assert str(my_dict.values()) == "dict_values([222, 111])"
    assert my_dict[1] == 111
    my_dict[0] = 1
    assert my_dict == {0: 1, 1: 111, 2: 222}
    assert len(my_dict) == 3
    del my_dict[0]
    assert my_dict == {1: 111, 2: 222}
    assert 1 in my_dict
    assert not isinstance(my_dict, Hashable)

    kort = (1, 2, "abc")
    assert kort + (3,) == (1, 2, "abc", 3)
    assert kort[1] == 2
    assert 1 in kort
    assert len(kort) == 3
    assert () >= ()
    assert kort > ()
    assert () < (1,)
    assert kort != ()
    assert kort * 2 == (1, 2, "abc", 1, 2, "abc")
    assert kort.count(2) == 1
    assert isinstance(kort, Hashable)

    st = {1, 2}
    assert {1, 2, 3}.issuperset(st)
    assert st & {2, 3} == {2}
    assert 1 in st
    st.add(3)
    assert st == {1, 2, 3}
    stc = st.copy()
    assert stc == st
    assert st.difference({3, 4, 5}) == {1, 2}
    st.difference_update({3, 4, 5})
    assert st == {1, 2}
    st.clear()
    assert not st
    st = {1, 2}
    st.discard(2)
    assert st == {1}
    assert st.intersection({1, 2, 3}) == {1}
    assert st.isdisjoint({2, 3})
    assert {1}.issubset(st)
    pse = st.pop()
    assert pse == 1
    st = {1, 2, 3}
    st.remove(2)
    assert st == {1, 3}
    assert st > set()
    assert st != set()
    assert st.symmetric_difference({1, 2, 3}) == {2}
    st.symmetric_difference_update({1, 2, 3})
    assert st == {2}
    assert st.union({3, 4}) == {2, 3, 4}
    st.update({1, 2, 3})
    assert st == {1, 2, 3}
    assert not isinstance(st, Hashable)

    assert "abc" + "def" == "abcdef"
    assert "n" not in "abc"
    assert "a" in "abc"
    assert "abc"[1] == "b"
    assert "abc" != "adc"
    assert not len("")
    assert "abc" < "def"
    assert "ma" * 2 == "mama"
    assert "abc".capitalize() == "Abc"
    assert "AbC".casefold() == "abc"
    assert "abc".center(5, "!") == "!abc!"
    assert "abc cab".count("a") == 2
    assert "abc".encode() == b"abc"
    assert "abc".endswith("c")
    assert "abc\tdef".expandtabs(2) == "abc def"
    assert "abc".find("bc") == 1
    assert "abc".index("c") == 2
    assert "abc".isalnum()
    assert not "abc1".isalpha()
    assert "abc".isascii()
    assert not "abc".isdecimal()
    assert not "abc".isdigit()
    assert not "&".isidentifier()
    assert "abc".islower()
    assert not "abc".isnumeric()
    assert "abc".isprintable()
    assert " ".isspace()
    assert "Abc".istitle()
    assert "ABC".isupper()
    assert "-".join(["A", "B"]) == "A-B"
    assert "abc".ljust(5, "*") == "abc**"
    assert "abc".rjust(5, "*") == "**abc"
    assert "AbC".lower() == "abc"
    assert ",- abc".lstrip(", -") == "abc"
    assert "abc".partition("b") == ("a", "b", "c")
    assert "abcdef".removeprefix("abc") == "def"
    assert "abcdef".removesuffix("def") == "abc"
    assert "a.b.c".replace(".", "") == "abc"
    assert "abcdefg".rfind("def") == 3
    assert "abcdefg".rindex("efg") == 4
    assert "abcd".rpartition("b") == ("a", "b", "cd")
    assert "abc\nabc".splitlines() == ["abc", "abc"]
    assert "abc".startswith("a")
    assert ",.abc,.abc".strip(",.") == "abc,.abc"
    assert "AbC".swapcase() == "aBc"
    assert "abc".title() == "Abc"
    assert "abc".translate({97: "b"}) == "bbc"
    assert "abc".upper() == "ABC"
    assert "abc".zfill(5) == "00abc"
    assert str.maketrans({"a": "b"}) == {97: "b"}
    text = "a b"
    assert text.split() == ["a", "b"]
