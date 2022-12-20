from hw.jana_sergienko.lesson09.tasks import task_01_do_twice


@task_01_do_twice
def f(lst: list) -> None:
    lst.append(1)


def test_task_01_do_twice() -> None:
    x: list[None] = []
    f(x)
    assert len(x) == 2
