from hw.eugene_ladyko.lesson06.tasks import task_01_boundary
from hw.eugene_ladyko.lesson06.tasks import task_02_expand
from hw.eugene_ladyko.lesson06.tasks import task_03_hdist
from hw.eugene_ladyko.lesson06.tasks import task_04_cities
from hw.eugene_ladyko.lesson06.tasks import task_05_route


def test_task_01_boundary() -> None:
    assert task_01_boundary([1, 3, 8, 7]) == (1, 7)
    assert task_01_boundary((3, 5, 8, 9)) == (3, 9)
    assert task_01_boundary("python") == ("p", "n")


def test_task_02_expand() -> None:
    assert task_02_expand([2, "py"]) == ["py", "py"]
    assert task_02_expand((2, 4, 2)) == (4, 2, 4, 2)


def test_task_03_hdist() -> None:
    assert task_03_hdist("rod", "row") == 1
    assert task_03_hdist("el", "else") == 2
    assert task_03_hdist("python", "") == 6
    assert task_03_hdist("zxc", "qwe") == 3


def test_task_04_cities() -> None:
    distances = task_04_cities("Минск")
    km = distances["Берёза"]
    assert int(km) == 225
    km = distances["Лида"]
    assert int(km) == 146


def test_task_05_route() -> None:
    km = task_05_route(("Минск", "Минск", "Жодино", "Жодино", "Минск"))
    assert int(km) == 108
    km = task_05_route(("Минск", "Берёза", "Brest", "Гродно"))
    assert int(km) == 373
