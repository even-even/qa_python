import allure
import pytest
import requests

from Sprint_7.decorators import Step, Check
from Sprint_7.helpers import DataCourier
from Sprint_7.urls import Urls, Endpoints


class TestCreateCourier:

    @allure.title('Создание нового курьера')
    def test_registration_courier_success(self, courier):

        with Step("Отправить запрос на создание курьера"):
            courier_data = courier

        with Check(f'Курьер создан'):
            assert courier_data["status_code"] == 201
            assert courier_data["response_text"] == '{"ok":true}'

    @allure.title('Ошибка при создании двух одинаковых курьеров')
    def test_registration_double_courier_failed(self, courier):

        with Step("Отправить повторный запрос на создание курьера"):
            response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=courier["data"])

        with Check("Курьер на создался"):
            assert response.status_code == 409
            assert "Этот логин уже используется" in response.text

    @allure.title('Ошибка при создании курьера без заполнения обязательных полей login/password')
    @pytest.mark.parametrize('courier_data', (DataCourier.invalid_data_login_without_login,
                                           DataCourier.invalid_data_login_without_password))
    def test_courier_registration_without_parameters_failed(self, courier_data):

        with Step("Отправить запрос на создание курьера без заполненных login/password"):
            response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=courier_data)

        with Check("Курьер не создался"):
            assert response.status_code == 400
            assert "Недостаточно данных для создания учетной записи" in response.text
