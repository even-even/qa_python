import datetime

from Sprint_7.helpers import DataCreateCourier


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
