from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
SECRET_KEY = "clave_secreta"

users_db = [
    {            
        'id': "scvs98ds98d7c98s7d", 
        'name':'vicente',
        'email':'vicente@gmail.com'             
    },
    {            
        'id': "353gdfg345", 
        'name':'pepito',
        'email':'pepito@gmail.com'             
    }
]

# Middleware para verificar el token
def verify_token():
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith("Bearer "):
        return None

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

@app.route('/user', methods=['GET'])
def get_users():   
    user_data = verify_token()
    if not user_data:
        return jsonify({'error': 'Unauthorized'}), 400
    
    return jsonify(users_db)

@app.route('/user', methods=['PUT'])
def update_user():   
    data = request.json
    required_fields = ['id', 'name', 'email']

    if not data or not all(field in data for field in required_fields):
        return jsonify({'result': False, 'message': 'Missing required fields'}), 400

    for user in users_db:
        if user['id'] == data['id']:
            user.update(data)  # Actualiza el usuario
            print('Updating user:', data)
            return jsonify({'result': True, 'message': 'User updated successfully'})

    return jsonify({'result': False, 'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(port=5002, debug=True)
