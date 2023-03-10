# Django

### Наш проект основан на изучении Django и представляет из себя сайт "Доска объявлений", на котором пользователи могут публиковать, редактировать и комментировать объявления. Так же реализована регистарция и активация по email.

#### Все работы основаны на книге - Дронов В.А. - Django 3.0. Практика создания веб-сайтов на Python (Профессиональное программирование) - 2021

---

## Установка:

```
git clone https://github.com/Dmitrykevich/Django_3_0_practice.git --single-branch
# Скопируйте главную ветвь
python -m venv venv
# Внутри папки Django_3_0_practice активируйте виртуальное окружение 
pip install -r requirements.txt
# Установите библиотеки-зависимости
python manage.py makemigrations
python manage.py migrate
# Создайте миграции и приментие их
python manage.py runserver
# Запустите локальный сервер Django
```

---

## Отладочнымй SMTP-сервер:

Чтобы протестировать отправку электронных писем, воспользуемся отладочным SMTP-сервером. В модуль `settings.py` пакета
конфигурации внесён дефолтный для отладочного сервера TCP-порт:
`EMAIL_PORT = 1025`
В новом экземпляре командной стркои запустим отладочный SMTP-сервер:

```
python -m smtpd -n -c DebuggingServer localhost:1025
```

### Все коммиты помечены и создавались с изучением по номерам глав

Пример перехода в главу
[32.4. Bеб-страницы регистрации и активиции пользователей](https://github.com/Dmitrykevich/Django_3_0_practice/commit/3b1e86556cc377ed5bc6ae549f481d4d279266f7)
где в модуле `bboard/main/utilities.py` необходимо исправить импорт `ALLOWED_HOSTS`,
что было бы небольшим домашним заданием :)