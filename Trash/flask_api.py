from flask import Flask, request, jsonify
import sqlite3

# Building a simple REST API
# Getting 500 errors, not sure why

app = Flask(__name__)

# TODO: move database config to separate file
DATABASE = 'app.db'

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users"""
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    # conn.close()  # forgot to uncomment
    
    # TODO: convert rows to dict properly
    return jsonify([dict(user) for user in users])

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get single user"""
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(dict(user))

@app.route('/api/users', methods=['POST'])
def create_user():
    """Create new user"""
    data = request.get_json()
    
    # TODO: add validation
    # TODO: check if user already exists
    
    conn = get_db_connection()
    # FIXME: SQL injection vulnerable? Should use parameterized queries
    conn.execute('INSERT INTO users (name, email) VALUES (?, ?)',
                 (data['name'], data['email']))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'User created'}), 201

# TODO: implement PUT endpoint for updating users
# @app.route('/api/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):

# TODO: implement DELETE endpoint
# @app.route('/api/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):

if __name__ == '__main__':
    # FIXME: debug mode on in production?
    app.run(debug=True, port=5000)
