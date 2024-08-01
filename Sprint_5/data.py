from dataclasses import dataclass
from random import randint


@dataclass(frozen=True)
class Person:
    user_name = 'Владимир'
    email = 'roschin_12@gmail.com'
    password = '123456'


@dataclass(frozen=True)
class RandomPerson:
    user_name = 'Тестовый_Владимир'
    email = f'test{randint(0, 9999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Q1gaq$'


@dataclass(frozen=True)
class Timeouts:
    small = 3
    medium = 5
    large = 10
