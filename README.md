# allmax_test

Для запуска:

1. Создать PostgreSQL базу данных
2. Настроить переменные окружения:  
    TODO_DB - Имя базы данных  
    PGUSER - пользователь для доступа к бд  
    PGPWD - пароль от базы  
    EMAIL_HOST - smtp email server  
    EMAIL_PORT - порт на почтовом сервере  
    EMAIL_USER - пользовател для авторизации на почтовом сервере  
    EMAIL_PWD - пароль для авторизации на почтовом сервере  
 4. Создать виртуальное окружение и установить зависимости (requirements.txt)
 5. Запустить миграции  
  python manage.py migrate  
 6. Запустить сервер  
  python manage.py runserver
 7. Открыть http://127.0.0.1/todo_list/app
 
Протестировано в Google Chrome на десктопе
