<h1>Приложение для проверки качества кода</h1>

<h3>Краткое описание</h3>
В файле tz.md описано ТЗ данного приложения.

Из перечисленного там реализованы:
<ul>
<li>Регистрация и авторизация пользователей</li>
<li>Загрузка файлов .py (есть проверка на расширение файла)</li>
<li>Добавление файлов в очередь проверки</li>
<li>Есть несколько видов запуска проверки: ручная и автоматическая (при помощи Celery)</li>
<li>Реализована API прослойка с авторизацией по токену</li>
</ul>

----

<h3>Используемые технологии</h3>
<ul>
<li>Python 3.11</li>
<li>Django 4.2.3</li>
<li>Postgres</li>
<li>DRF</li>
<li>Docker</li>
<li>Celery, Redis</li>
<li>flake8 (в модуле проверки кода)</li>
</ul>

----

<h3>Локальный запуск</h3>

Файл .env для локального запуска:
> DB_ENGINE=django.db.backends.postgresql <br> 
DB_HOST=db <br>
DB_PORT=5432 <br>
CELERY_BROKER_URL=redis://redis:6379/0 <br>
SECRET_KEY= <br>
DEBUG=True <br>
POSTGRES_HOST_AUTH_METHOD=md5 <br>
POSTGRES_PASSWORD=postgres <br>
POSTGRES_USER=postgres <br>
POSTGRES_DB=cqs <br>
PGUSER=postgres

Команда для локального запуска (из корня проекта):<br>
<code>docker compose -f local.yml up</code>