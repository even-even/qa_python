# Проект 5 спринта курса "Автоматизатор тестирования на Python" от Яндекс Практикум на тему "UI-тестирование"

Автотесты для сервиса Stellar Burgers.

## Файлы:
- tests/ - каталог с автотестами
- tests/test_constructor.py - тесты раздела конструктор
- tests/test_login.py - тесты авторизации
- tests/test_profile_page.py - тесты личного кабинета
- tests/test_registration_page.py - тесты регистрации
- conftest.py - фикстуры
- data.py - данные для тестов
- locators.py - Локаторы элементов
- urls.py - файл с урлами страниц
- decorators.py - декораторы для человекочитаемых шагов тестов
- requirements.txt - зависимости

### Для запуска тестов должны быть установлены:
`pytest`
`selenium`
`allure-pytest`

### Команда для запуска тестов:
`pytest -v`