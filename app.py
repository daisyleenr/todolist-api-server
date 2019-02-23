# coding: utf-8

from flask import Flask, Response, request
# import ujson as json
import json
from flask_cors import CORS
import MySQLdb
from config import *


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def get_db_connect():
    db = MySQLdb.connect(user=DB_USER, passwd=DB_PASS, db=DB_NAME)
    return db

@app.route("/todos")
def get_todos():
    db = get_db_connect()
    c = db.cursor(MySQLdb.cursors.DictCursor)
    c.execute("""select id, todo as text, checked, UNIX_TIMESTAMP(created_at) as created_at from todos""")
    todos = c.fetchall()
    c.close()

    resp = Response(response=json.dumps(todos),
                    mimetype="application/json") #Response 객체 생성
    return resp


@app.route("/todos", methods=['POST'])
def add_todo():
    db = get_db_connect()
    c = db.cursor(MySQLdb.cursors.DictCursor)

    todo_text = request.form['text']
    c.execute(f"""insert into todos(todo) values('{todo_text}')""")
    db.commit()

    c.execute("""select id, todo as text, checked, UNIX_TIMESTAMP(created_at) as created_at from todos""")
    todos = c.fetchall()
    c.close()

    resp = Response(response=json.dumps(todos),
                    mimetype="application/json") #Response 객체 생성
    return resp


@app.route("/todos/<int:todo_id>", methods=['PUT'])
def update_todo(todo_id):
    db = get_db_connect()
    c = db.cursor(MySQLdb.cursors.DictCursor)

    c.execute(f"""select * from todos where id = '{todo_id}'""")
    todo = c.fetchone()
    checked = 0 if todo['checked'] == 1 else 1
    c.execute(f"""update todos set checked='{checked}' where id = '{todo_id}'""")
    db.commit()

    c.execute("""select id, todo as text, checked, UNIX_TIMESTAMP(created_at) as created_at from todos""")
    todos = c.fetchall()
    c.close()

    resp = Response(response=json.dumps(todos),
                    mimetype="application/json")  # Response 객체 생성
    return resp


@app.route("/todos/<int:todo_id>", methods=['DELETE'])
def remove_todo(todo_id):
    db = get_db_connect()
    c = db.cursor(MySQLdb.cursors.DictCursor)

    c.execute(f"""delete from todos where id = {todo_id}""")
    db.commit()

    c.execute("""select id, todo as text, checked, UNIX_TIMESTAMP(created_at) as created_at from todos""")
    todos = c.fetchall()
    c.close()

    resp = Response(response=json.dumps(todos),
                    mimetype="application/json") #Response 객체 생성
    return resp


if __name__ == "__main__":
    app.run(debug=True)
