from selenium import webdriver
import pytest
from Sprint_5.locators import MainPage, AuthPage
from Sprint_5.urls import URLS
from Sprint_5.data import Person


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def get_login_driver(driver):
    driver.get(URLS.MAIN_PAGE_URL)
    driver.find_element(*MainPage.personal_account_btn).click()
    driver.find_element(*AuthPage.email_input).send_keys(Person.email)
    driver.find_element(*AuthPage.password_input).send_keys(Person.password)
    driver.find_element(*AuthPage.login_account_btn).click()

    return driver
