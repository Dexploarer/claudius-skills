"""
Intentionally Vulnerable Web Application for Testing Bug Hunting Framework
WARNING: This code contains INTENTIONAL security vulnerabilities for testing purposes.
NEVER use this code in production or as a reference for secure coding.
"""

from flask import Flask, request, render_template_string, session, jsonify
import sqlite3
import os
import subprocess
import pickle
import hashlib
import random
import jwt
import xml.etree.ElementTree as ET
import requests

app = Flask(__name__)

# VULNERABILITY 1: Hardcoded Secret (CWE-798, CVSS 7.5)
app.secret_key = "supersecretkey12345"
API_KEY = "sk_live_51234567890abcdef"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# VULNERABILITY 2: Hardcoded Database Credentials
DB_PASSWORD = "admin123"
DB_USER = "root"

# VULNERABILITY 3: SQL Injection via String Concatenation (CWE-89, CVSS 8.5)
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # CRITICAL: SQL injection vulnerability
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE email = '" + email + "' AND password = '" + password + "'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        session['user_id'] = user[0]
        return jsonify({"success": True})
    return jsonify({"success": False}), 401

# VULNERABILITY 4: SQL Injection via String Formatting (CWE-89, CVSS 8.5)
@app.route('/search')
def search():
    query = request.args.get('q', '')
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    # CRITICAL: Another SQL injection
    sql = "SELECT * FROM products WHERE name LIKE '%" + query + "%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()
    return jsonify(results)

# VULNERABILITY 5: XSS via innerHTML (CWE-79, CVSS 6.5)
@app.route('/profile')
def profile():
    username = request.args.get('name', 'Guest')
    # CRITICAL: XSS vulnerability
    html = """
    <html>
    <body>
    <h1>Welcome!</h1>
    <script>
        document.getElementById('username').innerHTML = '{username}';
    </script>
    <div id="username"></div>
    </body>
    </html>
    """.format(username=username)
    return render_template_string(html)

# VULNERABILITY 6: Command Injection (CWE-78, CVSS 9.0)
@app.route('/ping')
def ping():
    host = request.args.get('host', 'localhost')
    # CRITICAL: Command injection with shell=True
    result = subprocess.run("ping -c 1 " + host, shell=True, capture_output=True)
    return jsonify({"output": result.stdout.decode()})

# VULNERABILITY 7: Path Traversal (CWE-22, CVSS 7.5)
@app.route('/download')
def download():
    filename = request.args.get('file')
    # CRITICAL: Path traversal vulnerability
    with open('/var/www/files/' + filename, 'r') as f:
        content = f.read()
    return content

# VULNERABILITY 8: IDOR - Insecure Direct Object Reference (CWE-639, CVSS 7.5)
@app.route('/api/users/<int:user_id>/profile')
def get_user_profile(user_id):
    # CRITICAL: No authorization check - any user can view any profile
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            "id": user[0],
            "email": user[1],
            "ssn": user[2],  # Sensitive data exposed
            "credit_card": user[3]
        })
    return jsonify({"error": "Not found"}), 404

# VULNERABILITY 9: JWT with 'none' Algorithm (CWE-287, CVSS 9.8)
@app.route('/api/token')
def generate_token():
    user_id = request.args.get('user_id')
    # CRITICAL: Accepts 'none' algorithm
    token = jwt.encode({"user_id": user_id}, app.secret_key, algorithm="HS256")
    return jsonify({"token": token})

@app.route('/api/verify')
def verify_token():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        # CRITICAL: Allows 'none' algorithm for signature bypass
        payload = jwt.decode(token, app.secret_key, algorithms=["HS256", "none"])
        return jsonify(payload)
    except:
        return jsonify({"error": "Invalid token"}), 401

# VULNERABILITY 10: Insecure Deserialization (CWE-502, CVSS 9.8)
@app.route('/load_config', methods=['POST'])
def load_config():
    config_data = request.data
    # CRITICAL: Unsafe pickle deserialization - RCE vulnerability
    config = pickle.loads(config_data)
    return jsonify({"status": "loaded", "config": str(config)})

# VULNERABILITY 11: SSRF - Server-Side Request Forgery (CWE-918, CVSS 8.0)
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    # CRITICAL: SSRF - can access internal services
    response = requests.get(url)
    return jsonify({"content": response.text})

# VULNERABILITY 12: XXE - XML External Entity (CWE-611, CVSS 7.5)
@app.route('/parse_xml', methods=['POST'])
def parse_xml():
    xml_data = request.data
    # CRITICAL: XXE vulnerability - external entities not disabled
    tree = ET.fromstring(xml_data)
    return jsonify({"parsed": str(tree)})

# VULNERABILITY 13: Race Condition (CWE-367, CVSS 9.1)
@app.route('/transfer', methods=['POST'])
def transfer_money():
    from_account = request.form['from']
    to_account = request.form['to']
    amount = float(request.form['amount'])

    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    # CRITICAL: TOCTOU race condition
    # Check balance
    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (from_account,))
    balance = cursor.fetchone()[0]

    if balance >= amount:
        # Vulnerable window here - another request could deplete balance
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?",
                      (amount, from_account))
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?",
                      (amount, to_account))
        conn.commit()
        conn.close()
        return jsonify({"success": True})

    conn.close()
    return jsonify({"error": "Insufficient funds"}), 400

# VULNERABILITY 14: Weak Cryptography (CWE-327, CVSS 5.0)
@app.route('/hash_password')
def hash_password():
    password = request.args.get('password')
    # CRITICAL: Using MD5 for password hashing
    hashed = hashlib.md5(password.encode()).hexdigest()
    return jsonify({"hash": hashed})

# VULNERABILITY 15: Insecure Random (CWE-338, CVSS 5.0)
@app.route('/reset_token')
def generate_reset_token():
    # CRITICAL: Using non-cryptographic random for security token
    token = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return jsonify({"reset_token": token})

# VULNERABILITY 16: Missing Authorization on Admin Function
@app.route('/admin/delete_user/<int:user_id>', methods=['DELETE'])
def admin_delete_user(user_id):
    # CRITICAL: No authorization check - anyone can delete users
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

# VULNERABILITY 17: eval() Code Injection (CWE-94, CVSS 9.8)
@app.route('/calculate')
def calculate():
    expression = request.args.get('expr')
    # CRITICAL: Remote code execution via eval()
    result = eval(expression)
    return jsonify({"result": result})

# VULNERABILITY 18: Price Manipulation (Business Logic)
@app.route('/checkout', methods=['POST'])
def checkout():
    item_id = request.form['item_id']
    # CRITICAL: Price comes from user input!
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])

    total = price * quantity
    return jsonify({
        "success": True,
        "total": total,
        "message": f"Charged ${total}"
    })

if __name__ == '__main__':
    # VULNERABILITY 19: Debug mode enabled in production
    app.run(debug=True, host='0.0.0.0', port=5000)
