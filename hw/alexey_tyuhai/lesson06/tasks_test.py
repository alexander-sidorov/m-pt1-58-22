import hw.alexey_tyuhai.lesson06.tasks as les6


def test_task_01_boundary() -> None:

    assert les6.task_01_boundary("ab") == ("a", "b")
    assert les6.task_01_boundary([1, 2, 3, 4]) == (1, 4)
    assert les6.task_01_boundary((1, 2, 3, 4)) == (1, 4)


def test_task_02_expand() -> None:

    assert les6.task_02_expand([2, 3, 4]) == [3, 4, 3, 4]
    assert les6.task_02_expand((3, 1, 2)) == (1, 2, 1, 2, 1, 2)


def test_task_03_hdist() -> None:

    assert les6.task_03_hdist("aaa", "aab") == 1
    assert les6.task_03_hdist("aaa", "aba") == 1
    assert les6.task_03_hdist("aaa", "baa") == 1
    assert les6.task_03_hdist("", "baa") == 3
    assert les6.task_03_hdist([1, 2, 3, 4], [2, 3, 5, 4]) == 3
    assert les6.task_03_hdist(("22", "dd", "hh"), (1, 2, 3)) == 3


def test_task_04_cities() -> None:

    distances = les6.task_04_cities("Минск")
    km = distances["Жодино"]
    assert int(km) == 54
    distances = les6.task_04_cities("Слуцк")
    km = distances["Солигорск"]
    assert int(km) == 26


def test_task_05_route() -> None:

    km = les6.task_05_route(
        ("Минск", "Минск", "Жодино", "New-York", "Жодино", "Минск")
    )
    assert int(km) == 108
