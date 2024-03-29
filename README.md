## KITTYGRAM
![workflow](https://github.com/fantomv1/kittygram_final/actions/workflows/main.yml/badge.svg/)

### Описание:
>KITTYGRAM - сервис для хранения воспоминания о своих питомцах (котах).

>Проект позволяет хранить информацию о котах - их имена, даты рождения, их фото и "достижения", а также предоставляет интерфейс для обмена данными в формате JSON.

>Позволяет выдавать информацию сторонним клиентам и обрабатывать полученные от них данные.

### Стек используемых технологий:
Linux, SQLite, PostgreSQL, Python, Django, Rest_framework, JavaScript, Git, Docker, GitHub Actions.

### Тестовое развёртывание на локальном копьютере:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:fantomv1/kittygram_final.git
```

```
cd kittygram_final
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Заполнить файл .env (описание - далее).

При тестовом развёртывнии (SQLite) выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Развёртывание на удаленном сервере через DockerCompose:

- Настроить удаленный сервер.

Операционная система - Ubuntu, управление по SSH, установить Docker и Docker Compose, прокси сервер должен переадресовывать всё запросы (включая статику) на порт 9000.

Пример для Nginx:

```
server {
    server_name ваш_домен;

    location / {
        proxy_pass http://127.0.0.1:9000;
    }
}
```

- Создать аккаунт на DockerHub.

- Создать бота в Telegram.

- Настроить GitHub Actions.

Добавить секреты в Repository secrets (Settings - Secrets and variables - Actions):

USER - имя пользователя на удаленном сервере.

HOST - IP адрес сервера.

SSH_KEY - Закрытый ключ SSH для доступа к серверу.

SSH_PASSPHASE - кодовая фраза ключа SSH.

DOCKER_USERNAME - логин на DockerHub.

DOCKER_PASSWORD - пароль на DockerHub.

TELEGRAM_TO - ID TELEGRAM аккаунта, на который нужно отправить сообщение.

TELEGRAM_TOKEN - токен TELEGRAM бота.

- Отправить репозиторий на github, проект на сервер загрузится автоматически.

### Как заполнить .env:

Пример заполнения есть в файле .env.example.

POSTGRES_DB - имя базы данных POSTGRES.

POSTGRES_USER - логин базы данных POSTGRES.

POSTGRES_PASSWORD - пароль базы данных POSTGRES.

DB_NAME - имя базы данных.

DB_HOST - названия контейнера с базой данных POSTGRES.

DB_PORT - порт для связи с контейнером базы данных POSTGRES

# Настройки settings.py django:

SETTINGS_SECRET_KEY - SECRET_KEY django.

SETTINGS_DEBUG - режим отладки.

SETTINGS_ALLOWED_HOSTS - разрешенные хосты для работы сервера. **Перечисляются через пробел**.

SETTINGS_DATABASES_SQLITE - true, чтобы подключить локальную БД SQLite для тестового запуска.


>Автор: fantomv1