from hw.dmitry_mihkailiuk.lesson06.tasks import task_01_boundary
from hw.dmitry_mihkailiuk.lesson06.tasks import task_02_expand
from hw.dmitry_mihkailiuk.lesson06.tasks import task_03_hdist
from hw.dmitry_mihkailiuk.lesson06.tasks import task_04_cities
from hw.dmitry_mihkailiuk.lesson06.tasks import task_05_route


def test_task_01_boundary() -> None:
    assert task_01_boundary("ab") == ("a", "b")


def test_task_02_expand() -> None:
    assert task_02_expand([2, 3, 4]) == [3, 4, 3, 4]


def test_task_03_hdist() -> None:
    assert task_03_hdist("aaa", "aab") == 1
    assert task_03_hdist("aaa", "aba") == 1
    assert task_03_hdist("aaa", "baa") == 1
    assert task_03_hdist("", "baa") == 3
    assert task_03_hdist("aa", "baa") == 2


def test_task_04_cities() -> None:
    distances = task_04_cities("Минск")
    km = distances["Жодино"]
    assert int(km) == 54


def test_task_05_route() -> None:
    km = task_05_route(("Минск", "Минск", "Жодино", "Жодино", "Минск"))
    assert int(km) == 108
