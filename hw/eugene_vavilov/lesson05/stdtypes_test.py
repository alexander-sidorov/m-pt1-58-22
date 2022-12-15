from typing import Hashable


def test_list() -> None:

    assert [1, 2, 3] < [2, 3]
    assert [1, 2, 3] > [0, 90]

    assert [1] + [2] == [1, 2]  # __add__

    assert 2 in [1, 2, 3]  # __contains__

    my_list = [1, 2, 3]
    del my_list[1]
    assert my_list == [1, 3]  # __delitem__

    assert [1, 2, 3][1] == 2  # __getitem__

    my_list = [0, 1]
    my_list += [2]
    assert [0, 1, 2] == my_list  # __iadd__

    my_list = [2]
    my_list *= 4
    assert [2, 2, 2, 2] == my_list  # __imul__

    assert len([1, 2, 3]) == 3  # __len__

    assert [1] * 4 == [1, 1, 1, 1]  # __mul__

    assert [1, 2, 3][2] == 3  # __setitem__

    my_list = [1, 2]
    my_list.append(3)
    assert my_list == [1, 2, 3]

    my_list = [1, 2]
    my_list.clear()
    assert my_list == []

    my_list = [1]
    my_list_copy = my_list.copy()
    assert my_list_copy == [1]

    my_list = [0, 0, 1, 1, 1, 2]
    assert my_list.count(1) == 3

    my_list = [0, 1]
    my_list.extend([2, 3])
    assert my_list == [0, 1, 2, 3]

    my_list = [3, 4, 5]
    assert my_list.index(4) == 1

    my_list = [1, 2, 4]
    my_list.insert(2, 3)
    assert my_list == [1, 2, 3, 4]

    my_list = [1, 2, 3, 4, 7]
    my_list.pop()
    assert my_list == [1, 2, 3, 4]

    my_list = [1, 2, 3, 4, 7]
    my_list.remove(3)
    assert my_list == [1, 2, 4, 7]

    my_list = [1, 2, 3, 4, 7]
    my_list.reverse()
    assert my_list == [7, 4, 3, 2, 1]

    my_list = [1, 5, 2, 8, 7]
    my_list.sort()
    assert my_list == [1, 2, 5, 7, 8]

    assert type([1, 2, 3]) == list

    assert not isinstance(["a", "b", "c"], Hashable)


def test_tuple() -> None:

    my_tuple = (1, 2, 3, 4)

    assert (1, 2, 3) < (2, 3)
    assert (1, 2, 3) > (0, 90)

    assert my_tuple + (5, 6) == (1, 2, 3, 4, 5, 6)  # __add__

    assert 2 in my_tuple  # __contains__

    assert my_tuple[2] == 3  # __getitem__

    assert len(my_tuple) == 4  # __len__

    assert my_tuple * 2 == (1, 2, 3, 4, 1, 2, 3, 4)  # __mul__

    assert my_tuple.count(3) == 1

    assert my_tuple.index(3) == 2

    assert type(my_tuple) == tuple

    assert isinstance(("a", "b", "c"), Hashable)


def test_str() -> None:

    assert "1, 2, 3" < "2, 3"
    assert "1, 2, 3" > "0, 90"

    assert "a" + "b" == "ab"  # __add__

    assert "aa" in "aabbcc"  # __contains__

    assert "Hello {}".format("world!") == "Hello world!"  # __format__

    assert "Hello"[2] == "l"  # __getitem__

    assert isinstance("", Hashable)

    assert len("Hello") == 5  # __len__

    assert ("%s %s" % ("H", "w")) == "H w"  # noqa: S001,MOD001

    assert "a" * 5 == "aaaaa"  # __mul__

    assert "hELLo WORLD".capitalize() == "Hello world"

    assert "HeLlO worLd".casefold() == "hello world"

    assert "Hello world".center(15, "!") == "!!Hello world!!"

    assert "hello worLd".count("l") == 2

    assert (
        "hello_world дороу".encode()
        == b"hello_world \xd0\xb4\xd0\xbe\xd1\x80\xd0\xbe\xd1\x83"
    )

    assert "hello world".endswith("world")

    assert "hello\tworld".expandtabs(1) == "hello world"

    assert "hello world".find("ll") == 2

    assert "Hello {}".format("World") == "Hello World"

    assert "Hello {what}".format_map({"what": "world"}) == "Hello world"

    assert "Hello world".index("e") == 1

    assert "HelloWorld111".isalnum()

    assert "HelloWorld".isalpha()

    assert "Hello World123-+= ".isascii()

    assert "22800".isdecimal()

    assert "223".isdigit()

    assert "cats22_4".isidentifier()

    assert "hello world2_12.2".islower()

    assert "⅓".isnumeric()

    assert "abc123-=+/.,<>фбв".isprintable()

    assert "    \t\n".isspace()

    assert "Hello World 223 +-+=,./ Привет".istitle()

    assert "HELLO WORLD 224-=".isupper()

    assert ",".join(["Hello", "world", "1"]) == "Hello,world,1"

    assert "Hell".ljust(11, "o") == "Hellooooooo"

    assert "HELLO world".lower() == "hello world"

    assert "               hello world".lstrip() == "hello world"

    assert "hello world".partition(" ") == ("hello", " ", "world")

    assert "goodbye hello world".removeprefix("goodbye") == " hello world"

    assert "goodbye hello world".removesuffix(" world") == "goodbye hello"

    assert (
        "goodbye world goodbye".replace("goodbye", "hello", 1)
        == "hello world goodbye"
    )

    assert "Hello world".rfind("l") == 9

    assert "Hello world".rindex("l") == 9

    assert "Hello world".rjust(13, "@") == "@@Hello world"

    assert "Hello the World".rpartition(" ") == ("Hello the", " ", "World")

    assert "Hello 1world 1hello".rsplit(" 1") == ["Hello", "world", "hello"]

    assert "Hello world".rstrip("world") == "Hello "

    assert "H1 w1 h".split("1 ") == ["H", "w", "h"]  # noqa: SIM905

    assert "Hello\rworld\n".splitlines() == ["Hello", "world"]

    assert "Hello world".startswith("Hello")

    assert "@@Hello @world@@@@".strip("@") == "Hello @world"

    assert "HELLO world !!!1".swapcase() == "hello WORLD !!!1"

    assert "heLLo woRLD !".title() == "Hello World !"

    trans_table = str.maketrans({"*": "a"})
    assert "N*gger".translate(trans_table) == "Nagger"

    assert "hello WoRLD".upper() == "HELLO WORLD"

    assert "world".zfill(11) == "000000world"

    assert str.maketrans("a", "1") == {97: 49}


assert {1, 2, 3} > {2, 3}
assert {1, 2, 3} < {1, 2, 3, 5}


def test_set() -> None:

    assert {1, 2, 3} > {2, 3}
    assert {1, 2, 3} < {1, 2, 3, 5}

    assert {1, 2, 3} & {3, 4} == {3}  # __and__

    assert 1 in {1, 2, 3}  # __contains__

    my_set = {1, 2, 3}
    my_set &= {2}
    assert my_set == {2}  # __iand__

    my_set = {1, 2, 3}
    my_set |= {7}
    assert my_set == {1, 2, 3, 7}  # __ior__

    my_set = {1, 2, 3}
    my_set -= {2}
    assert my_set == {1, 3}  # __isub__

    my_set = {1, 2, 3}
    my_set1 = {1, 2, 3}
    my_set ^= {3}
    my_set1 ^= {5}
    assert my_set == {1, 2} and my_set1 == {1, 2, 3, 5}  # __ixor__

    assert len({1, 2, 3, 4, 5, 6}) == 6  # __len__

    assert {1, 2, 3} | {7} == {1, 2, 3, 7}  # __or__

    assert {1, 2, 3} - {2} == {1, 3} and {1, 2, 3} - {4} == {
        1,
        2,
        3,
    }  # __sub__

    assert {1, 2, 3} ^ {3} == {1, 2} and {1, 2, 3} ^ {5} == {
        1,
        2,
        3,
        5,
    }  # __xor__

    my_set = {1, 2, 3}
    my_set.add(4)
    assert my_set == {1, 2, 3, 4}

    my_set = {1, 2, 3}
    my_set.clear()
    assert my_set == set()

    my_set = {1, 2, 3, 4}
    my_set1 = my_set.copy()
    assert my_set == my_set1 and my_set is not my_set1

    my_set = {1, 2, 3, 4}
    my_set1 = {3, 4, 5, 6}
    my_set = my_set1.difference(my_set)
    assert my_set == {6, 5}

    my_set = {1, 2, 3, 4}
    my_set1 = {3, 4, 5, 6}
    my_set.difference_update(my_set1)
    assert my_set == {1, 2}

    my_set = {1, 2, 3}
    my_set.discard(2)
    assert my_set == {1, 3}

    assert {1, 2, 3, 4}.intersection({3, 4, 5, 6}) == {3, 4}

    my_set = {1, 2, 3, 4}
    my_set1 = {3, 4, 5, 6}
    (my_set.intersection_update(my_set1))
    assert my_set == {3, 4}

    assert {1, 2, 3, 4}.isdisjoint({5, 6})

    my_set = {1, 2, 3}
    assert (
        not my_set.issubset({1, 2})
        and my_set.issubset({1, 2, 3})
        and my_set.issubset({1, 2, 3, 4})
    )

    my_set = {1, 2, 3}
    assert (
        not my_set.issuperset({1, 2, 3, 4})
        and my_set.issuperset({1, 2, 3})
        and my_set.issuperset({1, 2})
    )

    my_set = {3, 1, 2, 0}
    my_set.pop()
    assert my_set == {1, 2, 3}

    my_set = {1, 2, 3, 4}
    my_set.remove(3)
    assert my_set == {1, 2, 4}

    assert {1, 2, 4}.symmetric_difference({2, 3, 4, 6}) == {1, 3, 6}

    my_set = {1, 2, 4}
    my_set.symmetric_difference_update({2, 3, 4, 6})
    assert my_set == {1, 3, 6}

    my_set = {1, 2, 3, 4}.union({4, 5, 6})
    assert my_set == {1, 2, 3, 4, 5, 6}

    my_set = {1, 2, 3, 4}
    my_set.update({4, 5, 6})
    assert my_set == {1, 2, 3, 4, 5, 6}

    assert not isinstance({"a", "b"}, Hashable)

    assert type({1, 2}) is set


def test_dict() -> None:

    assert 1 in {1: "1", 2: "2", 3: "3"} and "1" not in {
        1: "1",
        2: "2",
        3: "3",
    }  # __contains__

    my_dict = {1: "1", 2: "2", 3: "3"}
    del my_dict[2]
    assert my_dict == {1: "1", 3: "3"}  # __delete__

    assert {"a": "1", "b": "2"}["b"] == "2"  # __getitem__

    my_dict = {1: "1", 2: "2"}
    my_dict |= {3: "3"}
    assert my_dict == {1: "1", 2: "2", 3: "3"}  # __ior__

    assert len({"a": "1", "b": "2", "c": "3"}) == 3

    assert {"a": "1", "b": "2"} | {"c": "3", "b": "2"} == {
        "a": "1",
        "b": "2",
        "c": "3",
    }  # __or__

    assert {"a": "1", "b": "2", "c": "3"}["b"] == "2"  # __setitem__

    my_dict = {1: "1", 2: "2"}
    my_dict.clear()
    assert my_dict == {}

    my_dict = {1: "1", 2: "2"}
    my_dict1 = my_dict.copy()
    assert my_dict == my_dict1 and my_dict1 is not my_dict

    assert {"a": "1", "b": "2", "c": "3"}.get("b") == "2"

    my_dict = {1: "1", 2: "2", 3: "3"}
    assert str(my_dict.items()) == "dict_items([(1, '1'), (2, '2'), (3, '3')])"

    my_dict = {1: "1", 2: "2", 3: "3"}
    assert str(my_dict.keys()) == "dict_keys([1, 2, 3])"

    my_dict = {1: "1", 2: "2", 3: "3"}
    assert my_dict.pop(3) == "3"

    my_dict = {1: "1", 2: "2", 3: "3"}
    my_dict.popitem()
    assert my_dict == {1: "1", 2: "2"}

    my_dict = {1: "1", 2: "2", 3: "3"}
    my_dict.setdefault(4, "4")
    assert my_dict[4] == "4"

    my_dict = {1: "1", 2: "2", 3: "3"}
    my_dict.update({4: "4"})
    assert my_dict == {1: "1", 2: "2", 3: "3", 4: "4"}

    my_dict = {1: "1", 2: "2", 3: "3"}
    assert str(my_dict.values()) == "dict_values(['1', '2', '3'])"

    dict1 = {1: "a", 2: "b"}
    assert not isinstance(dict1, Hashable)

    my_dict = dict.fromkeys([1, 2, 3, 4], "0")
    assert my_dict == {1: "0", 2: "0", 3: "0", 4: "0"}
