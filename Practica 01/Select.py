from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def get_users():   
    # get data form DB
    result = [
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
    
    return jsonify(result)

@app.route('/user/<id>', methods=['GET'])
def get_user(id):   
    # get data form DB
    # buscar usuario (dummy)

    result = {            
            'id': id, 
            'name':'vicente',
            'email':'vicente@gmail.com',
            'address':'Arequipa',
            'description':'...'             
        }    
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5002)