from typing import Hashable

def test_stdtypes() -> None:
    assert "abc" + "def" == "abcdef"
    assert "v" not in "abc"
    assert "abc"[1] == "b"
    assert isinstance("abc", Hashable)
    assert "abc" <= "abc"
    assert not len("")
    assert "abc" < "def"
    assert "%s or %s" % ("two", 2) == "two or 2"  # noqa: S001,MOD001
    assert "abc" * 2 == "abcabc"
    assert "abc".capitalize() == "Abc"
    assert "AbC".casefold() == "abc"
    assert "abc".center(7, "&") == "&&abc&&"
    assert "abcabcabc".count("b") == 3
    assert "abc".encode() == b"abc"
    assert "abc".endswith("c")
    assert "abc\tdef".expandtabs(8) == "abc     def"
    assert "abcdef".find("cde") == 2
    assert "{}{}".format("ab", "c") == "abc"
    assert "{x}{y}".format_map({"x": "ab", "y": "c"}) == "abc"
    assert "abc".index("b") == 1
    assert "abc".isalnum()
    assert not "1abc".isalpha()
    assert "iuhgamgl".isascii()
    assert not "abc".isdecimal()
    assert not "abc".isdigit()
    assert not "%".isidentifier()
    assert "abc".islower()
    assert not "abc".isnumeric()
    assert "abc".isprintable()
    assert " ".isspace()
    assert "Abc".istitle()
    assert "ABC".isupper()
    assert "&".join(["a", "b", "c"]) == "a&b&c"
    assert "abc".ljust(10, "*") == "abc*******"
    assert "ABC".lower() == "abc"
    assert ",./! abc".lstrip(" .,!?/") == "abc"
    assert "abc".partition("b") == ("a", "b", "c")
    assert "preabc".removeprefix("pre") == "abc"
    assert "abcsuff".removesuffix("suff") == "abc"
    assert "a.b.c".replace(".", " ") == "a b c"
    assert "abcabcabc".rfind("abc") == 6
    assert "abcabcabc".rindex("abc") == 6
    assert "abc".rjust(10, "*") == "*******abc"
    assert "abbc".rpartition("b") == ("ab", "b", "c")
    assert "abc".split("b") == ["a", "c"]  # noqa: SIM905
    assert "abc".rsplit("b") == ["a", "c"]
    assert "abc,./".rstrip(",./") == "abc"
    assert "abc\nabc\nabc".splitlines() == ["abc", "abc", "abc"]
    assert "abc".startswith("a")
    assert ",./abc,./abc,./".strip(",./") == "abc,./abc"
    assert "AbC".swapcase() == "aBc"
    assert "abc".title() == "Abc"
    assert "abc".translate({97: "b"}) == "bbc"
    assert "abc".upper() == "ABC"
    assert "abc".zfill(5) == "00abc"
    assert str.maketrans({"a": "b"}) == {97: "b"}

    assert [1] + [2] == [1, 2]
    assert 1 in [1]
    lis = [1]
    del lis[0]
    assert lis == []
    assert [1, 2, 3][1] == 2
    lis += [1]
    assert lis == [1]
    lis *= 2
    assert lis == [1, 1]
    assert [] >= []
    assert [1] > []
    assert [] <= []
    assert [0] < [1]
    assert not len([])
    assert [1] * 2 == [1, 1]
    assert [] != [1]
    lis[1] = 2
    assert lis[1] == 2
    lis.append(3)
    assert lis == [1, 2, 3]
    lis.clear()
    assert not lis
    assert not lis.copy()
    assert [1, 2, 3].count(2) == 1
    lis.extend([1, 2])
    assert lis == [1, 2]
    assert lis.index(2) == 1
    lis.insert(1, 8)
    assert lis == [1, 8, 2]
    assert lis.pop(1) == 8
    lis.remove(1)
    assert lis == [2]
    lis.extend([2, 3])
    lis.reverse()
    assert lis == [3, 2, 2]
    lis.sort()
    assert lis == [2, 2, 3]
    assert not isinstance(lis, Hashable)

    assert (1,) + (2,) == (1, 2)
    tup = (1, 2)
    assert 1 in tup
    assert () >= ()
    assert (1,) > ()
    assert () <= ()
    assert () < (1,)
    assert tup[1] == 2
    assert isinstance(tup, Hashable)
    assert len(tup) == 2
    assert tup * 2 == (1, 2, 1, 2)
    assert () != (1,)
    assert tup.count(2) == 1
    assert not tup.index(1)

    se = {1, 2}
    assert se & {2, 3} == {2}
    assert 1 in se
    assert se > set()
    assert se >= set()
    assert set() < se
    assert set() <= se
    se &= {2, 3}
    assert se == {2}
    se |= {1, 3}
    assert se == {1, 2, 3}
    se -= {3}
    assert se == {1, 2}
    se ^= {2, 3}
    assert se == {1, 3}
    assert len(se) == 2
    assert se != {1}
    assert se | {2} == {1, 2, 3}
    assert se - {3} == {1}
    assert se ^ {2, 3, 4} == {1, 2, 4}
    se.add(2)
    assert se == {1, 2, 3}
    se.clear()
    assert not se
    assert not se.copy()
    se = {1, 2, 3}
    assert se.difference({3, 4, 5}) == {1, 2}
    se.difference_update({3, 4, 5})
    assert se == {1, 2}
    se.discard(2)
    assert se == {1}
    assert se.intersection({1, 2, 3}) == {1}
    se.add(2)
    se.add(3)
    se.intersection_update({2, 3})
    assert se == {2, 3}
    assert se.isdisjoint({1, 4})
    assert {2}.issubset(se)
    poppy = se.pop()
    assert poppy == 2 or poppy == 3
    se.remove(3)
    assert not se
    se = {1, 2, 3}
    assert se.symmetric_difference({2, 3, 4}) == {1, 4}
    se.symmetric_difference_update({2, 3, 4})
    assert se == {1, 4}
    assert se.union({2, 3}) == {1, 2, 3, 4}
    se.update({2, 3})
    assert se == {1, 2, 3, 4}
    assert not isinstance(se, Hashable)

    dic = {1: 2, 2: 3}
    assert 1 in dic
    del dic[2]
    assert dic == {1: 2}
    dic |= {2: 3}
    assert dic == {1: 2, 2: 3}
    assert len(dic) == 2
    assert dic != {}
    assert dic | {3: 4} == {1: 2, 2: 3, 3: 4}
    dic[0] = 1
    assert dic == {0: 1, 1: 2, 2: 3}
    dic.clear()
    assert not dic
    assert not dic.copy()
    assert not dic.get(1)
    dic = {1: 2, 2: 3}
    assert str(dic.items()) == "dict_items([(1, 2), (2, 3)])"
    assert dic.keys() == {1, 2}
    assert dic.pop(2) == 3
    assert dic.popitem() == (1, 2)
    dic.setdefault(1, 5)
    assert dic == {1: 5}
    dic.update({2: 3})
    assert dic == {1: 5, 2: 3}
    assert str(dic.values()) == "dict_values([5, 3])"
    assert dict.fromkeys([1, 2, 3]) == {1: None, 2: None, 3: None}
    assert not isinstance(dic, Hashable)
