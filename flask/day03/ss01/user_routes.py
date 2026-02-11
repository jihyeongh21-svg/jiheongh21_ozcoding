from flask_smorest import Blueprint, abort
from flask import request, jsonify

def create_user_blueprint(mysql):
    user_blp = Blueprint('user_routes', __name__, url_prefix='/users')
    
    @user_blp.route('/', methods=['GET'])
    def get_users():
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, username, email FROM users')
        users = cursor.fetchall()
        cursor.close()

        users_list = []
        for user in users:
            users_list.append({
                'id': user['id'],
                'name': user['username'],
                'email': user['email']
            })
        return jsonify(users_list)

    @user_blp.route('/', methods=['POST'])
    def add_user():
        user_data = request.json
        if not user_data or 'name' not in user_data or 'email' not in user_data:
            abort(400, message="Invalid user data")
            
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (username, email) VALUES (%s, %s)',
                        (user_data['name'], user_data['email']))
        mysql.connection.commit()
        user_id = cursor.lastrowid
        cursor.close()
        
        return jsonify({'id': user_id, 'name': user_data['name'], 'email': user_data['email']}), 201

    @user_blp.route('/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user_data = request.json
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE users SET username = %s, email = %s WHERE id = %s',
                        (user_data['name'], user_data['email'], user_id))
        mysql.connection.commit()
        cursor.close()
        return '', 204

    
    @user_blp.route('/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
        mysql.connection.commit()
        cursor.close()
        return '', 204

    return user_blp