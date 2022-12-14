import json
import tempfile
from pathlib import Path

from hw.alexey_tyuhai.lesson10.lesson import Counter
from hw.alexey_tyuhai.lesson10.lesson import User


def test_01() -> None:
    hw_text = "hello world"
    petya = User("Петя")
    vasya = User("Вася")

    assert str(petya) == "Петя"
    assert petya.get_class_name() == User.__name__
    assert petya.get_hello_world() == hw_text

    assert str(vasya) == "Вася"
    assert vasya.get_class_name() == User.__name__
    assert vasya.get_hello_world() == hw_text


def test_02() -> None:
    r1 = 3
    ctr1 = Counter(0, r1)
    r2 = 4
    ctr2 = Counter(1, r2)

    assert next(ctr1) == 0
    assert next(ctr1) == 1
    assert next(ctr1) == 2
    list_n = list(ctr2)
    assert list_n == [1, 2, 3]


def test_task_05() -> None:
    petya = User("P")
    js = petya.to_json()

    assert js == '{"name": "P"}'
    assert json.loads(js) == {"name": "P"}

    with tempfile.TemporaryDirectory() as _tmpdir:
        tmpdir = Path(_tmpdir)
        assert tmpdir.is_dir()

        json_file = tmpdir / "asd.json"
        assert not json_file.is_file()

        petya.save_json(json_file)
        assert json_file.is_file()

        with json_file.open("r") as stream:
            jsonobj = json.load(stream)
            assert jsonobj == {"name": "P"}
