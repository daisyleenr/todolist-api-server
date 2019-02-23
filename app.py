# coding: utf-8

from flask import Flask, Response, request
# import ujson as json
import json

from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

todos = [
    {
        'id': 0,
        'text': '앵귤러 배우고',
        'checked': True,
    },
    {
        'id': 1,
        'text': '리액트 배우고',
        'checked': False,
    },
    {
        'id': 2,
        'text': '뷰 배우자',
        'checked': False,
    },
]


@app.route("/todos")
def get_todos():
    resp = Response(response=json.dumps(todos),
                    mimetype="application/json") #Response 객체 생성
    return resp


@app.route("/todos", methods=['POST'])
def add_todo():
    is_checked = request.form['check'] == 'true'
    value = {'text': request.form['text'], 'checked': is_checked, 'id': len(todos)}
    todos.append(value)

    resp = Response(response=json.dumps(value),
                    mimetype="application/json") #Response 객체 생성
    return resp


@app.route("/todos/<int:todo_id>", methods=['PUT'])
def update_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['checked'] = not todo['checked']
            break

    resp = Response(response=json.dumps(todos),
                    mimetype="application/json")  # Response 객체 생성
    return resp


@app.route("/todos/<int:todo_id>", methods=['DELETE'])
def remove_todo(todo_id):
    for idx, todo in enumerate(todos):
        if todo['id'] == todo_id:
            # todos.remove(todo)
            todos.pop(idx)
            break

    resp = Response(response=json.dumps(todos),
                    mimetype="application/json") #Response 객체 생성
    return resp


if __name__ == "__main__":
    app.run(debug=True)
