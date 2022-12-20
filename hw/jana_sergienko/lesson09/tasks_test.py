from hw.jana_sergienko.lesson09.tasks import task_01_do_twice


@task_01_do_twice
def f01(lst: list) -> None:
    lst.append(1)


def test_task_01_do_twice() -> None:
    x01: list[None] = []
    f01(x01)
    assert len(x01) == 2
