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

@app.route('/user/upload_photo', methods=['POST'])
def upload_file():
    print("Headers:", request.headers)
    print("Files:", request.files)
    
    if 'file' not in request.files:
        return jsonify({'result': False, 'message': 'No se envió ningún archivo'}), 400  

    f = request.files['file']
    ruta_destino = r"C:\Users\da968\Documents\Trabajos 2025 A\Construcción de Software\Practica 01\Galeria\\" + f.filename
    f.save(ruta_destino)

    return jsonify({'result': True, 'message': 'Archivo subido con éxito'})



if __name__ == '__main__':
    app.run(debug=True, port=5002)
