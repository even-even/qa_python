# Финальный проект 7 спринта курса "Автоматизатор тестирования на Python" от Яндекс Практикум на тему "Тестирование API"

Автотесты для сервиса "Яндекс Самокат". 
Документация: `qa-scooter.praktikum-services.ru/docs/.`

## Файлы:
- allure_results - каталог с отчетом о тестировании
- tests/ - каталог с автотестами
- tests/test_create_courier.py - тесты на создание курьера 
- tests/test_login_courier.py - тесты на авторизацию курьера
- tests/test_order.py - тесты на создание заказа и получение списка заказов
- urls - файл с URL и эндпоинтами сервиса
- helpers.py - вспомогательные данные для тестирования
- requirements.txt - файл с зависимостями
- conftest.py - фикстуры
- decorators.py - декораторы для человекочитаемых шагов тестов

Перед работой с репозиторием нужно
1. Установить зависимости 
```
pip install -r requirements.txt
```
2. Запустить все тесты
```
pytest tests --alluredir=allure_results
```
3. Посмотреть отчет о тестировании
```
allure serve allure_results
```