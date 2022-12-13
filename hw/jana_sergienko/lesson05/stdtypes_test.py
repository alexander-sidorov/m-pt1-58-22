from typing import Hashable


def test_str() -> None:
    assert "jana".capitalize() == "Jana"
    assert "JaNA".casefold() == "jana"
    assert "jana".center(8, "*") == "**jana**"
    assert "jana".count("a") == 2
    assert "jana".encode() == b"jana"
    assert "jana".endswith("a")
    assert "\tjana".expandtabs(tabsize=5) == "     jana"
    assert "jana_monkey".find("mo") == 5
    assert "{}{}".format("ja", "na") == "jana"
    assert "{j}{n}".format_map({"j": "ja", "n": "na"}) == "jana"
    assert "jana".index("j") == 0
    assert "jana".isalnum()
    assert "jana95".isalpha()
    assert "jana".isascii()
    assert not "jana".isdecimal()
    assert not "jana".isdigit()
    assert "jana".isidentifier()
    assert "jana".islower()
    assert not "jana".isnumeric()
    assert "jana".isprintable()
    assert not "jana".isspace()
    assert "Jana".istitle()
    assert "JANA".isupper()
    assert "*".join(["j", "a", "n", "a"]) == "j*a*n*a"
    assert "jana".ljust(8, "*") == "jana****"
    assert "JANA".lower() == "jana"
    assert " jana".lstrip() == "jana"
    assert "jana".partition("n") == ("ja", "n", "a")
    assert "sergjana".removeprefix("serg") == "jana"
    assert "janaserg".removesuffix("serg") == "jana"
    assert "j*a*n*a".replace("*", " ") == "j a n a"
    assert "janjanjan".rfind("jan") == 6
    assert "janjanjan".rindex("jan") == 6
    assert "jana".rjust(8, "*") == "****jana"
    assert "janna".rpartition("n") == ("jan", "n", "a")
    assert "jan".rsplit("a") == ["j", "n"]
    assert "jana.!".rstrip(".!") == "jana"
    assert "jana".split(" ") == ["jana"]
    assert "jana\njana\njana".splitlines() == ["jana", "jana", "jana"]
    assert "jana".startswith("j")
    assert "    jana    ".strip() == "jana"
    assert "JaNa".swapcase() == "jAnA"
    assert "jana".title() == "Jana"
    assert "jan".translate({97: "b"}) == "jbn"
    assert "jana".upper() == "JANA"
    assert "jana".zfill(8) == "0000jana"
    assert str.maketrans({"a": "b"}) == {97: "b"}
    assert "ja" + "na" == "jana"
    assert "b" not in "jana"
    assert "jana"[0] == "j"
    assert isinstance("jana", Hashable)
    assert "jana" <= "jana"
    assert len("jana") == 4
    assert "abc" < "def"
    assert "%s %s" % (2, "milk") == "2 milk"
    assert "jana" * 2 == "janajana"


def test_list() -> None:
    assert [0] + [1] == [0, 1]
    assert 0 in [0, 1]
    lst = [0, 1]
    del lst[0]
    assert lst == [1]
    assert [0, 1][1] == 1
    lst = []
    lst += [1]
    assert lst == [1]
    assert lst * 3 == [1, 1, 1]
    assert [] >= []
    assert [1] > []
    assert [] <= []
    assert [0] < [1]
    assert not len([])
    assert [1] * 3 == [1, 1, 1]
    assert [] != [1]
    lst = [1, 1]
    lst[1] = 2
    assert lst[1] == 2
    lst.append(3)
    assert lst == [1, 2, 3]
    lst.clear()
    assert not lst.copy()
    assert [1, 2, 3].count(1) == 0
    lst.extend([1, 2, 3])
    assert lst == [1, 2, 3]
    assert lst.index(1) == 0
    lst.insert(1, 4)
    assert lst == [1, 4, 2, 3]
    assert lst.pop(1) == 4
    lst.remove(1)
    assert lst == [2, 3]
    lst.extend([2, 3])
    assert lst == [2, 3, 2, 3]
    lst.reverse()
    assert lst == [3, 2, 3, 2]
    lst.sort()
    assert lst == [2, 2, 3, 3]
    assert not isinstance(lst, Hashable)


def test_tuple() -> None:
    assert (0, ) + (1, ) == (0, 1)
    tpl = (0, 1)
    assert 0 in tpl
    assert () >= ()
    assert (1, ) > ()
    assert () <= ()
    assert () < (1, )
    assert tpl[1] == 1
    assert len(tpl) == 2
    assert tpl * 3 == (0, 1, 0, 1, 0, 1)
    assert () != (1, )
    assert tpl.count(2) == 0
    assert tpl.index(0) == 0
    assert isinstance(tpl, Hashable)


def test_set() -> None:
    st = {1, 2}
    assert {1, 2, 3}.issuperset(st)
    assert st & {1, 2} == {1, 2}
    assert 1 in st
    assert st > set()
    assert st >= set()
    assert set() < st
    assert set() <= st
    st &= {2, 3}
    assert st == {2}
    st |= {1, 3}
    assert st == {1, 2, 3}
    st -= {1}
    assert st == {2, 3}
    st ^= {1, 2}
    assert st == {1, 3}
    assert len(st) == 2
    assert st != {1}
    assert st | {2} == {1, 2, 3}
    assert st - {3} == {1}
    assert st ^ {2, 3, 4} == {1, 2, 4}
    st.add(2)
    assert st == {1, 2, 3}
    st.clear()
    assert not st
    assert not st.copy()
    st = {1, 2, 3}
    assert st.difference({3, 4, 5}) == {1, 2}
    st.difference_update({3, 4, 5})
    assert st == {1, 2}
    st.discard(2)
    assert st == {1}
    assert st.intersection({1, 2, 3}) == {1}
    st.add(2)
    st.add(3)
    st.intersection_update({2, 3})
    assert st == {2, 3}
    assert st.isdisjoint({1, 4})
    assert {2}.issubset(st)
    poppies = st.pop()
    assert poppies == 2 or poppies == 3
    st.remove(3)
    assert not st
    st = {1, 2, 3}
    assert st.symmetric_difference({2, 3, 4}) == {1, 4}
    st.symmetric_difference_update({2, 3, 4})
    assert st == {1, 4}
    assert st.union({2, 3}) == {1, 2, 3, 4}
    st.update({2, 3})
    assert st == {1, 2, 3, 4}
    assert not isinstance(st, Hashable)


def test_dictionary() -> None:
    dct = {1: 2, 3: 4}
    assert dct[3] == 4
    assert 1 in dct
    del dct[3]
    assert dct == {1: 2}
    dct |= {3: 4}
    assert dct == {1: 2, 3: 4}
    assert len(dct) == 2
    assert dct != {}
    assert dct | {5: 6} == {1: 2, 3: 4, 5: 6}
    dct[0] = 1
    assert dct == {0: 1, 1: 2, 3: 4}
    dct.clear()
    assert not dct
    assert not dct.copy()
    assert not dct.get(3)
    dct = {1: 2, 2: 3}
    assert str(dct.items()) == "dict_items([(1, 2), (2, 3)])"
    assert dct.keys() == {1, 2}
    assert dct.pop(2) == 3
    assert dct.popitem() == (1, 2)
    dct.setdefault(1, 5)
    assert dct == {1: 5}
    dct.update({2: 3})
    assert dct == {1: 5, 2: 3}
    assert str(dct.values()) == "dict_values([5, 3])"
    assert dict.fromkeys([1, 2, 3]) == {1: None, 2: None, 3: None}
    assert not isinstance(dct, Hashable)
