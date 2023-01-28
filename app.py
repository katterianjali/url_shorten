import sqlite3
from flask import Flask, request, redirect, jsonify
from random import choice
import string


# Randon character generation of desired length is used as the short id for the url

def generate_short_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_of_chars))


# Connection to db is established, which can be reused throughout the application

def connect_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)


# Routine to return the shortened URL

@app.route('/shorten', methods=["POST"])
def shorten():
    conn = connect_db()
    url = request.get_json()

    # Check the database for existing match for the url to return

    url_content = conn.execute('SELECT short_id FROM url_table WHERE original_url = (?)', (url["url"],)).fetchone()

    if url_content:
        return jsonify(request.host_url + url_content[0])

    # Create new shorten url if it is not found in the database and insert it to the url table
    else:
        short_id = generate_short_id(6)
        conn.execute('INSERT INTO url_table (original_url,short_id) VALUES (?,?)', (url["url"], short_id))
        conn.commit()
        conn.close()
        return jsonify(request.host_url + short_id)


# Routine to redirect to the actual url from shorten url

@app.route('/<id>')
def actual_url_redirect(id):
    conn = connect_db()
    url_content = conn.execute('SELECT original_url FROM url_table WHERE short_id = (?)', (id,)).fetchone()
    original_url = url_content['original_url']
    conn.commit()
    conn.close()
    return redirect(original_url)
