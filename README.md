# pageshot bot
[![License MIT](https://img.shields.io/badge/licence-MIT-green)](https://opensource.org/license/mit/)
[![Code style black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Python versions](https://img.shields.io/badge/python-3.11-blue)](#)
[![Telegram API](https://img.shields.io/badge/Telegram%20Bot%20API-6.9-blue?logo=telegram)](https://core.telegram.org/bots/api)
[![Aiogram version](https://img.shields.io/badge/Aiogram-3.1.1-blue)](https://aiogram.dev/)
[![Main auto_bot workflow](https://github.com/andprov/auto_bot/actions/workflows/main.yml/badge.svg)](https://github.com/andprov/auto_bot/actions/workflows/main.yml)


<details> 
  <summary>Задание</summary>
Напиши клон телеграм-бота @siteshot_bot, который присылает скриншот вебстраницы в ответ на присланную боту ссылку.


### Технические требования
1. Бот должен быть написан на языке Python
2. Все настройки бот должен брать из переменных окружения или .env
файла
3. Бот и необходимые ему сервисы должны разворачиваться в контейнерах
с помощью Docker Compose
4. Зависимости бота указаны в requirements.txt с версиями или с помощью
инструментов вроде Poetry
5. Для бота есть инструкция по его развёртыванию в README.md проекта
6. Бот логгирует свою работу с использованием библиотеки logging или
loguru
7. Перезапуск контейнеров не должен приводить к потере данных
8. (бонус +1 балл) Процесс получения скриншота не должен блокировать
работу бота (бот должен продолжать отвечать на сообщения от других
пользователей)

### Функциональные требования
1. Бот работает и в личных сообщениях и при добавлении в чат.
2. По команде /start бот встречает пользователя сообщением-приветствием,
которое рассказывает о функционале бота.
3. При получении сообщения с ссылкой, бот присылает сообщение-
заглушку, о том что запрос принят, и запускает процесс получения
скриншота в фоне.
4. Когда скриншот получен, бот редактирует сообщение-заглушку:
a. Прикрепляет скриншот к сообщению
b. Заменяет текст сообщения на заголовок сайта, URL и время обработки
страницы
c. (бонус 1 балл) добавляет к сообщению кнопку “Подробнее”, которая
показывает WHOIS сайта
5. Скриншоты бот так же сохраняет в файловую систему. В имени файла
обязательно должны быть: дата запроса, user_id пользователя, домен из
url запроса.
6. (бонус 5 баллов) Бот сохраняет статистику о своей работе в базу данных -
PostgreSQL или ClickHouse
7. (бонус 1 балл) Бот позволяет выбрать язык работы - русский или
английский. После переключения языка все последующие сообщения от
бота выводятся на выбранном языке.

</details>


![Pic](https://github.com/andprov/auto_bot/blob/main/img/pic.png?raw=true "Pic")


# Установка
[Создать бота и получить](https://core.telegram.org/bots#how-do-i-create-a-bot) `BOT_TOKEN`

Возможно два сценария установки локально и в [Docker](https://docs.docker.com/engine/install/).

## Локальная установка
Для локальной установки необходимо наличие [PostgreSQL](https://www.postgresql.org/download/) 
в системе.

Клонировать репозиторий:
```shell
git clone <https or SSH URL>
```

Перейти в каталог проекта:
```shell
cd pageshot_bot
```

Создать файл `.env` с переменными окружения, со следующим содержанием:
```shell
# MODE
DEBUG=True

# BOT
BOT_TOKEN=<bot_token>
GROUP_ID=<group_id>

# DB
DB_TYPE=postgresql
DB_CONNECTOR=psycopg
DB_HOST=db
DB_PORT=5432
POSTGRES_DB=bot
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# REDIS
REDIS_HOST=redis
REDIS_PORT=6379
```

Создать базу данных PostgreSQL с именем `bot`.

```shell
createdb -U postgres -h localhost -p 5432 bot
```

Создать и активировать виртуальное окружение:
```shell
python3 -m venv .venv
source .venv/bin/activate
```

Обновить pip:
```shell
pip install --upgrade pip
```

Установить зависимости:
```shell
pip install -r requirements.txt
```

Выполнить миграции:
```shell
alembic upgrade head
```

Запустить приложение:
```shell
python -m app
```

## Установка в Docker на удаленный сервер
Дальнейшая инструкция предполагает, что удаленный сервер настроен на работу 
по SSH. На сервере установлен Docker. Зарегистрирован аккаунт на 
[hub.docker.com](https://hub.docker.com/)

Клонировать репозиторий:
```shell
git clone <https or SSH URL>
```

Перейти в каталог проекта:
```shell
cd pageshot_bot
```

Создать файл .env с переменными окружения, со следующим содержанием:
```shell
# MODE
DEBUG=False

# BOT
BOT_TOKEN=<bot_token>
GROUP_ID=<group_id>

# DB
DB_TYPE=postgresql
DB_CONNECTOR=psycopg
DB_HOST=db
DB_PORT=5432
POSTGRES_DB=bot
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# REDIS
REDIS_HOST=redis
REDIS_PORT=6379

# Docker images
DB_IMAGE=postgres:14
REDIS_IMAGE=redis:7
BOT_IMAGE=<user_name/image_name>
```

Подготовить docker images образ:
```shell
sudo docker build -t <username>/<image_name> .
```

Загрузить образ на Docker Hub:
```shell
sudo docker push <username>/<image_name>
```

Выполнить сборку и запуск:
```shell
sudo docker compose -f docker-compose.yml up -d
```
