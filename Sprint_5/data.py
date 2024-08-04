from dataclasses import dataclass
from random import randint


@dataclass(frozen=True)
class Person:
    USER_NAME = 'Владимир'
    EMAIL = 'roschin_12@gmail.com'
    PASSWORD = '123456'


@dataclass(frozen=True)
class RandomPerson:
    USER_NAME = 'Тестовый_Владимир'
    email = f'test{randint(0, 9999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Q1gaq$'


@dataclass(frozen=True)
class Timeouts:
    SMALL = 3
    MEDIUM = 5
    LARGE = 10


@dataclass(frozen=True)
class Strings:
    BUNS = "Булки"
    SAUCES = "Соусы"
    FILINGS = "Начинки"

    CREATE_ORDER = "Оформить заказ"
    INCORRECT_PASSWORD = "Некорректный пароль"
    USER_ALREADY_EXISTS = "Такой пользователь уже существует"
