import pytest
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_5.data import Person, RandomPerson, Timeouts
from Sprint_5.decorators import Given, Step, Check
from Sprint_5.locators import RegistrationPage, AuthPage
from Sprint_5.urls import URLS


class TestRegistrationPage:

    @pytest.fixture(scope='function')
    def open_page(self, driver):
        with Given('Осуществлен переход на экран регистрации пользователя'):
            driver = driver
            driver.get(URLS.REG_PAGE_URL)
            WebDriverWait(driver, Timeouts.medium).until(
                conditions.visibility_of_element_located(RegistrationPage.registration_btn))

    def test_registration_success(self, driver, open_page):
        """Регистрация пользователя"""
        with Step(f"Вести данные пользователя {RandomPerson.user_name}"):
            driver.find_element(*RegistrationPage.name_input).send_keys(RandomPerson.user_name)
            driver.find_element(*RegistrationPage.email_input).send_keys(RandomPerson.email)
            driver.find_element(*RegistrationPage.password_input).send_keys(RandomPerson.password)

        with Step("Нажать на кнопку регистрации"):
            driver.find_element(*RegistrationPage.registration_btn).click()
            WebDriverWait(driver, Timeouts.medium).until(conditions.visibility_of_element_located(
                AuthPage.login_account_btn))
            login_btn_displayed = driver.find_element(*AuthPage.login_account_btn).is_displayed()

        with Check("Пользователь зарегистрирован"):
            assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed

    def test_double_registration_check_error(self, driver, open_page):
        """Повторная регистрация пользователя"""
        with Step(f"Вести данные пользователя {Person.user_name}"):
            driver.find_element(*RegistrationPage.name_input).send_keys(Person.user_name)
            driver.find_element(*RegistrationPage.email_input).send_keys(Person.email)
            driver.find_element(*RegistrationPage.password_input).send_keys(Person.password)

        with Step("Нажать на кнопку регистрации"):
            driver.find_element(*RegistrationPage.registration_btn).click()
            WebDriverWait(driver, Timeouts.medium).until(
                conditions.visibility_of_element_located(RegistrationPage.error_message_double_reg))

        with Check("Отображается ошибка регистрации"):
            error = driver.find_element(*RegistrationPage.error_message_double_reg).text
            assert (error == 'Такой пользователь уже существует') and (driver.current_url == URLS.REG_PAGE_URL)

    def test_registration_incorrect_password_check_error(self, driver, open_page):
        """Регистрация пользователя с некорректным паролем (менее 6 символов)"""
        with Step(f"Вести данные пользователя {Person.user_name}"):
            driver.find_element(*RegistrationPage.name_input).send_keys(Person.user_name)
            driver.find_element(*RegistrationPage.email_input).send_keys(Person.email)
            driver.find_element(*RegistrationPage.password_input).send_keys(12345)

        with Step("Нажать на кнопку регистрации"):
            driver.find_element(*RegistrationPage.registration_btn).click()
            WebDriverWait(driver, Timeouts.medium).until(
                conditions.visibility_of_any_elements_located(RegistrationPage.error_message_incorrect_password))

        with Check("Отображается ошибка регистрации"):
            error = driver.find_element(*RegistrationPage.error_message_incorrect_password).text
            assert (error == 'Некорректный пароль') and (driver.current_url == URLS.REG_PAGE_URL)
