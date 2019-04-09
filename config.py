# coding: utf-8

import os

DB_USER = os.getenv("TODO_DB_USER", "todolist")
DB_PASSWORD = os.getenv("TODO_DB_PASSWORD", "todolist")
DB_NAME = os.getenv("TODO_DB_NAME", "todolist")
DB_HOST = os.getenv("TODO_DB_HOST", "localhost")
DB_STRING = "mysql://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_HOST + "/" + DB_NAME + "?charset=utf8"
