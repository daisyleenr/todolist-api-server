# todolist api server
Flask project for study

* Flask
* pipenv
* MySQL
* Frontend: https://github.com/daisyleenr/todolist-react

# Requirements
python >= 3.7
pipenv
mysql >= 5.7

# Install modules
```
$ pipenv install
```

# Activate this project's virtualenv
```
$ pipenv shell
```

# Set the config.py
```
$ cp config.py.original config.py
$ vi config.py
# coding: utf-8
DB_USER = ''
DB_PASS = ''
DB_NAME = ''
DB_STRING = '' 
# ex: mysql://username:password@localhost/database?charset=utf8
```

# Run
```
$ python app.py
```
