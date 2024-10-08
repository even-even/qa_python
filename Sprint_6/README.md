# Проект 6 спринта курса "Автоматизатор тестирования на Python" от Яндекс Практикум на тему "Page Object"

Автотесты для сервиса «Яндекс.Самокат».


## Файлы:
- allure_results - каталог с отчетом о тестировании
- tests/ - каталог с автотестами
- tests/test_home_page.py - тесты домашней страницы 
- tests/test_order_page.py - тесты оформления заказа
- conftest.py - фикстуры
- data.py - вспомогательные данные для тестирования
- pages/ - каталог с локаторами и методами page's
- pages/base_page.py - базовые методы взаимодействия с элементами
- pages/dzen_page.py - локаторы и методы для взаимодействия со страницей дзена
- pages/home_page.py - локаторы и методы для взаимодействия с домашней страницей
- pages/order_page.py - локаторы и методы для взаимодействия со страницами оформления заказа
- requirements.txt - зависимости

Перед работой с репозиторием требуется установить зависимости 
```shell
pip install -r requirements.txt
```
Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
Посмотреть отчет в веб версии пройденного прогона
```shell
allure serve allure_results
```