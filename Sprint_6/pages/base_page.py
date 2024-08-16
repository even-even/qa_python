from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_6.data import Timeouts

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Получение текущего URL
    def get_current_url(self):
        return self.driver.current_url

    # Ожидание отображения локатора
    def find_and_wait_locator(self, locator):
        return WebDriverWait(self.driver, Timeouts.LARGE).until(
            conditions.visibility_of_element_located(locator)
            )

    # Клик по кнопке
    def click_button(self, locator):
        self.find_and_wait_locator(locator).click()

    # Заполнение формы
    def send_keys_to_field(self, locator, text):
        self.find_and_wait_locator(locator).send_keys(text)

    # Получение текста элемента
    def get_text_locator(self, locator):
        return self.find_and_wait_locator(locator).text

    # Скролл к нужному элементу
    def scroll_to_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Переход на новую вкладку браузера
    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_element(self, locator):
        return self.find_and_wait_locator(locator).is_displayed()
