from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def user():   
    name = request.json['name']
    lastname = request.json['lastname']
    age = request.json['age']
    height = request.json['height']
    weight = request.json['weight']

    print('inserting new user', name, lastname, age, height, weight)

    result = {'result': True, 'message':'OK' }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5002)