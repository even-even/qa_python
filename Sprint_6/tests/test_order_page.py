import allure

from Sprint_6.data import Users
from Sprint_6.pages.home_page import HomePage, HomePageHeader
from Sprint_6.pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Оформление заказа по клику на кнопку "Заказать" в хедере')
    @allure.description('''1)На главной странице в хедере кликнуть на кнопку "Заказать";
                        2)Заполнить данные на странице "Для кого самокат' и кликнуть на кнопку "Далее";
                        3)Заполнить данные "Про аренду" и кликнуть на кнопку "Заказать";
                        4)Подтвердить заказ и проверить открытие окна с текстом оформления заказа''')
    def test_order_scooter_by_order_button_from_header(self, driver):
        header_page = HomePageHeader(driver)
        order_page = OrderPage(driver)
        header_page.order_button_click()
        order_page.order_scooter_full_path(Users.user)

        assert order_page.check_order_title()

    @allure.title('Оформление заказа по клику на кнопку "Заказать" на главной странице')
    @allure.description('''1)На главной странице проскролить до кнопки "Заказать" и кликаем на нее;
                        2)Заполнить данные на странице "Для кого самокат', кликнуть на кнопку "Далее";
                        3)Заполнить данные "Про аренду" и кликнуть на кнопку "Заказать";
                        4)Подтвердить заказ - проверить открытие окна с текстом оформления заказа''')
    def test_order_scooter_by_order_button_from_home_page(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.scroll_and_click_on_the_order_button()
        order_page.order_scooter_full_path(Users.user_2)

        assert order_page.check_order_title()
