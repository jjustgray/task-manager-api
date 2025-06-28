# Лабораторна робота №1 + №2

**ПІБ:** Пшеничний Сергій Володимирович  
**Група:** КВ-42мп 
**Дисципліна:** Технології розробки веб-додатків  
**Завдання:** API для Task Manager (список справ)  
**Репозиторій фронтенду:** https://github.com/jjustgray/task-manager-ui  
**Посилання на звіт №1:** [Google Docs](https://docs.google.com/document/d/1GUImBWqVSiFMctQPjHu49WQ0rjDM6GSXdHtv-68NRLM/edit?usp=sharing)
**Посилання на звіт №2:** [Google Docs](https://docs.google.com/document/d/1lZceM9JW6ZFabeaBKCnJhGrBlmGChSn6B2lHVWSJF8s/edit?usp=sharing)

## Опис для лаби №1

Цей сервер реалізує REST API для керування задачами:

- реєстрація користувача
- авторизація через JWT
- додавання / редагування / видалення задач
- документація OpenAPI через Redoc
- захист API через токени

## Команди

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Опис для лаби №2

Загальне завдання: розробити функції обміну даними між користувачами Web-додатка, а також адміністрування користувачами у реальному часі.
На основі обраної тематики (див. рекомендований список) і реалізованого у лабораторній роботі №1 Web-додатку виконати розробку наступних функціональних вимог:
Можливість передавати робочі дані додатку між користувачами у реальному часі. 
Адміністратору додатка мати можливість переглядати список користувачів, які працюють з додатком у даний час (список користувачів “онлайн”).

## Команди

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
daphne taskmanager_backend.asgi:application
```
