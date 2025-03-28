from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de base de datos con estructura mejorada
users_db = [
    {            
        'id': "scvs98ds98d7c98s7d", 
        'name': 'Vicente',
        'lastname': 'Gómez',
        'age': 30,
        'height': 1.75,
        'weight': 70,
        'email': 'vicente@gmail.com',
        'address': 'Arequipa'
    },
    {            
        'id': "353gdfg345", 
        'name': 'Pepito',
        'lastname': 'Pérez',
        'age': 25,
        'height': 1.68,
        'weight': 65,
        'email': 'pepito@gmail.com',
        'address': 'Lima'
    }
]

@app.route('/user', methods=['GET'])
def get_users():   
    name_filter = request.args.get('name')  # Filtrar por nombre (opcional)

    if name_filter:
        filtered_users = [user for user in users_db if user['name'].lower() == name_filter.lower()]
        return jsonify(filtered_users if filtered_users else {'message': 'No users found'}), 404 if not filtered_users else 200

    return jsonify(users_db)

@app.route('/user', methods=['PUT'])
def update_user():   
    data = request.json
    required_fields = ['id', 'name', 'lastname', 'age', 'height', 'weight', 'email', 'address']

    if not data or not all(field in data for field in required_fields):
        return jsonify({'result': False, 'message': 'Missing required fields'}), 400

    for user in users_db:
        if user['id'] == data['id']:
            user.update(data)  # Actualiza el usuario
            print('Updating user:', data)
            return jsonify({'result': True, 'message': 'User updated successfully'})

    return jsonify({'result': False, 'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5002)
