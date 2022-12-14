from hw.eugene_vavilov.lesson06.tasks import task_01_boundary
from hw.eugene_vavilov.lesson06.tasks import task_02_expand
from hw.eugene_vavilov.lesson06.tasks import task_03_hdist
from hw.eugene_vavilov.lesson06.tasks import task_04_cities
from hw.eugene_vavilov.lesson06.tasks import task_05_route


def test_task_01_boundary() -> None:
    assert task_01_boundary("ab") == ("a", "b")
    assert task_01_boundary("a") == ("a", "a")


def test_task_02_expand() -> None:
    assert task_02_expand([2, 3, 4]) == [3, 4, 3, 4]


def test_task_03_hdist() -> None:
    assert task_03_hdist("aaa", "aab") == 1
    assert task_03_hdist("aaa", "aba") == 1
    assert task_03_hdist("aaa", "ba") == 2
    assert task_03_hdist("", "baa") == 3
    assert task_03_hdist("aa", "baa") == 2


def test_task_04_cities() -> None:
    distances = task_04_cities("Минск")
    km = distances["Жодино"]
    assert int(km) == 54


def test_task_05_route() -> None:
    km = task_05_route(("Минск", "Минск", "Жодино", "Жодино", "Минск"))
    assert int(km) == 108
    km = task_05_route(
        (
            "Минск",
            "Минск",
            "Жодино",
            "asdjashdasAAHSDH23423",
            "Жодино",
            "Минск",
        )
    )
    assert int(km) == 108
