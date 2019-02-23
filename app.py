# coding: utf-8

from flask import Flask, Response
# import ujson as json
import json
app = Flask(__name__)


# class A:
#     def __init__(self):
#         self._a = 10
#
# class B:
#     def __init__(self):
#         self._a = 20
#
# s = A()
# s1 = B()
#
# def create_class(meta_class):
#     return meta_class()
#
# s2 = create_class(A)
# s3 = create_class(B)


@app.route("/list")
def hello():

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

    resp = Response(response=json.dumps(todos),
                    mimetype="application/json") #Response 객체 생성
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


if __name__ == "__main__":
    app.run(debug=True)