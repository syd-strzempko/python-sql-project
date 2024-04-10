from models.entries import Entry

def init_db_values(db):
    db.drop_all()
    db.create_all()
    entries = [
        Entry(title='Southwest', lat=29, long=-98, author='Syd'),
        Entry(title='Northeast', lat=31, long=-96, author='Syd'),
        Entry(title='Southeast', lat=29, long=-96, author='Syd'),
        Entry(title='Northwest', lat=31, long=-98, author='Brandon'),
    ]
    db.session.add_all(entries)
    db.session.commit()