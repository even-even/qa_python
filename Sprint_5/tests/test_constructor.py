from Sprint_5.data import Strings
from Sprint_5.decorators import Step, Check
from Sprint_5.locators import MainPage


class TestConstructorPage:

    def test_transition_to_bun_success(self, driver, open_main_page):
        """Переход к разделу 'Булки' """
        with Step(f"Перейти на фильтр {Strings.SAUCES}"):
            driver.find_element(*MainPage.SAUCES_BTN).click()

        with Step(f'Вернуться на фильтр {Strings.BUNS}'):
            driver.find_element(*MainPage.BUN_BTN).click()

        with Check(f'Активен раздел {Strings.BUNS}'):
            bun_text = driver.find_element(*MainPage.BUN).text
            bun_displayed = driver.find_element(*MainPage.BUN_UL).is_displayed()
            assert bun_text == Strings.BUNS and bun_displayed

    def test_transition_to_sauces_success(self, driver, open_main_page):
        """Переход к разделу 'Соусы' """
        with Step(f"Перейти на фильтр {Strings.SAUCES}"):
            driver.find_element(*MainPage.SAUCES_BTN).click()

        with Check(f'Активен раздел {Strings.SAUCES}'):
            sauces = driver.find_element(*MainPage.SAUCES).text
            sauces_displayed = driver.find_element(*MainPage.SAUCES_UI).is_displayed()
            assert sauces == Strings.SAUCES and sauces_displayed

    def test_transition_to_topping_success(self, driver, open_main_page):
        """Переход к разделу 'Начинки' """
        with Step(f"Перейти на фильтр {Strings.FILINGS}"):
            driver.find_element(*MainPage.TOPPINGS_BTN).click()

        with Check(f'Активен раздел {Strings.FILINGS}'):
            topping = driver.find_element(*MainPage.TOPPING).text
            topping_displayed = driver.find_element(*MainPage.TOPPING_UL).is_displayed()
            assert topping == Strings.FILINGS and topping_displayed
