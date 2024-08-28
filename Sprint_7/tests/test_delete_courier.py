import allure

from Sprint_7.decorators import Step, Check
from Sprint_7.helpers import Courier


class TestDeleteCourier:

    @allure.title('Удаление курьера')
    def test_delete_courier_success(self, courier_delete):

        with Step("Отправить запрос на удаление курьера"):
            courier_id = courier_delete
            response = Courier().courier_subsequent_deletion(courier_id["id"])

        with Check("Курьер удалился"):
            assert response["status_code"] == 200
            assert response["response_text"] == '{"ok":true}'


    @allure.title('Удаление курьера с несуществующим ID')
    def test_delete_courier_invalid_id_failed(self):
        courier_id = '123456'

        with Step("Отправить запрос на удаление курьера с несуществующим ID"):
            response = Courier().courier_subsequent_deletion(courier_id)

        with Check("Курьер не удалился"):
            assert response["status_code"] == 404
            assert "Курьера с таким id нет" in response["response_text"]

    @allure.title('Удаление курьера без ID')
    def test_delete_courier_none_id_failed(self):
        courier_id = None

        with Step("Оправить запрос на удаление курьера без ID"):
            response = Courier().courier_subsequent_deletion(courier_id)

        with Check("Курьер не удалился"):
            assert response["status_code"] == 500
            assert "invalid input syntax" in response["response_text"]
