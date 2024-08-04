from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_5.data import Person, RandomPerson, Timeouts, Strings
from Sprint_5.decorators import Step, Check
from Sprint_5.locators import RegistrationPage, AuthPage
from Sprint_5.urls import URLS


class TestRegistrationPage:

    def test_registration_success(self, driver, open_registration_page):
        """Регистрация пользователя"""
        with Step(f"Вести данные пользователя {RandomPerson.USER_NAME}"):
            driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(RandomPerson.USER_NAME)
            driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(RandomPerson.email)
            driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(RandomPerson.password)

        with Step("Нажать на кнопку регистрации"):
            driver.find_element(*RegistrationPage.REGISTRATION_BTN).click()
            WebDriverWait(driver, Timeouts.MEDIUM).until(conditions.visibility_of_element_located(
                AuthPage.LOGIN_ACCOUNT_BTN))
            login_btn_displayed = driver.find_element(*AuthPage.LOGIN_ACCOUNT_BTN).is_displayed()

        with Check("Пользователь зарегистрирован"):
            assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed

    def test_double_registration_check_error(self, driver, open_registration_page):
        """Повторная регистрация пользователя"""
        with Step(f"Вести данные пользователя {Person.USER_NAME}"):
            driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(Person.USER_NAME)
            driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(Person.EMAIL)
            driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(Person.PASSWORD)

        with Step("Нажать на кнопку регистрации"):
            driver.find_element(*RegistrationPage.REGISTRATION_BTN).click()
            WebDriverWait(driver, Timeouts.MEDIUM).until(
                conditions.visibility_of_element_located(RegistrationPage.ERROR_MESSAGE_DOUBLE_REG))

        with Check("Отображается ошибка регистрации"):
            error = driver.find_element(*RegistrationPage.ERROR_MESSAGE_DOUBLE_REG).text
            assert (error == Strings.USER_ALREADY_EXISTS) and (driver.current_url == URLS.REG_PAGE_URL)

    def test_registration_incorrect_password_check_error(self, driver, open_registration_page):
        """Регистрация пользователя с некорректным паролем (менее 6 символов)"""
        with Step(f"Вести данные пользователя {Person.USER_NAME}"):
            driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(Person.USER_NAME)
            driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(Person.EMAIL)
            driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(12345)

        with Step("Нажать на кнопку регистрации"):
            driver.find_element(*RegistrationPage.REGISTRATION_BTN).click()
            WebDriverWait(driver, Timeouts.MEDIUM).until(
                conditions.visibility_of_any_elements_located(RegistrationPage.ERROR_MESSAGE_INCORRECT_PASSWORD))

        with Check("Отображается ошибка регистрации"):
            error = driver.find_element(*RegistrationPage.ERROR_MESSAGE_INCORRECT_PASSWORD).text
            assert (error == Strings.INCORRECT_PASSWORD) and (driver.current_url == URLS.REG_PAGE_URL)
