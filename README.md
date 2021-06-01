# DjangoAirline
Sample app for [CS50](https://cs50.jp/) Web 2020 > [SQL, Models, and Migrations](https://cs50.jp/web/2020/sql-models-and-migrations/notes/)

## Learning environment
* macOS Catalina 10.15.7
* Python 3.9.5

## How to setup
After [download Python](https://www.python.org/downloads/),
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip3 install Django
```

## How to start server
```
cd DjangoAirline
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py test
python3 manage.py runserver
```
