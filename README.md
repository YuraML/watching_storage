# Пульт охраны банка

Сайт, подключенный к базе данных сотрудников банка, где можно проверить историю посещения каждого сотрудника.

### Как установить

Параметры базы данных находятся в файле .env. Его необходимо создать и заполнить в таком порядке: 

 ```
DB_ENGINE=' '
DB_HOST=' '
DB_PORT=' '
DB_NAME=' '
DB_USER=' '
DB_PASSWORD=' '

SECRET_KEY=' '

DEBUG=False
 ```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

В терминале введите:
```
python manage.py runserver 0.0.0.0:8000
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).