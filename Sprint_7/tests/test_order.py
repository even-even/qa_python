import json

import allure
import pytest
import requests

from Sprint_7.data import DataOrder, ResponseText
from Sprint_7.urls import Urls, Endpoints
from Sprint_7.decorators import Step, Check


class TestOrder:

    @allure.title('Оформление заказа с разным набором цветов')
    @pytest.mark.parametrize('color', ({"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": ["BLACK", "GRAY"]}, {"color": [""]}, {"color": [123]}))
    def test_create_order_success(self, color):

        with Step("Отправить запрос на создание заказа с поочередным добавлением разных цветов"):
            headers = {"Content-type": "application/json"}
            data = DataOrder.data
            data.update(color)
            data = json.dumps(data)
            response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_order}', headers=headers, data=data)

        with Check("Заказ создан"):
            assert response.status_code == 201
            assert ResponseText.TRACK in response.text

    @allure.title('Получение списка заказов')
    def test_list_orders_success(self):

        with Step("Получить список заказов"):
            response = requests.get(f'{Urls.QA_SCOOTER_URL}{Endpoints.get_orders_list}')

        with Check("Список получен"):
            assert response.status_code == 200
            assert ResponseText.TRACK in response.text
            assert len(response.content) > 0
