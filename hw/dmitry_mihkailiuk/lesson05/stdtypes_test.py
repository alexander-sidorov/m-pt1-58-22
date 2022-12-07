from typing import Hashable


def test_str() -> None:
    #__add__
    assert "a" + "b" == "ab"

    # __contains__
    assert "b" in "abc"

    # __getitem__
    assert "abc"[1] == "b"

    # __hash__
    assert isinstance("", Hashable)

    # __len__
    assert len("abc") == 3

    # __mod__
    assert "%s%s%s" % ("a", "b", "c") == "abc"

    # __mul__
    assert "abc" * 2 == "abcabc"

    assert "abc" < "abd"

    assert 'abc'.capitalize() == "Abc"

    assert "aBc".casefold() == "abc"

    assert "abc".center(5, "*") == "*abc*"

    assert "abca".count("a") == 2

    assert "abc".encode() == b"abc"

    assert "abc.".endswith(".")

    assert "a\tb".expandtabs(2) == "a b"

    assert "abc".find("b") == 1

    assert "a{}c".format("b") == "abc"

    assert "{a}{b}{c}".format_map({"a": "H", "b": "i", "c": "!"}) == "Hi!"

    assert "abc".index("c") == 2

    assert "abc123".isalnum()

    assert "abc".isalpha()

    assert "abc".isascii()

    assert not "abc".isdecimal()

    assert "123".isdigit()

    assert "abc_123".isidentifier()

    assert "abc".islower()

    assert not "-1".isnumeric()

    assert not "abc\n".isprintable()

    assert "  ".isspace()

    assert "Abc".istitle()

    assert "ABC".isupper()

    assert "#".join(["a", "b", "c"]) == "a#b#c"

    assert "abc".ljust(5) == "abc  "

    assert "AbC".lower() == "abc"

    assert "  abc  ".lstrip() == "abc  "

    assert "adc".maketrans("d", "b") == {100: 98}

    assert "abc".partition("c") == ('ab', 'c', '')

    assert "abc".removeprefix("a") == "bc"

    assert "abc".removesuffix("bc") == "a"

    assert "abd".replace("d", "c") == "abc"

    assert "abcabc".rfind("bc") == 4

    assert "abcabc".rindex("bc") == 4

    assert "abc".rjust(5, "#") == "##abc"

    assert "abcabc".rpartition("ca") == ('ab', 'ca', 'bc')

    assert "a, b, c".rsplit(", ", 1) == ['a, b', 'c']

    assert "   abc   ".rstrip() == "   abc"

    assert "a b c".split() == ["a", "b", "c"]

    assert "abc\nabc".splitlines() == ["abc", "abc"]

    assert "abc".startswith("a")

    assert "   abc    ".strip() == "abc"

    assert "abcABC".swapcase() == "ABCabc"

    assert "abc".title() == "Abc"

    assert "dbc".translate({100: 97}) == "abc"

    assert "abc".upper() == "ABC"

    assert "abc".zfill(5) == "00abc"


def test_tuple() -> None:
    # __add__
    assert ("a",) + ("b",) == ("a", "b")

    # __contains__
    assert "a" in ("a", "b", "c")

    # __getitem__
    assert ("a", "b", "c")[1] == "b"

    # __hash__
    assert isinstance(("a", "b", "c"), Hashable)

    # __len__
    assert len(("a", "b", "c")) == 3

    # __mul__
    assert ("a", "b", "c") * 2 == ("a", "b", "c", "a", "b", "c")

    assert ("a",) < ("b",)

    assert ("a", "b", "c", "d", "e", "b").count("b") == 2

    assert ("a", "b", "c", "d", "e", "b").index("b") == 1


def test_list() -> None:
    # __add__
    assert ["a"] + ["b"] == ["a", "b"]

    # __contains__
    assert "a" in ["a", "b", "c"]

    # __delitem__
    list1 = ["a", "b", "c"]
    del list1[1]
    assert list1 == ["a", "c"]

    # __getitem__
    assert ["a", "b", "c"][2] == "c"

    # __hash__
    assert not isinstance(["a", "b", "c"], Hashable)

    # __iadd__
    list1 = ["a"]
    list1 += ["b"]
    assert list1 == ["a", "b"]

    # __imul__
    list1 = ["a"]
    list1 *= 2
    assert list1 == ["a", "a"]

    # __len__
    assert len(["a", "b", "c"]) == 3

    # __mul__
    assert ["a", "b"] * 2 == ["a", "b", "a", "b"]

    # __setitem__
    list1 = ["a", "b"]
    list1[1] = "c"
    assert list1 == ["a", "c"]

    assert ["a"] < ["a", "b"]

    list1 = ["a"]
    list1.append("b")
    assert list1 == ["a", "b"]

    list1 = ["a", "b"]
    list1.clear()
    assert list1 == []

    list1 = ["a"]
    list2 = list1.copy()
    assert list2 == ["a"]

    assert ["a", "c", "b", "c"].count("c") == 2

    list1 = ["a", "b"]
    list1.extend(["c", "d"])
    assert list1 == ["a", "b", "c", "d"]

    assert ["a", "b", "c"].index("b") == 1

    list1 = ["a", "c"]
    list1.insert(1, "b")
    assert list1 == ["a", "b", "c"]

    list1 = ["a", "b", "c"]
    list1.pop(1)
    assert list1 == ["a", "c"]

    list1 = ["a", "b", "c"]
    list1.remove("a")
    assert list1 == ["b", "c"]

    list1 = ["a", "b", "c"]
    list1.reverse()
    assert list1 == ["c", "b", "a"]

    list1 = ["c", "b", "a", "a", "b", "c"]
    list1.sort()
    assert list1 == ['a', 'a', 'b', 'b', 'c', 'c']


