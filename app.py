from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy import select
from werkzeug.exceptions import abort
from extensions import db
from init_db import init_db_values

from models.entries import Entry
from models.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['GOOGLE_API_KEY'] = 'AIzaSyCEjbyIQMQoeiL-_U4zM9Za4yXDkurEWmY'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

@app.before_first_request
def create_tables():
    init_db_values(db)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/new', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        lat, long = request.form['location'].split(',',2)
        associated_user = db.session.query(User).filter(User.name == request.form['user']).first()
        if (associated_user is None):
            associated_user = User(name=request.form['user'])
            db.session.add(associated_user)
        new_entry = Entry(title=request.form['title'], user=associated_user, lat=float(lat), long=float(long))
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('list'))

    return render_template('new.html')

@app.route('/list')
def list():
    # entries = Entry.query.all() Model query deprecated in 2.x
    entries = [e.to_dict(True) for e in db.session.query(Entry)]
    if entries is None:
        abort(404)
    return render_template('list.html', entries=entries)

@app.route('/entry/<int:entry_id>')
def entry(entry_id):
    # entry = Entry.query.get(entry_id) Model query deprecated in 2.x
    entry = db.session.get(Entry, entry_id)
    if entry is None:
        abort(404)
    return render_template('entry.html', entry=entry.to_dict(True))

@app.route('/user/<int:user_id>')
def user(user_id):
    user = db.session.get(User, user_id)
    if user is None:
        abort(404)
    return render_template('user.html', user=user.to_dict(True))