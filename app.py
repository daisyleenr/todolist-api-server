# coding: utf-8

from flask import Flask, Response, request, jsonify
# import ujson as json
# import json
from flask_cors import CORS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from model import Todos
from config import DB_STRING
from marshmallow import Schema, fields

print("connect: " + DB_STRING)
engine = create_engine(DB_STRING, echo=True, pool_recycle=3600)
Session = sessionmaker(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


class TodoSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    checked = fields.Boolean()
    created_at = fields.DateTime()


todos_schema = TodoSchema(many=True)


@app.route("/")
def index():
    return "Hello Todolist :)"


@app.route("/todos")
def get_todos():
    todos = db_session.query(Todos).all()
    return jsonify(todos_schema.dump(todos).data)


@app.route("/todos", methods=['POST'])
def add_todo():
    todo_text = request.form['text']
    db_session.add(Todos(title=todo_text))
    db_session.commit()

    todos = db_session.query(Todos).all()
    return jsonify(todos_schema.dump(todos).data)


@app.route("/todos/<int:todo_id>", methods=['PUT'])
def update_todo(todo_id):
    todo = db_session.query(Todos).filter_by(id=todo_id).one()
    todo.checked = 0 if todo.checked == 1 else 1
    db_session.commit()

    todos = db_session.query(Todos).all()
    return jsonify(todos_schema.dump(todos).data)


@app.route("/todos/<int:todo_id>", methods=['DELETE'])
def remove_todo(todo_id):
    db_session.query(Todos).filter_by(id=todo_id).delete()
    db_session.commit()

    todos = db_session.query(Todos).all()
    return jsonify(todos_schema.dump(todos).data)


if __name__ == "__main__":
    app.run(debug=True)
