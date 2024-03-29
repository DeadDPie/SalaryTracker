
## Что реализовано
- [ ] REST-сервис на fastapi
- [ ] зависимости зафиксированы менеджером зависимостей poetry
- [ ] написаны тесты с использованием pytest
- [ ] реализована возможность собирать и запускать контейнер с сервисом в Docker
- [ ] Технология аутентификации JSON Web Token (JWT) (OAuth2 с паролем (и хэшированием), Bearer с токенами JWT)
- [ ] Middleware
## Реализация
Как базу данных использую json file
-  Что можно делать?
   1) Просмотреть список всех работников:
   - Metod: GET
   - Endpoint: `host:port/api/users`
   2) Получить токен:
   - Metod: POST
   - Endpoint: `host:port/api/token`
   3) Просмотр текущей зарплаты и даты следующего повышения авторизованного работника
   - Metod: GET
   - Endpoint: `host:port/api/salary`


#### Логины и пароли:
    - Kolya TheBestPassword
    - Jane 123
    - Olesya ilovecats

## Запуск

Скачать файлы из репозитория или клонировать репозиторий

### Запуск в контейнере Docker

*Для запуска должeн быть установлен docker*

Создаём образ `docker build -t myimage .`

Создаём контейнер на основе образа `docker run -d --name mycontainer -p 80:80 myimage`

Прописываем `docker logs` и id контейнера

После запуска, API доступно по адресу `http://localhost:8000/docs`

Примечание:
- Назвать образ и контейнер можно по-другому. Я привела пример названий.

### Установка зависимостей с помощью Poetry

*Для запуска должен быть установлен пакет Poetry [инструкция](https://python-poetry.org/docs/)*

- Для установки зависимостей выполнить команду `poetry install`

- Для запуска виртуального окружения выполнить команду `poetry shell`

- Запустить main.py 

- После запуска, API доступно по адресу `http://localhost:8000/docs`

## Тестирование
Для запуска виртуального окружения выполнить команду `poetry shell`

В переменную среды добавляем значение пути до проекта и запускаем тесты, выполнив команду `export PYTHONPATH=$(pwd) && pytest -v`

