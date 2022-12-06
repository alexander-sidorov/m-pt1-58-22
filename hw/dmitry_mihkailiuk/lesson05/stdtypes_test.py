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