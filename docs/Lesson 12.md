# Домашнее задание 12

За каждое задание начисляются баллы.

## Общее ТЗ

1. Пулл-реквест с ДЗ вмержен в ветку `main` до 11.1.2023.
2. Ветка называется в формате `<imia>-<familia>-lesson-12`: строчные латинские буквы, разделитель — дефис `-`.
3. Пулл-реквест называется в формате `<Imia> <Familia> Lesson 12`: латинские буквы, первая заглавная, слова разделяются пробелами.
2. В папке `hw/<ваше имя и фамилия>/` есть питон-пакет `lesson12` (далее — _рабочий пакет_).
3. В рабочем пакете есть питон-модуль `lesson.py` (далее - _модуль решений_).
4. Код покрыт тестами в отдельном модуле в рабочем пакете: `lesson_test.py` (далее — _модуль с тестами_).
5. Код покрыт тестами на 100%.
6. На ревью предоставляется рабочий код с "зелёным" статусом пулл-реквеста.
   Оценка уменьшается на 1 за:
   1. "красный" статус, если произошел из-за вашего кода;
   2. непротестированный код, не покрытый тестами на 100%;
   3. несоответствие ТЗ;
   4. некорректное использование прошедшего материала (напр. вызов вручную магических методов);
7. Готовым для ревью считается пулл-реквест с лейблом [pr:ready-for-review](https://github.com/alexander-sidorov/m-pt1-58-22/labels).
8. Непонятные места в ТЗ, коде можно решать без предоставления ПР на ревью.


## ТЗ по задачам

---

#### 1. класс `Url` (+3)

Существует класс с названием `Url`.

Класс повторяет логику функции `urllib.parse.urlsplit`:
декомпозирует URL и сохраняет его компоненты в атрибуты объекта класса.
Атрибуты должны быть ровно такими же, и в том же количестве, как в примерах ниже:

Пример:

```python
url = Url("http://google.com")
assert url.scheme == "http"
assert url.username is None
assert url.password is None
assert url.host == "google.com"
assert url.port is None
assert url.path is None  # в этом случае можно "" или "/"
assert url.query is None
assert url.fragment is None


url = Url("postgresql://u:p@db:5432/dbname?opt=1&xyz=2#f")
assert url.scheme == "postgresql"
assert url.username == "u"
assert url.password == "p"
assert url.host == "db"
assert url.port == 5432
assert url.path == "/dbname"
assert url.query == "opt=1&xyz=2"
assert url.fragment == "f"
```

Класс должен быть протестирован на следующих URL-ах:

1. `http://google.com`
2. `postgresql://u:p@db:5432/dbname?opt=1&xyz=2#f`
3. `vnc://user@host?query=q`
4. `vnc://user@host/?query=q`
5. `ftp://a.b.c.host/p/a/t/h?query=q&f=f#f`

Алгортимы класса должны быть реализованы
без использования стандартной библиотеки.

---

#### 2. Класс `HttpRequest` (+2)

Существует класс `HttpRequest`. Он декомпозирует переданный ему HTTP запрос
на компоненты. Компоненты сохраняются в атрибуты объекта класса.
Атрибуты должны быть такие же и в таком же количестве, как в примерах ниже:

```python
message = """HEAD / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: github.com
User-Agent: HTTPie/3.2.1

"""

req = HttpRequest(message)

assert req.method == "GET"
assert req.path == "/"
assert req.http_version == "HTTP/1.1"
assert req.headers == {
   "Accept": "*/*",
   "Accept-Encoding": "gzip, deflate",
   "Connection": "keep-alive",
   "Host": "github.com",
   "User-Agent": "HTTPie/3.2.1",
}
assert req.body is None
```

Алгортимы класса могут быть реализованы
с использованием стандартной библиотеки.

---

#### 3. Класс `HttpResponse` (+5)

Существует класс `HttpResponse`. Он декомпозирует переданный ему HTTP ответ
на компоненты. Компоненты сохраняются в атрибуты объекта класса.
Атрибуты должны быть такие же и в таком же количестве, как в примерах ниже.

У класса есть метод `is_valid`, который возвращает `True`, если
в сообщении длина контента из заголовка совпадает с длиной тела сообщения.

У класса есть метод `json`, который возвращает десериализованный JSON объект
из тела соощения, если сообщение валидное и заголовки указыват на то, что
передан JSON. Если заголовки указывают на JSON, а в теле не JSON — специально не
обрабатывать этот случай.
Если заголовки не указывают на JSON — метод должен возвращать None

```python
message = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: application/json
Server: gunicorn/19.9.0

{"status_code": 404, "description": "no access"}
"""

resp = HttpResponse(message)

assert resp.status_code == 404
assert resp.reason == "Not Found"
assert resp.http_version == "HTTP/1.1"
assert resp.headers == {
    "Content-Length": 48,
    "Content-Type": "application/json",
    "Server": "gunicorn/19.9.0",
}
assert resp.body == '{"status_code": 404, "description": "no access"}'
assert resp.is_valid()
assert resp.json() == {"status_code": 404, "description": "no access"}
```

```python
message = """HTTP/1.1 404 NOT FOUND
Content-Length: 49
Content-Type: text/html
Server: gunicorn/19.9.0

{"status_code": 404, "description": "no access"}
"""

resp = HttpResponse(message)

assert not resp.is_valid()
assert resp.json() is None
```

```python
message = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: text/html
Server: gunicorn/19.9.0

{"status_code": 404, "description": "no access"}
"""

resp = HttpResponse(message)

assert resp.is_valid()
assert resp.json() is None
```

Алгортимы класса могут быть реализованы
с использованием стандартной библиотеки.
