from api import app
from flask import request
from calc.calc import calculator
from api.database import Database


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        try:
            data = request.json
            expression_id = calculator(data)
            return expression_id
        except TypeError:
            return "Example request: {'expression': 'a+b*10-c*d'" \
                   ", 'variables': {'a': 10, 'b': 12, 'c': 23, 'd': 30}}"
    elif request.method == 'GET':
        try:
            data = request.json
            expression_id = data['expression_id']
            data = Database.query.filter_by(id=expression_id).first()
            return str({'result': data.result})
        except TypeError:
            return "Example request: 'expression_id': 11"
    return 'OK'
