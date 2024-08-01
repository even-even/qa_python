from Sprint_5.data import Person, Timeouts
from Sprint_5.locators import MainPage, AuthPage, RegistrationPage, RecoverPage
from Sprint_5.urls import URLS
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.decorators import Given, Step, Check


class TestLogin:

    def test_login_in_login_btn_success(self, driver):
        """Вход в личный кабинет через кнопку 'Войти в аккаунт' на главной странице"""
        with Given("Пользователь на Главной"):
            driver.get(URLS.MAIN_PAGE_URL)

        with Step("Залогиниться"):
            driver.find_element(*MainPage.login_account_btn).click()
            driver.find_element(*AuthPage.email_input).send_keys(Person.email)
            driver.find_element(*AuthPage.password_input).send_keys(Person.password)
            driver.find_element(*AuthPage.login_account_btn).click()
        WebDriverWait(driver, Timeouts.large).until(conditions.visibility_of_element_located(
            MainPage.place_order_button))

        with Check("Пользователь залогинен"):
            order_btn = driver.find_element(*MainPage.place_order_button).text
            assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')

    def test_login_in_personal_account_btn_success(self, driver):
        """Вход в личный кабинет через кнопку 'Личный кабинет' на главной странице"""
        with Given("Пользователь на Главной"):
            driver.get(URLS.MAIN_PAGE_URL)

        with Step("Залогиниться через личный кабинет"):
            driver.find_element(*MainPage.personal_account_btn).click()
            driver.find_element(*AuthPage.email_input).send_keys(Person.email)
            driver.find_element(*AuthPage.password_input).send_keys(Person.password)
            driver.find_element(*AuthPage.login_account_btn).click()
            WebDriverWait(driver, Timeouts.large).until(conditions.visibility_of_element_located(
                MainPage.place_order_button))

        with Check("Пользователь залогинен"):
            order_btn = driver.find_element(*MainPage.place_order_button).text
            assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')

    def test_login_in_registration_form_success(self, driver):
        """Вход в личный кабинет через форму регистрации"""
        with Given("Пользователь на странице регистрации"):
            driver.get(URLS.REG_PAGE_URL)

        with Step("Залогиниться"):
            driver.find_element(*RegistrationPage.login_account_btn).click()
            driver.find_element(*AuthPage.email_input).send_keys(Person.email)
            driver.find_element(*AuthPage.password_input).send_keys(Person.password)
            driver.find_element(*AuthPage.login_account_btn).click()
            WebDriverWait(driver, Timeouts.large).until(conditions.visibility_of_element_located(
                MainPage.place_order_button))

        with Check("Пользователь залогинен"):
            order_btn = driver.find_element(*MainPage.place_order_button).text
            assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')

    def test_login_in_recover_form_success(self, driver):
        """Вход в личный кабинет через форму восстановления"""
        with Given("Пользователь на экране восстановление пароля"):
            driver.get(URLS.RECOVER_PAGE_URL)

        with Step("Залогиниться"):
            driver.find_element(*RecoverPage.login_account_btn).click()
            driver.find_element(*AuthPage.email_input).send_keys(Person.email)
            driver.find_element(*AuthPage.password_input).send_keys(Person.password)
            driver.find_element(*AuthPage.login_account_btn).click()
            WebDriverWait(driver, Timeouts.large).until(conditions.visibility_of_element_located(
                MainPage.place_order_button))

        with Check("Пользователь залогинен"):
            order_btn = driver.find_element(*MainPage.place_order_button).text
            assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')
