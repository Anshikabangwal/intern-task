from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
# from werkzeug.security import generate_password_hash

app = Flask(__name__)
CORS(app)

def connect_db():
    return psycopg2.connect(
        dbname='trial',
        user='postgres',
        password='prachi',
        host='localhost'
    )

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    conn.commit()

    return jsonify({"message": "User created successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if user:
        return jsonify({"message": "Login successful", "token": "your_generated_token"}), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401
    
if __name__ == '__main__':
    app.run(debug=True)
