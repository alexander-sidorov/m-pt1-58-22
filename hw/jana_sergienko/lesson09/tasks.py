def task_01_do_twice(func) -> None:
    def wrapper(*args, **kwargs) -> None:
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper
