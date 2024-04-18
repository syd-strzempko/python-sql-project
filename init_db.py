from models.entries import Entry
from models.users import User

def init_db_values(db):
    db.drop_all()
    db.create_all()
    users = [
        User(name='Syd'),
        User(name='Brandon')
    ]
    db.session.add_all(users)
    entries = [
        Entry(title='Southwest', lat=30.25, long=-97.77, user=users[0], verified=True),
        Entry(title='Northeast', lat=30.277, long=-97.74, user=users[0], verified=True),
        Entry(title='Southeast', lat=30.24, long=-97.72, user=users[0], verified=True),
        Entry(title='Northwest', lat=30.25, long=-97.74, user=users[1]),
    ]
    db.session.add_all(entries)
    db.session.commit()