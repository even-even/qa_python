from Sprint_5.data import Person, Timeouts, Strings
from Sprint_5.locators import MainPage, AuthPage, RegistrationPage, RecoverPage
from Sprint_5.urls import URLS
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.decorators import Given, Step, Check


class TestLogin:

    def test_login_in_login_btn_success(self, driver, open_main_page):
        """Вход в личный кабинет через кнопку 'Войти в аккаунт' на главной странице"""

        with Step("Залогиниться"):
            driver.find_element(*MainPage.LOGIN_ACCOUNT_BTN).click()
            driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(Person.EMAIL)
            driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(Person.PASSWORD)
            driver.find_element(*AuthPage.LOGIN_ACCOUNT_BTN).click()
        WebDriverWait(driver, Timeouts.LARGE).until(conditions.visibility_of_element_located(
            MainPage.PLACE_ORDER_BTN))

        with Check("Пользователь залогинен"):
            order_btn = driver.find_element(*MainPage.PLACE_ORDER_BTN).text
            assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == Strings.CREATE_ORDER)

    def test_login_in_personal_account_btn_success(self, driver, open_main_page):
        """Вход в личный кабинет через кнопку 'Личный кабинет' на главной странице"""

        with Step("Залогиниться через личный кабинет"):
            driver.find_element(*MainPage.PERSONAL_ACCOUNT_BTN).click()
            driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(Person.EMAIL)
            driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(Person.PASSWORD)
            driver.find_element(*AuthPage.LOGIN_ACCOUNT_BTN).click()
            WebDriverWait(driver, Timeouts.LARGE).until(conditions.visibility_of_element_located(
                MainPage.PLACE_ORDER_BTN))

        with Check("Пользователь залогинен"):
            order_btn = driver.find_element(*MainPage.PLACE_ORDER_BTN).text
            assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == Strings.CREATE_ORDER)

    def test_login_in_registration_form_success(self, driver):
        """Вход в личный кабинет через форму регистрации"""
        with Given("Пользователь на странице регистрации"):
            driver.get(URLS.REG_PAGE_URL)

        with Step("Залогиниться"):
            driver.find_element(*RegistrationPage.LOGIN_ACCOUNT_BTN).click()
            driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(Person.EMAIL)
            driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(Person.PASSWORD)
            driver.find_element(*AuthPage.LOGIN_ACCOUNT_BTN).click()
            WebDriverWait(driver, Timeouts.LARGE).until(conditions.visibility_of_element_located(
                MainPage.PLACE_ORDER_BTN))

        with Check("Пользователь залогинен"):
            order_btn = driver.find_element(*MainPage.PLACE_ORDER_BTN).text
            assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == Strings.CREATE_ORDER)

    def test_login_in_recover_form_success(self, driver):
        """Вход в личный кабинет через форму восстановления"""
        with Given("Пользователь на экране восстановление пароля"):
            driver.get(URLS.RECOVER_PAGE_URL)

        with Step("Залогиниться"):
            driver.find_element(*RecoverPage.LOGIN_ACCOUNT_BTN).click()
            driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(Person.EMAIL)
            driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(Person.PASSWORD)
            driver.find_element(*AuthPage.LOGIN_ACCOUNT_BTN).click()
            WebDriverWait(driver, Timeouts.LARGE).until(conditions.visibility_of_element_located(
                MainPage.PLACE_ORDER_BTN))

        with Check("Пользователь залогинен"):
            order_btn = driver.find_element(*MainPage.PLACE_ORDER_BTN).text
            assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == Strings.CREATE_ORDER)
