import json
from pathlib import Path
import tempfile

from hw.dmitry_mihkailiuk.lesson10.lesson import Counter
from hw.dmitry_mihkailiuk.lesson10.lesson import User


def test_01() -> None:
    dim = User("Dim")
    assert str(dim) == "Dim"
    assert dim.get_class_name() == "User"
    assert dim.get_hello_world() == "hello world"

    js = dim.to_json()
    assert js == '{"name": "Dim"}'
    assert json.loads(js) == {"name": "Dim"}

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        assert tmpdir.is_dir()

        json_file = tmpdir / "data.json"
        assert not json_file.is_file()

        dim.save_json(json_file)
        assert json_file.is_file()

        with json_file.open("r") as stream:
            jsonobj = json.load(stream)
            assert jsonobj == {"name": "Dim"}


def test_02() -> None:
    ctr1 = Counter(0, 5)

    ctr2 = Counter(0, 2)

    assert next(ctr1) == 0

    list_num = list(ctr1)
    assert list_num == [1, 2, 3, 4]

    assert next(ctr2) == 0
    assert next(ctr2) == 1
