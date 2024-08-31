import allure
import pytest
import requests

from Sprint_7.decorators import Step, Check
from Sprint_7.helpers import Courier
from Sprint_7.data import DataCourier, ResponseText
from Sprint_7.urls import Urls, Endpoints


class TestLoginCourier:

    @allure.title('Авторизация курьера с валидными данными')
    def test_courier_login_success(self, courier):

        with Step("Отправить запрос авторизации курьера"):
            courier_data = courier
            response = Courier().courier_login_in_the_system_and_get_id_courier(courier_data["data"])

        with Check("Курьер успешно авторизовался"):
            assert response["status_code"] == 200
            assert response.get("id")

    @allure.title('Ошибка при авторизации курьера без заполнения обязательных полей Login/Password')
    @pytest.mark.parametrize('courier_data', [DataCourier.invalid_data_login_without_login,
                                           DataCourier.invalid_data_login_without_password])
    def test_courier_login_without_parameters_failed(self, courier_data):

        with Step("Отправить запрос на авторизацию курьера без заполненных login/password"):
            response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=courier_data)

        with Check("Авторизация не прошла"):
            assert response.status_code == 400
            assert ResponseText.NOT_ENOUGT_DATA_LOG_IN in response.text

    @allure.title('Ошибка при авторизации курьера с несуществующими данными')
    def test_courier_login_without_null_login_failed(self):

        with Step("Отправить запрос на авторизацию с несуществующими данными"):
            response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=DataCourier.null_data_login)

        with Check("Авторизация не прошла"):
            assert response.status_code == 404
            assert ResponseText.ACCOUNT_NOT_FOUND in response.text
