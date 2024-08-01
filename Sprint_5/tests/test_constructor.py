import pytest

from Sprint_5.decorators import Given, Step, Check
from Sprint_5.locators import MainPage
from Sprint_5.urls import URLS


class TestConstructorPage:

    @pytest.fixture(scope='function')
    def open_main_page(self, driver):
        with Given('Пользователь на Главной'):
            return driver.get(URLS.MAIN_PAGE_URL)

    def test_transition_to_bun_success(self, driver, open_main_page):
        """Переход к разделу 'Булки' """
        with Step("Перейти на фильтр 'Соусы'"):
            driver.find_element(*MainPage.sauces_btn).click()
        with Step('Вернуться на фильтр "Булки"'):
            driver.find_element(*MainPage.bun_btn).click()

        with Check('Активен раздел "Булки"'):
            bun_text = driver.find_element(*MainPage.bun).text
            bun_displayed = driver.find_element(*MainPage.bun_ul).is_displayed()
            assert bun_text == 'Булки' and bun_displayed

    def test_transition_to_sauces_success(self, driver, open_main_page):
        """Переход к разделу 'Соусы' """
        with Step("Перейти на фильтр 'Соусы'"):
            driver.find_element(*MainPage.sauces_btn).click()

        with Check('Активен раздел "Соусы"'):
            souces = driver.find_element(*MainPage.sauces).text
            souces_displayed = driver.find_element(*MainPage.sauces_ul).is_displayed()
            assert souces == 'Соусы' and souces_displayed

    def test_transition_to_topping_success(self, driver, open_main_page):
        """Переход к разделу 'Начинки' """
        with Step("Перейти на фильтр 'Начинки'"):

            driver.find_element(*MainPage.toppings_btn).click()

        with Check('Активен раздел "Начинки"'):
            topping = driver.find_element(*MainPage.topping).text
            topping_displayed = driver.find_element(*MainPage.topping_ul).is_displayed()
            assert topping == 'Начинки' and topping_displayed
