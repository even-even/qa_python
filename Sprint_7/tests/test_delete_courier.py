import allure

from Sprint_5.decorators import Given
from Sprint_7.decorators import Step, Check
from Sprint_7.helpers import Courier
from Sprint_7.data import ResponseText


class TestDeleteCourier:

    @allure.title('Удаление курьера')
    def test_delete_courier_success(self):
        with Given("Создан курьер"):
            courier_create = Courier().courier_registration_in_the_system_and_get_courier_data()
            courier_login = Courier().courier_login_in_the_system_and_get_id_courier(courier_create["data"])

        with Step("Отправить запрос на удаление курьера"):
            courier_id = courier_login
            response = Courier().courier_subsequent_deletion(courier_id["id"])

        with Check("Курьер удалился"):
            assert response["status_code"] == 200
            assert response["response_text"] == ResponseText.OK_TRUE

    @allure.title('Удаление курьера с несуществующим ID')
    def test_delete_courier_invalid_id_failed(self):
        courier_id = '123456'

        with Step("Отправить запрос на удаление курьера с несуществующим ID"):
            response = Courier().courier_subsequent_deletion(courier_id)

        with Check("Курьер не удалился"):
            assert response["status_code"] == 404
            assert ResponseText.COURIER_NOT_FOUND in response["response_text"]

    @allure.title('Удаление курьера без ID')
    def test_delete_courier_none_id_failed(self):
        courier_id = None

        with Step("Оправить запрос на удаление курьера без ID"):
            response = Courier().courier_subsequent_deletion(courier_id)

        with Check("Курьер не удалился"):
            assert response["status_code"] == 500
            assert ResponseText.INVALID_SYNTAX in response["response_text"]
