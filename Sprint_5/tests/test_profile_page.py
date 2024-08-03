from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_5.data import Timeouts
from Sprint_5.decorators import Step, Check
from Sprint_5.locators import MainPage, PersonalArea, AuthPage
from Sprint_5.urls import URLS


class TestProfileArea:

    def test_transition_to_personal_area_from_main_page_success(self, driver, open_account_page):
        """Переход в личный кабинет с главной страницы по кнопке 'Личный кабинет' """
        with Check("Открыт экран личный кабинет"):
            save_btn_displayed = driver.find_element(*PersonalArea.SAVE_BTN).is_displayed()
            assert driver.current_url == URLS.PROFILE_PAGE_URL and save_btn_displayed

    def test_transition_from_personal_area_to_constructor_by_click_constructor_btn_success(self, driver,
                                                                                           open_account_page):
        """Переход из личного кабинета в конструктор по клику на кнопку 'Конструктор' """
        with Step('Перейти на экран конструктора'):
            driver.find_element(*PersonalArea.CONSTRUCTOR_BTN).click()
            WebDriverWait(driver, Timeouts.LARGE).until(conditions.visibility_of_element_located(MainPage.BUN))

        with Check("Пользователь на экране Конструктора"):
            bun_displayed = driver.find_element(*MainPage.BUN).is_displayed()
            assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed

    def test_transition_from_personal_area_to_constructor_by_click_logo_success(self, driver, open_account_page):
        """Переход из личного кабинета в конструктор по клику на 'Логотип' """
        with Step("Кликнуть по логотипу"):
            driver.find_element(*PersonalArea.LOGO_BTN).click()
            WebDriverWait(driver, Timeouts.LARGE).until(conditions.visibility_of_element_located(MainPage.BUN))

        with Check("Пользователь на экране Конструктора"):
            bun_displayed = driver.find_element(*MainPage.BUN).is_displayed()
            assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed

    def test_logout_from_personal_area_success(self, driver, open_account_page):
        """Выход из личного кабинета"""
        with Step("Разлогиниться"):
            driver.find_element(*PersonalArea.EXIT_BTN).click()
        WebDriverWait(driver, Timeouts.LARGE).until(conditions.visibility_of_element_located(
            AuthPage.LOGIN_ACCOUNT_BTN))

        with Check('Пользователь разлогинен'):
            login_btn_displayed = driver.find_element(*AuthPage.LOGIN_ACCOUNT_BTN).is_displayed()
            assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed
