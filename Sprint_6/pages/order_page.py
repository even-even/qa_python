from selenium.webdriver.common.by import By
import allure

from Sprint_6.pages.base_page import BasePage


class OrderPage(BasePage):
    """Форма заказа самоката"""
    # Страница 1
    name_field = (By.XPATH, "//input[@placeholder = '* Имя']")
    last_name_field = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    address_field = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    metro_station_field = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    metro = (By.XPATH, ".//div[text() = 'Парк культуры']")
    telephone_field = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text() = 'Далее']")

    # Страница 2
    deliver_order_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    rent_period_field = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    rent_period_three_days = (By.XPATH, ".//div[text() = 'трое суток']")
    black_color_scooter_check = (By.ID, 'black')
    gray_color_scooter_check = (By.ID, 'grey')
    comment_field = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']")
    back_button = (By.XPATH, ".//button[text() = 'Назад']")
    order_button = (By.XPATH, "(.//button[text() = 'Заказать'])[2]")

    # Окно подтверждения заказа
    no_button = (By.XPATH, ".//button[text() = 'Нет']")
    yes_button = (By.XPATH, ".//button[text() = 'Да']")

    # Окно заказа
    order_placed_text = (By.XPATH, ".//div[text() = 'Заказ оформлен']")
    view_status_button = (By.XPATH, ".//button[text() = 'Посмотреть статус']")

    @allure.step('Заполнение поля Имя')
    def send_name_to_name_field(self, text):
        self.send_keys_to_field(self.name_field, text)

    @allure.step('Заполнение поля Фамилия')
    def send_last_name_to_last_name_field(self, text):
        self.send_keys_to_field(self.last_name_field, text)

    @allure.step('Заполнение поля Адрес')
    def send_address_to_address_field(self, text):
        self.send_keys_to_field(self.address_field, text)

    @allure.step('Заполнение поля Станция метро')
    def send_metro_station_to_metro_station_field(self, text):
        self.click_button(self.metro_station_field)
        self.send_keys_to_field(self.metro_station_field, text)
        self.click_button(self.metro)

    @allure.step('Заполнение поля Номер телефона')
    def send_telephone_number_to_telephone_number_field(self, text):
        self.send_keys_to_field(self.telephone_field, text)

    @allure.step('Клик на кнопку Далее')
    def click_on_the_next_button(self):
        self.click_button(self.next_button)

    @allure.step('''Заполнение данных на странице "Для кого самокат"
                                 и переход на сл.страницу "Про аренду"''')
    def complete_filling_of_the_who_is_scooter_form(self, user):
        self.send_name_to_name_field(user[1])
        self.send_last_name_to_last_name_field(user[2])
        self.send_address_to_address_field(user[3])
        self.send_metro_station_to_metro_station_field(user[4])
        self.send_telephone_number_to_telephone_number_field(user[5])
        self.click_on_the_next_button()

    @allure.step('Заполнение поля Когда привезти заказ')
    def send_deliver_to_deliver_order_field(self, text):
        self.click_button(self.deliver_order_field)
        self.send_keys_to_field(self.deliver_order_field, text)

    @allure.step('Заполнение поля Срок аренды')
    def period_time(self):
        self.click_button(self.rent_period_field)
        self.click_button(self.rent_period_three_days)

    @allure.step('Заполнение поля Цвет самоката')
    def select_color_scooter(self):
        self.click_button(self.black_color_scooter_check)

    @allure.step('Заполнение поля Комментарии для курьера')
    def send_comment_to_comment_field(self, text):
        self.send_keys_to_field(self.comment_field, text)

    @allure.step('Клик на кнопку Заказать')
    def click_order_button(self):
        self.click_button(self.order_button)

    @allure.step('''Заполнение данных на странице "Про аренду"
                 и переход к подтверждению заказа''')
    def complete_filling_of_the_about_rent_form(self, text):
        self.send_deliver_to_deliver_order_field(text[6])
        self.period_time()
        self.select_color_scooter()
        self.send_comment_to_comment_field(text[7])
        self.click_order_button()

    @allure.step('Клик на кнопку Да')
    def confirm_order_scooter(self):
        self.click_button(self.yes_button)

    @allure.step('''Заполнение формы "Для кого самокат", "Про аренду" и подтверждение заказа''')
    def order_scooter_full_path(self, user):
        self.complete_filling_of_the_who_is_scooter_form(user)
        self.complete_filling_of_the_about_rent_form(user)
        self.confirm_order_scooter()

    @allure.step('Проверка отображения окна с текстом подтверждения заказа')
    def check_order_title(self):
        return self.find_and_wait_locator(self.order_placed_text).is_displayed()
