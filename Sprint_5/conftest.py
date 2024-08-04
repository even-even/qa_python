import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_5.data import Person, Timeouts
from Sprint_5.decorators import Given, Step
from Sprint_5.locators import MainPage, AuthPage, PersonalArea, RegistrationPage
from Sprint_5.urls import URLS


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def get_login_driver(driver):
    driver.get(URLS.MAIN_PAGE_URL)
    driver.find_element(*MainPage.PERSONAL_ACCOUNT_BTN).click()
    driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(Person.EMAIL)
    driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(Person.PASSWORD)
    driver.find_element(*AuthPage.LOGIN_ACCOUNT_BTN).click()

    return driver


@pytest.fixture(scope='function')
def open_main_page(driver):
    with Given('Пользователь на Главной'):
        return driver.get(URLS.MAIN_PAGE_URL)


@pytest.fixture(scope='function')
def open_account_page(driver, get_login_driver):
    with Step('Перейти в личный кабинет'):
        driver = get_login_driver
        WebDriverWait(driver, Timeouts.LARGE).until(conditions.visibility_of_element_located(
            MainPage.PERSONAL_ACCOUNT_BTN))
        driver.find_element(*MainPage.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, Timeouts.LARGE).until(conditions.visibility_of_element_located(PersonalArea.EXIT_BTN))


@pytest.fixture(scope='function')
def open_registration_page(driver):
    with Given('Осуществлен переход на экран регистрации пользователя'):
        driver = driver
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, Timeouts.MEDIUM).until(
            conditions.visibility_of_element_located(RegistrationPage.REGISTRATION_BTN))
