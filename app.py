from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
import os
import sqlite3
import string
import random

app = Flask(__name__)
CORS(app)

# Initialize the database
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  long_url TEXT NOT NULL,
                  short_code TEXT NOT NULL UNIQUE)''')
    conn.commit()
    conn.close()

init_db()

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['url']
    short_code = generate_short_code()
    
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("INSERT INTO urls (long_url, short_code) VALUES (?, ?)", (long_url, short_code))
    conn.commit()
    conn.close()
    
    base_url = os.environ.get('BASE_URL', 'http://localhost:5000')
    return jsonify({'short_url': f'{base_url}/{short_code}'})

@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    result = c.fetchone()
    conn.close()
    
    if result:
        return redirect(result[0])
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)