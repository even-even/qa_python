from selenium.webdriver.common.by import By


class MainPage:
    """Главная страница"""
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета
    LOGIN_ACCOUNT_BTN = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка войти в аккаунт
    BUN_BTN = (By.XPATH, ".//span[text() = 'Булки']")  # Кнопка переключения на булки
    SAUCES_BTN = (By.XPATH, ".//span[text() = 'Соусы']")  # Кнопка переключения на соусы
    TOPPINGS_BTN = (By.XPATH, ".//span[text() = 'Начинки']")  # Кнопка переключения на начинки
    PLACE_ORDER_BTN = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка оформить заказ
    SAUCES = (By.XPATH, ".//h2[text() = 'Соусы']")  # Текст соусы на главной странице
    SAUCES_UI = (
        By.XPATH,
        "(.//ul[contains(@class, 'BurgerIngredients_ingredients__list')])[2]")  # Выбор соусов на главной странице
    BUN = (By.XPATH, ".//h2[text() = 'Булки']")  # Текст булки на главной странице
    BUN_UL = (
        By.XPATH,
        "(.//ul[contains(@class, 'BurgerIngredients_ingredients__list')])[1]")  # Выбор булок на главной странице
    TOPPING = (By.XPATH, ".//h2[text() = 'Начинки']")  # Текст начинки на главной странице
    TOPPING_UL = (
        By.XPATH,
        "(.//ul[contains(@class, 'BurgerIngredients_ingredients__list')])[3]")  # Выбор начинок на главной странице


class AuthPage:
    """Форма авторизации"""
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    LOGIN_ACCOUNT_BTN = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка войти


class RegistrationPage:
    """Форма регистрации"""
    NAME_INPUT = (By.XPATH, "(.//input[@name = 'name'])[1]")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "(.//input[@name = 'name'])[2]")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    REGISTRATION_BTN = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка зарегистрироваться
    LOGIN_ACCOUNT_BTN = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка войти
    ERROR_MESSAGE_DOUBLE_REG = (
        By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")  # Ошибка при повторной регистрации
    ERROR_MESSAGE_INCORRECT_PASSWORD = (
        By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Ошибка при вводе некорректного пароля


class RecoverPage:
    """Форма восстановления пароля"""
    LOGIN_ACCOUNT_BTN = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка войти


class PersonalArea:
    """Форма личного кабинета"""
    EXIT_BTN = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка выход
    SAVE_BTN = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка сохранить
    CONSTRUCTOR_BTN = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка конструктор
    LOGO_BTN = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]")  # Кнопка главной страницы сайта
