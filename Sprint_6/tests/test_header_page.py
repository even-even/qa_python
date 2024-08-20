import time

import allure
import pytest

from Sprint_6.data import Questions, Urls, Timeouts
from Sprint_6.pages.dzen_page import DzenPage
from Sprint_6.pages.home_page import HomePage, HomePageHeader


class TestMainPage:

    @allure.title('Переход на главную страницу веб-приложения по клику на логотип "Самокат"')
    @allure.description('''1)Кликнуть на кнопку "Заказать"
                        2)Кликнуть на логотип "Самокат"
                        3)Сравнить текущий URL с ожидаемым и отображение надписи - "Учебный проект"''')
    def test_scooter_logo_click(self, driver):
        header_page = HomePageHeader(driver)
        header_page.order_button_click()
        header_page.scooter_logo_click()
        current_url = header_page.get_current_url()
        title_is_displayed = header_page.check_order_title()

        assert current_url == Urls.QA_SCOOTER_URL and title_is_displayed

    @allure.title('Переход на главную страницу DZEN по клику на логотип "Яндекс"')
    @allure.description('''1)Кликнуть на логотип "Яндекс"
                        2)Переключиться на новую вкладку и дождаться загрузку страницы
                        3)Сравнить текущий URL с ожидаемым''')
    def test_yandex_logo_click(self, driver):
        header_page = HomePageHeader(driver)
        dzen_page = DzenPage(driver)
        header_page.yandex_logo_click()
        header_page.go_to_new_tab()
        time.sleep(Timeouts.MEDIUM)
        current_url = header_page.get_current_url()

        assert current_url == Urls.DZEN_URL and dzen_page.check_element_main_button()

    @allure.title('Текста ответов на вопросы на главной странице веб-приложения')
    @allure.description('''1)Проскролить до блока с вопросами;
                        2)Кликнуть на вопрос;
                        3)Получить текст ответа на выбранный вопрос;
                        4)Сравнить полученный текст с ожидаемым''')
    @pytest.mark.parametrize('question_locator, question_text_locator, expected_question_text',
                             zip(HomePage.questions, HomePage.questions_text, Questions.expected_question_text))
    def test_accordion(self, driver, question_locator, question_text_locator, expected_question_text):
        home_page = HomePage(driver)
        text = home_page.get_text_question(question_locator, question_text_locator)

        assert text == expected_question_text