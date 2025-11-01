"""
Example Vulnerable Web Application

WARNING: This application contains INTENTIONAL security vulnerabilities
for educational and testing purposes. DO NOT deploy to production!

Purpose: Demonstrate bug hunting framework capabilities
"""

import sqlite3
import os
import subprocess
from flask import Flask, request, render_template_string, session
import pickle
import jwt
from datetime import datetime, timedelta


app = Flask(__name__)
app.secret_key = "hardcoded_secret_key_123"  # Vulnerability: Hardcoded secret


# Vulnerability: SQL Injection
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # VULNERABLE: String concatenation in SQL query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)  # SQL Injection vulnerability
    user = cursor.fetchone()

    if user:
        # Vulnerability: Weak JWT (accepts 'none' algorithm)
        token = jwt.encode(
            {'user': username, 'exp': datetime.utcnow() + timedelta(hours=24)},
            app.secret_key,
            algorithm='HS256'
        )
        return {'token': token, 'status': 'success'}
    return {'status': 'failed'}


# Vulnerability: Authentication Bypass (JWT with 'none' algorithm)
@app.route('/validate_token', methods=['POST'])
def validate_token():
    token = request.headers.get('Authorization')

    # VULNERABLE: Accepts 'none' algorithm
    try:
        payload = jwt.decode(
            token,
            app.secret_key,
            algorithms=['HS256', 'none']  # Vulnerability: Allows 'none'
        )
        return {'user': payload.get('user'), 'valid': True}
    except:
        return {'valid': False}


# Vulnerability: XSS (Cross-Site Scripting)
@app.route('/profile', methods=['GET'])
def profile():
    name = request.args.get('name', 'Guest')

    # VULNERABLE: Unescaped user input in template
    template = f"""
    <html>
        <body>
            <h1>Welcome {name}!</h1>
        </body>
    </html>
    """
    return render_template_string(template)  # XSS vulnerability


# Vulnerability: IDOR (Insecure Direct Object Reference)
@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    # VULNERABLE: No authorization check
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
    user = cursor.fetchone()

    if user:
        return {
            'id': user[0],
            'username': user[1],
            'email': user[2],
            'ssn': user[3]  # Sensitive data exposed!
        }
    return {'error': 'Not found'}


# Vulnerability: Command Injection
@app.route('/ping', methods=['POST'])
def ping():
    host = request.form.get('host')

    # VULNERABLE: Unsanitized input in shell command
    result = subprocess.check_output(
        f"ping -c 1 {host}",
        shell=True  # Command injection vulnerability
    )
    return {'result': result.decode()}


# Vulnerability: Path Traversal
@app.route('/download')
def download():
    filename = request.args.get('file')

    # VULNERABLE: No path validation
    filepath = os.path.join('/var/www/files', filename)
    with open(filepath, 'r') as f:  # Path traversal vulnerability
        content = f.read()
    return content


# Vulnerability: Race Condition (TOCTOU)
@app.route('/purchase', methods=['POST'])
def purchase():
    user_id = session.get('user_id')
    amount = float(request.form.get('amount'))

    # VULNERABLE: Check-then-act race condition
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check balance
    cursor.execute(f"SELECT balance FROM users WHERE id={user_id}")
    balance = cursor.fetchone()[0]

    if balance >= amount:  # Check
        # Race window here! Another request can pass the check
        # before this deduction happens

        # Deduct balance
        new_balance = balance - amount  # Use
        cursor.execute(
            f"UPDATE users SET balance={new_balance} WHERE id={user_id}"
        )
        conn.commit()
        return {'status': 'success', 'new_balance': new_balance}

    return {'status': 'insufficient_funds'}


# Vulnerability: Insecure Deserialization
@app.route('/load_session', methods=['POST'])
def load_session():
    session_data = request.form.get('session')

    # VULNERABLE: Deserializing untrusted data
    user_session = pickle.loads(session_data.encode())  # Deserialization vulnerability
    return {'session': user_session}


# Vulnerability: Integer Overflow
@app.route('/calculate_total', methods=['POST'])
def calculate_total():
    quantity = int(request.form.get('quantity'))
    price = int(request.form.get('price'))

    # VULNERABLE: No overflow check
    total = quantity * price  # Integer overflow possible

    if total < 0:  # Overflow happened
        return {'error': 'Invalid calculation'}

    return {'total': total}


# Vulnerability: Missing Access Control
@app.route('/admin/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # VULNERABLE: No admin check!
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id={user_id}")
    conn.commit()
    return {'status': 'deleted'}


# Vulnerability: Weak Cryptography
@app.route('/encrypt_data', methods=['POST'])
def encrypt_data():
    data = request.form.get('data')

    # VULNERABLE: Using weak/outdated encryption
    # This is a placeholder - real code might use DES, MD5, etc.
    encrypted = data[::-1]  # Extremely weak "encryption"
    return {'encrypted': encrypted}


# Vulnerability: CSRF (Cross-Site Request Forgery)
@app.route('/change_password', methods=['POST'])
def change_password():
    # VULNERABLE: No CSRF token validation
    user_id = session.get('user_id')
    new_password = request.form.get('password')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE users SET password='{new_password}' WHERE id={user_id}"
    )
    conn.commit()
    return {'status': 'password_changed'}


if __name__ == '__main__':
    # Vulnerability: Debug mode in production
    app.run(debug=True, host='0.0.0.0')  # Exposes debug info
