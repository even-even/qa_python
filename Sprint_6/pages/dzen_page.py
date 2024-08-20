import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_6.data import Timeouts
from Sprint_6.pages.base_page import BasePage


class DzenPage(BasePage):

    main_button_dzen = (By.XPATH, ".//span[text() = 'Главная']")

    @allure.step('Кнопка "Главная" отображается на странице DZEN')
    def check_element_main_button(self):
        return WebDriverWait(self.driver, Timeouts.MEDIUM).until(
            conditions.presence_of_element_located(self.main_button_dzen))
