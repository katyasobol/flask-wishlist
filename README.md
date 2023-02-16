# Flask wishlist
Веб-приложение Flask для создания списка желаний и управления им.

## Особенности:

1. Аутентификация пользователя (регистрация, вход и выход). 
2. Создание и изменение профиля пользователя
3. Создание, изменение и удаление списка желаний
4. ДСоздание, изменение и удаление элементов из списка желаний
5. Восзможность отметить элемент как завершенный
6. Просмотр всех элементов в списке желаний

## Requirements.txt

1. Python 3.x
2. Flask
3. Flask-SQLAlchemy
4. Flask-Login
5. Flask-WTF
6. passlib

 ## Скачивание
 
 1. Скопируйте репозиторий
```python
git clone https://github.com/katyasobol/flask-wishlist.git
```
2. Перейдите в директорию проекта
```python
cd flask-wishlist
```
3. Установите все нобходимые зависимости
```python
pip install -r requirements.txt
```
4. Установите переменные среды для Flask
```python
export FLASK_APP=app.py
export FLASK_ENV=development
```
5. Инициализируйте базу данных
```python
flask init-db
```
6. Запустите приложение
```python
flask run
```


