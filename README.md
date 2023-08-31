# Messenger API
### О проекте
Messenger API - серерная чать мессенджера. После регистрации в сервисе пользователь может искать других пользователей по имени, фамилии, username, email или телефону.
Есть возможность создать диалог с другим пользователем и отправлять ему сообщения. Пользователь может удалить диалог или свои сообщения.


### Технологии
- Python
- Django
- DRF
- Djoser
- Docker
- PostgreSQL

### Как запустить проект
- Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Etozheigor/messenger.git
```

```
cd messenger
```

- Активировать виртуальное окружение и установить зависимости:

```
poetry shell
poetry install
```

- перейти в папку messenger_api/messenger_api, создать файл .env и заполнить его по шаблону (можно использовать
файл .env.example, заполнив необходимые данные и просто переименовав его в .env) :


шаблон заполнения файла:

```
SECRET_KEY= # секретный ключ Джанго-проекта
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER= # логин для подключения к базе данных (установите свой)
POSTGRES_PASSWORD= # пароль для подключения к БД (установите свой)
DB_HOST=localhost
DB_PORT=5432
```


База данных Postgres запускается в контейнере Docker:

- Перейти в папку с файлом docker-compose.yml и запустить контейнер:

```
docker-compose up
```
- Перейти в папку messenger_api, выполнить миграции и запустить проект

```
cd messenger_api
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Проект будет доступен локально по адресу:

```
http://localhost/
```

Документация к Api находится по адресу:

```
http://localhost/swagger/
```

### Эндпоинты проекта:
- Регистрация и поиск пользователей:
```
http://localhost/api/v1/users/
```
- Изменение своих данных:
```
http://localhost/api/v1/users/me
```
- Вход/выход из системы (получение токена)
```
http://localhost/api/v1/auth/jwt/create/
http://localhost/api/v1/auth/jwt/refresh/
http://localhost/api/v1/auth/jwt/verify/
```
- Cоздание, чтение и удаление диалогов:
```
http://localhost/api/v1/dialogues/
```
Ограничение вывода количества сообщений в диалоге - через query param messages_limit:
```
GET http://localhost/api/v1/dialogues/?messages_limit=10
```

- Отправка и удаление сообщений:
```
http://localhost/api/v1/messages/
```
