# todolist api server

Flask project for study

- Flask
- pipenv
- MySQL
- Frontend: https://github.com/daisyleenr/todolist-react

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

# Set DB STRING

```
$ export TODO_DB_USER=todolist
$ export TODO_DB_PASSWORD=todolist
$ export TODO_DB_NAME=todolist
$ export TODO_DB_HOST=localhost
```

# Run

```
$ python app.py
```

# Run with docker

```
$ docker run -p 5000:5000 -e ~~~ daisyleenr/todo-api-server
```

# Build docker

```
$ docker build -t daisyleenr/todo-api-server:0.1 .
```
