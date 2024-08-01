import pytest
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_5.data import Timeouts
from Sprint_5.decorators import Step, Check
from Sprint_5.locators import MainPage, PersonalArea, AuthPage
from Sprint_5.urls import URLS


class TestProfileArea:
    @pytest.fixture(scope='function')
    def open_account_page(self, driver, get_login_driver):
        with Step('Перейти в личный кабинет'):
            driver = get_login_driver
            WebDriverWait(driver, Timeouts.large).until(conditions.visibility_of_element_located(
                MainPage.personal_account_btn))
            driver.find_element(*MainPage.personal_account_btn).click()
            WebDriverWait(driver, Timeouts.large).until(conditions.visibility_of_element_located(PersonalArea.exit_btn))

    def test_transition_to_personal_area_from_main_page_success(self, open_account_page, driver):
        """Переход в личный кабинет с главной страницы по кнопке 'Личный кабинет' """
        with Check("Открыт экран личный кабинет"):
            save_btn_displayed = driver.find_element(*PersonalArea.save_btn).is_displayed()
            assert driver.current_url == URLS.PROFILE_PAGE_URL and save_btn_displayed

    def test_transition_from_personal_area_to_constructor_by_click_constructor_btn_success(self, driver,
                                                                                           open_account_page):
        """Переход из личного кабинета в конструктор по клику на кнопку 'Конструктор' """
        with Step('Перейти на экран конструктора'):
            driver.find_element(*PersonalArea.constructor_btn).click()
            WebDriverWait(driver, Timeouts.large).until(conditions.visibility_of_element_located(MainPage.bun))

        with Check("Пользователь на экране Конструктора"):
            bun_displayed = driver.find_element(*MainPage.bun).is_displayed()

            assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed

    def test_transition_from_personal_area_to_constructor_by_click_logo_success(self, driver, open_account_page):
        """Переход из личного кабинета в конструктор по клику на 'Логотип' """
        with Step("Кликнуть по логотипу"):
            driver.find_element(*PersonalArea.logo_btn).click()
            WebDriverWait(driver, Timeouts.large).until(conditions.visibility_of_element_located(MainPage.bun))

        with Check("Пользователь на экране Конструктора"):
            bun_displayed = driver.find_element(*MainPage.bun).is_displayed()
            assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed

    def test_logout_from_personal_area_success(self, driver, open_account_page):
        """Выход из личного кабинета"""
        with Step("Разлогиниться"):
            driver.find_element(*PersonalArea.exit_btn).click()
        WebDriverWait(driver, Timeouts.large).until(conditions.visibility_of_element_located(
            AuthPage.login_account_btn))

        with Check('Пользователь разлогинен'):
            login_btn_displayed = driver.find_element(*AuthPage.login_account_btn).is_displayed()
            assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed
