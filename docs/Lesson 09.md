# Домашнее задание 9

За каждое задание начисляются баллы.

## Общее ТЗ

1. Пулл-реквест с ДЗ вмержен в ветку `main` до 24.12.2022.
2. В папке `hw/<ваше имя и фамилия>/` есть питон-пакет `lesson09` (далее — _рабочий пакет_).
3. В рабочем пакете есть питон-модуль `tasks.py` (далее - _модуль решений_).
4. Функции-решения задач урока написаны в модуле решения в любом порядке.
5. Функции-решения покрыты тестами в отдельном модуле в рабочем пакете: `tasks_test.py` (далее — _модуль с тестами_).
6. Функции-тесты написаны в модуле с тестами в любом порядке.

## ТЗ по задачам

---

#### 1. Задача про декоратор do_twice (+1)

Существует функция с названием `task_01_do_twice`.

Функция реализует декоратор: декорированная функция будет вызвана дважды.

Пример:

```python
def task_01_do_twice(func): ...

@task_01_do_twice
def f(lst):
    lst.append(1)

def test_01():
    x = []
    f(x)
    assert len(x) == 2
```

---

#### 2. Задача про декоратор, считающий запуски функций (+1)

Существует функция с названием `task_02_count_calls`.

Функция реализует декоратор: считает количество запусков декорированной функции.

Пример:

```python
counter = {}

def task_02_count_calls(func): ...

@task_02_count_calls
def f(): pass

@task_02_count_calls
def g(): pass

def test_02():
    assert not counter
    [ (f(), g()) for _ in "123" ]
    [ f() for _ in "123" ]
    assert counter["f"] == 6
    assert counter["g"] == 3
```

---

#### 3. Задача про бенчмарк (+2)

Существует функция с названием `task_04_benchmark`.

Функция реализует декоратор: кэширует запуск декорированной функции.

Пример:

```python
def test_03_benchmark(func):
    # здесь ваш код!
    ...

import time

@test_03_benchmark
def slowpoke(n):
    time.sleep(n)

def test_03():
    t = time.monotonic()
    slowpoke(1)  # дольше не спать! тесты будут педалить
    dt = time.monotonic() - t
    assert abs(dt - 1) < 0.1
```

---

#### 4. Задача про типизацию (+2)

Существует функция с названием `task_04_typecheck`.

Функция реализует декоратор: проверяет типы переданных аргументов и результата
у декорированной функции. Декорированная функция принимает аргументы только по имени.

Пример:

```python
def task_04_typecheck(func):
    # здесь ваш код!
    ...

@task_04_typecheck
def f(*, a: int, b: int) -> int:
    return b * a

@task_04_typecheck
def g() -> int:
    return "1"  # type: ignore

import pytest

def test_04():
    assert f(a=2, b=3) == 6

    with pytest.raises(TypeError):
        f(a=2, b=0.2)  # type: ignore

    with pytest.raises(TypeError):
        g()
```

Для проверки типа использовать инструкции:

```python
if not isinstance(a, b):
    raise TypeError(f"{a=!r} is not of type {b}")
```

---

#### 5. Задача про кэш (+4)

Существует функция с названием `task_05_cache`.

Функция реализует декоратор: кэширует запуск декорированной функции.

Пример:

```python
def task_05_cache(func):
    # здесь ваш код!
    ...

@task_05_cache
def bad(x=[]):
    x.append(1)
    return x

def test_05():
    y = bad()
    assert y == [1]
    
    z = [bad() for _ in "123"][-1]
    assert z is y
    
    data = [1,2,3,4]
    r1 = bad(data)
    r2 = bad(data)
    r3 = bad([1,2])
    assert data == [1,2,3,4,1]
    assert r1 is data
    assert r2 is r1
    assert r3 is not r1
    assert r3 == [1,2,1]
```

