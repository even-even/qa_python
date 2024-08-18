from selenium.webdriver.common.by import By
import allure

from Sprint_6.pages.base_page import BasePage


class HomePageHeader(BasePage):
    """Хедер"""
    logo_yandex = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")
    logo_scooter = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    order_button = (By.XPATH, "(.//button[text() = 'Заказать'])[1]")
    order_status_button = (By.XPATH, ".//button[text() = 'Статус заказа']")
    header_page_title = (By.XPATH, ".//div[text() = 'Учебный тренажер']")

    @allure.step('Клик по логотипу Яндекса')
    def yandex_logo_click(self):
        self.click_button(self.logo_yandex)

    @allure.step('Клик по логотипу Самоката')
    def scooter_logo_click(self):
        self.click_button(self.logo_scooter)

    @allure.step('Клик по кнопке Заказать')
    def order_button_click(self):
        self.click_button(self.order_button)

    @allure.step('Клик по кнопке Статус заказа')
    def status_order_click(self):
        self.click_button(self.order_status_button)

    @allure.step('Проверка отображения надписи - "Учебный проект"')
    def check_order_title(self):
        return self.find_and_wait_locator(self.header_page_title).is_displayed()


class HomePage(BasePage):
    """Главная страница сервиса"""
    order_button = (By.XPATH, "(//button[text() = 'Заказать'])[2]")
    accept_cookies_button = (By.XPATH, "//button[@id = 'rcc-confirm-button']")
    questions_title = (By.XPATH, "//div[text() = 'Вопросы о важном']")

    # Локаторы кнопок вопросов
    questions = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]

    # Локаторы текста ответов
    questions_text = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]

    @allure.step('Скролл и клик на кнопку Заказать')
    def scroll_and_click_on_the_order_button(self):
        self.scroll_to_locator(self.order_button)
        self.click_button(self.order_button)

    @allure.step('Переход к списку вопросов')
    def scroll_to_questions(self):
        self.scroll_to_locator(self.questions_title)

    @allure.step('Клик на вопрос')
    def click_question_button(self, question_button_locator):
        self.scroll_to_questions()
        self.click_button(question_button_locator)

    @allure.step('Получение текста вопроса')
    def get_text_question(self, question_button_locator, question_text_locator):
        self.click_question_button(question_button_locator)
        text_question = self.get_text_locator(question_text_locator)
        return text_question
