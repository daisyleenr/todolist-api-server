# coding: utf-8

import os

DB_STRING = os.getenv("TODO_DB_STRING", "mysql://root:root@localhost/todolist?charset=utf8")
