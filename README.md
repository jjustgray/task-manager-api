# Лабораторна робота №1

**ПІБ:** Пшеничний Сергій Володимирович  
**Група:** КВ-42мп 
**Дисципліна:** Технології розробки веб-додатків  
**Завдання:** API для Task Manager (список справ)  
**Репозиторій фронтенду:** https://github.com/jjustgray/task-manager-ui  
**Посилання на звіт:** [Google Docs](https://docs.google.com/document/d/1GUImBWqVSiFMctQPjHu49WQ0rjDM6GSXdHtv-68NRLM/edit?usp=sharing)

## Опис

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
