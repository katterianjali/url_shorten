import sqlite3
from flask import Flask, request, redirect, jsonify
from hashids import Hashids


# Connection to db is established, which can be reused throughout the application

def connect_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)
#This is our secret key for salting

app.config['SECRET_KEY'] = 'secrets die but secrecy grows'
hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])


# Routine to return the shortened URL

@app.route('/shorten', methods=["POST"])

def shorten():

    conn = connect_db()
    url = request.get_json()
    # Check the database for existing match for the url to return

    url_content = conn.execute('SELECT hash_id FROM url_table WHERE original_url = (?)', (url["url"],)).fetchone()
    if url_content:
        conn.close()
        return jsonify(request.host_url + url_content[0])
    # Create new shorten url if it is not found in the database and insert it to the url table

    else:
        url_content = conn.execute('INSERT INTO url_table (original_url) VALUES (?)',
                                    (url["url"],))

        url_id = url_content.lastrowid
        hashid = hashids.encode(url_id)
        url_content = conn.execute('UPDATE url_table SET  hash_id = (?) WHERE id = (?)',
                                (hashid, url_id))
        shorten_url = request.host_url + hashid
        conn.commit()
        conn.close()

    return shorten_url

# Routine to redirect to the actual url from shorten url

@app.route('/<id>')

def url_redirect(id):
    conn = connect_db()

    original_id = hashids.decode(id)
    if original_id:
        original_id = original_id[0]
        url_content = conn.execute('SELECT original_url FROM url_table'
                                ' WHERE id = (?)', (original_id,)
                                ).fetchone()
        original_url = url_content['original_url']
        conn.close()
        return redirect(original_url)
    else:
        return ("INVALID URL")