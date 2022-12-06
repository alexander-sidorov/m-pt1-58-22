ATTRS_NO_TEST = set[str] {
    "__class__",
    "__class_getitem__",
    "__delattr__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__getnewargs__",
    "__gt__",
    "__init__",
    "__init_subclass__",
    "__iter__",
    "__le__",
    "__lt__",
    "__ne__",
    "__new__",
    "__rand__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__reversed__",
    "__rmod__",
    "__rmul__",
    "__ror__",
    "__rsub__",
    "__rxor__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
}


CITIES: dict[str, tuple[float, float]] = {
    "Барановичи": (53.132227, 26.017363),
    "Берёза": (52.534754, 24.984273),
    "Бобруйск": (53.145646, 29.225297),
    "Борисов": (54.224141, 28.511507),
    "Браслав": (55.639499, 27.031569),
    "Брест": (52.093721, 23.684757),
    "Витебск": (55.184204, 30.202767),
    "Волковыск": (53.162982, 24.463780),
    "Глубокое": (55.138798, 27.685619),
    "Гомель": (52.424280, 31.014063),
    "Гродно": (53.677764, 23.829300),
    "Житковичи": (52.217048, 27.854883),
    "Жлобин": (52.892235, 30.037624),
    "Жодино": (54.094370, 28.321572),
    "Кобрин": (52.208612, 24.354257),
    "Лепель": (54.886647, 28.693817),
    "Лида": (53.891662, 25.302200),
    "Минск": (53.902735, 27.555696),
    "Мозырь": (52.049078, 29.267184),
    "Молодечно": (54.307345, 26.838960),
    "Орша": (54.510823, 30.429367),
    "Пинск": (52.111481, 26.102166),
    "Полоцк": (55.485590, 28.767977),
    "Поставы": (55.113615, 26.839303),
    "Речица": (52.371565, 30.386450),
    "Светлогорск": (52.633044, 29.748194),
    "Слуцк": (53.027615, 27.552063),
    "Солигорск": (52.792866, 27.543479),
}
