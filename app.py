from flask import Flask, render_template, request, url_for, redirect
import sqlite3
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/new', methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        conn = get_db_connection()
        conn.execute('INSERT INTO entries (title, author) VALUES (?, ?)',
                        (title, author))
        conn.commit()
        conn.close()
        return redirect(url_for('list'))

    return render_template('form.html')

@app.route('/list')
def list():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM entries').fetchall()
    conn.close()
    return render_template('list.html', entries=entries)

@app.route('/<int:entry_id>')
def entry(entry_id):
    entry = get_entry(entry_id)
    return render_template('entry.html', entry=entry)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_entry(entry_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM entries WHERE id = ?',
                        (entry_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def post_entry():
    return None