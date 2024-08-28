import datetime

import requests
from faker import Faker

from urls import Urls, Endpoints


class DataCreateCourier:

    # генерация валидных данных
    @staticmethod
    def generating_fake_valid_data_to_create_courier():
        fake = Faker("ru_RU")
        login = fake.user_name()
        password = fake.password()
        firstname = fake.first_name()
        data = {
            "login": login,
            "firstName": firstname,
            "password": password
        }

        return data

    # генерация данных без поля "login"
    @staticmethod
    def generating_fake_invalid_data_to_create_courier_without_login_field():
        fake = Faker("ru_RU")
        firstname = fake.first_name()
        password = fake.password()
        data = {
            "login": "",
            "firstName": firstname,
            "password": password
        }

        return data

    # генерация данных без поля "password"
    @staticmethod
    def generating_fake_invalid_data_to_create_courier_without_password_field():
        fake = Faker("ru_RU")
        login = fake.user_name()
        firstname = fake.first_name()
        data = {
            "login": login,
            "password": "",
            "firstName": firstname
        }

        return data


class DataCourier:
    # валидные данные для регистрации
    valid_data_login = DataCreateCourier.generating_fake_valid_data_to_create_courier()

    # невалидные данные для регистрации без поля "Login"
    invalid_data_login_without_login = DataCreateCourier.generating_fake_invalid_data_to_create_courier_without_login_field()

    # невалидные данные для регистрации без поля "Password"
    invalid_data_login_without_password = DataCreateCourier.generating_fake_invalid_data_to_create_courier_without_password_field()

    # данные несуществующего курьера
    null_data_login = {
        "login": "testLogin",
        "password": "testPassword"
    }


class Courier:

    # регистрация в системе с возвратом кода ответа и данных курьера
    @staticmethod
    def courier_registration_in_the_system_and_get_courier_data():
        data = DataCreateCourier.generating_fake_valid_data_to_create_courier()
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=data)
        return {"response_text": response.text, "status_code": response.status_code, "data": data}

    # логин в системе с возвратом кода ответа и id курьера
    @staticmethod
    def courier_login_in_the_system_and_get_id_courier(data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=data)
        return {"id": str(response.json()["id"]), "response_text": response.text, "status_code": response.status_code}

    # удаление курьера
    @staticmethod
    def courier_subsequent_deletion(courier_id):
        response = requests.delete(f'{Urls.QA_SCOOTER_URL}{Endpoints.delete_courier}{courier_id}')
        return {"response_text": response.text, "status_code": response.status_code}


class DataOrder:
    # данные для заказа самоката без цвета
    data = {
        "firstName": "Тестер",
        "lastName": "Автотестер",
        "address": "г.Москва",
        "metroStation": 2,
        "phone": "+7 800 555 3535",
        "rentTime": 4,
        "deliveryDate": f"{datetime.date.today()}",
        "comment": "Дай самокат",
    }
