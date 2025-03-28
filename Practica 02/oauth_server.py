from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = "clave_secreta"

# Endpoint para obtener token OAuth
@app.route('/oauth/token', methods=['POST'])
def generate_token():
    data = request.json

    if not data or data.get('username') != 'admin' or data.get('password') != '1234':
        return jsonify({'error': 'Invalid credentials'}), 401

    payload = {
        'user': data['username'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expira en 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return jsonify({'access_token': token})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
