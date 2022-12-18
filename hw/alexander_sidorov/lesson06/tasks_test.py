from hw.alexander_sidorov.lesson06.tasks import task_01_boundary
from hw.alexander_sidorov.lesson06.tasks import task_02_expand
from hw.alexander_sidorov.lesson06.tasks import task_03_hdist
from hw.alexander_sidorov.lesson06.tasks import task_04_cities
from hw.alexander_sidorov.lesson06.tasks import task_05_route


def test_01() -> None:
    assert task_01_boundary("ab") == ("a", "b")
    assert task_01_boundary("a") == ("a", "a")


def test_02() -> None:
    assert task_02_expand([3, 1j, "1"]) == [1j, "1", 1j, "1", 1j, "1"]
    assert task_02_expand((3, 1j, "1")) == (1j, "1", 1j, "1", 1j, "1")
    assert task_02_expand([0, 1j, "1"]) == []
    assert task_02_expand((0, 1j, "1")) == ()
    assert task_02_expand([-1, 1j, "1"]) == []
    assert task_02_expand((-1, 1j, "1")) == ()


def test_03() -> None:
    assert task_03_hdist("ab", "ab") == 0
    assert task_03_hdist("ab", "abc") == 1
    assert task_03_hdist("abc", "ab") == 1
    assert task_03_hdist("abc", "ac") == 2
    assert task_03_hdist((1, 2), (1, 2)) == 0
    assert task_03_hdist([1], [1]) == 0
    assert task_03_hdist([1, 1], [1, 2]) == 1
    assert task_03_hdist([], []) == 0


def test_04() -> None:
    distances = task_04_cities("Минск")
    km = distances["Жодино"]
    assert int(km) == 54


def test_05() -> None:
    km = task_05_route(("Минск", "Минск", "Жодино", "Жодино", "Минск"))
    assert int(km) == 108
